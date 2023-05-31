from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.contrib.auth import login
from .forms import *
from .models import *
from .functions import generated_salt, hashing, check_password
from random import randint
from datetime import datetime

def mainpage_view(request):
    games = game.objects.all()
    most_popular = games.order_by('?')[:4]
    new_games = games.order_by('-released')[:4]
    data_user = request.session.get('data_user', '')
    photos = {}
    for game_obj in games:
        photos[game_obj.id] = slider_photo.objects.filter(game_id=game_obj.id)
    if len(data_user) != 0:
        user_isauthorized = data_user[1]
        username = data_user[0]
        return render(request, 'mainpage.html', {'games': most_popular, 'new_games': new_games, 'is_authorized': user_isauthorized, 'username': username, 'game_photo': photos})
    return render(request, 'mainpage.html', {'games': most_popular, 'new_games': new_games, 'is_authorized': False, 'game_photo': photos})


@csrf_protect
def view_registration_page(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            generate_salt = generated_salt()
            feed = Buyer(
                username=form.cleaned_data['username'],
                age=form.cleaned_data['age'],
                email=form.cleaned_data['email'],
                tel_number=form.cleaned_data['telephone'],
                salt=generate_salt,
                password=hashing(form.cleaned_data['password'], generate_salt),
            )
            feed.save()
            return redirect('loginpage')
    else:
        form = UserForm()
    return render(request, 'registration.html', {'form': form})


@csrf_protect
def view_login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = Buyer.objects.filter(username=username).first()
            salt = user.salt
            if user and check_password(salt, password, user.password):
                login(request, user)
                user.is_authorized = 1
                request.session['data_user'] = [
                    user.username, user.is_authorized, user.id]
                return redirect('mainpage')
            else:
                form.add_error(None, 'Неверный логин или пароль')
    return render(request, 'login.html', {'form': form})


def view_catalog(request):
    categories = category.objects.all()
    games = game.objects.all()
    category_id = request.GET.get('category_id')
    if category_id:
        games = games.filter(category_id=category_id)
    data_user = request.session.get('data_user', '')
    photos = {}
    for game_obj in games:
        photos[game_obj.id] = slider_photo.objects.filter(game_id=game_obj.id)
    if len(data_user) != 0:
        user_isauthorized = data_user[1]
        username = data_user[0]
        return render(request, 'catalog.html', {'categories': categories, 'games': games, 'is_authorized': user_isauthorized, 'username': username, 'game_photo': photos})
    return render(request, 'catalog.html', {'categories': categories, 'games': games, 'game_photo': photos})


def view_game(request, game_id):
    buy_game = game.objects.get(id=game_id)
    cat = category.objects.get(id=buy_game.category_id)
    photos = slider_photo.objects.filter(game_id=game_id)
    title_photo = photos[0]
    data_user = request.session.get('data_user', '')
    review = reviews.objects.filter(game_id=game.objects.get(id= game_id))
    if len(data_user) != 0:
        user_isauthorized = data_user[1]
        username = data_user[0]
        buyer = Buyer.objects.get(id=data_user[2])
        games = get_object_or_404(game, id=game_id)
        pre_order_items = pre_order.objects.filter(buyer=buyer).exclude(order=None)
        list_of_buyed_game = [i.id_game.name for i in pre_order_items]
        is_buyed = str(games) in list(map(str,list_of_buyed_game))
        return render(request, 'games.html', {'game_id': game_id, 'game': buy_game, 'category': cat.name_category,'title_photo':title_photo ,'game_photo': photos[1:], 'is_authorized': user_isauthorized, 'username': username,'is_buyed':is_buyed,'review':review})
    return render(request, 'games.html', {'game_id': game_id, 'game': buy_game, 'category': cat.name_category, 'title_photo':title_photo ,'game_photo': photos[1:],'review':review})


@csrf_protect
def view_profile(request):
    data_user = request.session.get('data_user', '')
    if len(data_user) != 0:
        user_isauthorized = data_user[1]
        username = data_user[0]
        buyer = Buyer.objects.get(id=data_user[2])
        user_orders = order.objects.filter(buyer=buyer)
        pre_orders = pre_order.objects.filter(buyer=buyer)
        price = {}
        game_names = {}
        for id_oredr in user_orders:
            total_price=0
            game_name = []
            for pre_order_obj in pre_orders.filter(order=id_oredr):
                    total_price += pre_order_obj.id_game.price * pre_order_obj.count
                    game_name.append(pre_order_obj.id_game.name)
                    game_names[id_oredr.id] = game_name
                    price[id_oredr.id]=total_price
        return render(request, 'profile.html', {'is_authorized': user_isauthorized, 'username': username, 'user': buyer,'user_orders': user_orders,'price':price,'game_names':game_names})
    return render(request, 'profile.html')


@require_POST
@csrf_protect
def add_to_cart(request, game_id):
    data_user = request.session.get('data_user', '')
    if len(data_user) != 0:
        buyer = Buyer.objects.get(id=data_user[2])
        game_obj = get_object_or_404(game, id=game_id)  
        cart_obj, created = pre_order.objects.get_or_create(
            id_game=game_obj,
            buyer=buyer,
            order=None,
            defaults={
                'count': 1
            }
        )
        if not created:
            cart_obj.count += 1
            cart_obj.save()
        
        return redirect('basket')
    else:
        return redirect('loginpage')

def remove_from_cart(request, pre_order_id):
    pre_order_obj = get_object_or_404(pre_order, id=pre_order_id)
    pre_order_obj.delete()
    return redirect('basket')

def view_basket(request):
    data_user = request.session.get('data_user', '')
    if len(data_user) != 0:
        user_isauthorized = data_user[1]
        username = data_user[0]
        basket_is_null=True
        try:
            buyer = Buyer.objects.get(id=data_user[2])
            Pre_orders = pre_order.objects.filter(buyer=buyer, order=None)
            total_price = 0
            for pre_order_obj in Pre_orders:
                total_price += pre_order_obj.id_game.price * pre_order_obj.count
            basket_is_null = False
            return render(request, 'basket.html', {'is_authorized': user_isauthorized, 'username': username, 'pre_orders': Pre_orders,'is_null':basket_is_null,'total':total_price})
        except:
            return render(request, 'basket.html', {'is_authorized': user_isauthorized, 'username': username,'is_null':basket_is_null})
    return redirect('loginpage')

def order_success(request):
    data_user = request.session.get('data_user', '')
    if len(data_user) != 0:
        buyer = Buyer.objects.get(id=data_user[2])
        orders = order.objects.create(
            buyer=buyer,
            compleate = True
        )
        pre_orders = pre_order.objects.filter(buyer=buyer, order=None)
        for pre_order_item in pre_orders:
            pre_order_item.order = orders
            pre_order_item.save()
        return render(request, 'order_success.html')
    else:
        return redirect('loginpage')

def add_review(request, game_id):
    data_user = request.session.get('data_user', '')
    if len(data_user) != 0:
        game_obj = game.objects.get(id=game_id)
        if request.method == 'POST':
            author = request.POST['author']
            review_text = request.POST['review']
            review = reviews(author=author, reviews=review_text, game_id=game_obj)
            review.save()
            return redirect('game', game_id=game_id)
    else:
        return redirect('mainpage')
@csrf_protect
def logout_view(request):
    data_user = request.session.get('data_user', '')
    if len(data_user) != 0:
        user = Buyer.objects.get(id=data_user[2])
        user.is_authorized = 0
        user.save()
        del request.session['data_user']
    return redirect('mainpage')

def dbpanel(request):
    data_user = request.session.get('data_user', '')
    if len(data_user) != 0:
        user = Buyer.objects.get(id=data_user[2])
        if (not user.is_superuser):
            return redirect('mainpage')
        buyers = Buyer.objects.all()
        categories = category.objects.all()
        games = game.objects.all()
        slider_photos = slider_photo.objects.all()
        orders = order.objects.all()
        pre_orders = pre_order.objects.all()
        all_reviews = reviews.objects.all()

        context = {
            'buyers': buyers,
            'categories': categories,
            'games': games,
            'slider_photos': slider_photos,
            'orders': orders,
            'pre_orders': pre_orders,
            'reviews': all_reviews,
            'is_authorized':data_user[1],
            'username':data_user[0]
        }
        return render(request, 'dbpanel.html', context)
    redirect('mainpage')