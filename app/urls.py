
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.mainpage,name="home"),
    #cities
    path('vijayawada/', views.vijayawada ,name='vijayawada'),
    path('banglore/', views.banglore ,name='banglore'),
    path('amaravathi/', views.amaravathi ,name='amaravathi'),
    path('chennai/', views.chennai ,name='chennai'),
    path('hyd/', views.hyd ,name='hyd'),
    path('vizag/', views.vizag ,name='vizag'),
    #user
    path('login/',views.login_user,name="login"),
    path('accounts/login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('register/',views.register_user,name='register'),
    path('edit_profile/', views.edit_profile ,name='edit_profile'),
    path('change_password/',views.change_password,name='change_password'),
    #events
    path('birthday/', views.birthday ,name='birthday'),
    path('wedding/', views.wedding ,name='wedding'),
    path('babyshower/', views.babyshower ,name='babyshower'),
    path('surprise/', views.surprise ,name='surprise'),
    path('bachelor/', views.bachelor ,name='bachelor'),
    path('saree/', views.saree ,name='saree'),
    #event items
    path('cupcakes/', views.cupcakes ,name='cupcakes'),
    path('returngifts/', views.returngifts ,name='returngifts'),
    path('hydhalls/', views.HydHallView.as_view(), name='hydhalls'),
    path('hydgifts/', views.HydGiftView.as_view(), name='hydgifts'),
    path('hyddecorations/', views.HydDecorateView.as_view(), name='hyddecorations'),
    path('hydcakes/', views.HydCakeView.as_view(), name='hydcakes'),
    path('detail/<int:pk>/', views.cupcakeDetailView.as_view(), name="detail"),
    path('detaildecoration/<int:pk>/', views.HydDecorateDetailView.as_view(), name="detaildecoration"),
    path('detailgift/<int:pk>/', views.ReturngiftDetailView.as_view(), name="detailgift"),
    path('detailchocolate/<int:pk>/', views.HydGiftDetailView.as_view(), name="detailchocolate"),
    path('detailhall/<int:pk>/', views.HydHallDetailView.as_view(), name="detailhall"),
    path('detailcake/<int:pk>/', views.HydCakeDetailView.as_view(), name="detailcake"),
    #bachelor
    path('farmhouse/', views.Farmhouseview.as_view() ,name='farmhouse'),
    path('villas/', views.VillasView.as_view() ,name='villas'),
    path('pubs/', views.pubView.as_view() ,name='pubs'),
    path('entertainment/', views.entertainmentView.as_view() ,name='entertainment'),
    path('outstation/', views.outstationView.as_view(),name='outstation'),
    path('detailout/<int:pk>/', views.outstationDetailView.as_view(), name="detailout"),
    #marriage event
    path('halls/',views.MrghallView.as_view(),name="halls"),
    path('food/',views.MrgfoodView.as_view(),name="food"),
    path('gift/',views.MrggiftsView.as_view(),name="gift"),
    path('mandap/',views.MrgmandapView.as_view(),name="mandap"),
    path('halls/',views.MrghallView.as_view(),name="halls"),
    path('sangeeth/',views.MrgsangeethView.as_view(),name="sangeeth"),
    path('party/',views.MrgpartyView.as_view(),name="party"),
    
    
    
    #addtocart
    path('cart/',views.cart,name="cart"),
    path('feedback/',views.feedback_form,name="feedback"),
    #path('cart/id/',views.CartDetailView.as_view(),name="cart"),
    path('gotocart/',views.gotocart,name="gotocart"),
    path('payment/',views.payment,name="payment"),
    path('confirmation/',views.confirmation,name="confermation"),
    path('paymentsuccess/',views.success,name="success"),
    path('thankyou/',views.thankyou,name="thankyou"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('gallery/',views.gallery,name="gallery"),
]
