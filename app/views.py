from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm,EditProfileForm,FeedbackForm
from .models import CupCakes,Farmhouses,Villas,pubs,outstation,entertainment,Add_to_cart,Products,ReturnGift, Hydhalls, Hydbdaygifts, Hydbdaydecoration ,Hydbdaycakes,Hydmrghalls,Hydmrgbachelorparty,Hydmrgsangeethdecoration,Hydmrgfood,Hydmrgmandapdecoration,Hydmrggifts
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# main pages
def banglore(request):
    return render(request,'cities/banglore.html')
def chennai(request):
    return render(request,'cities/chennai.html')
def hyd(request):
    return render(request,'cities/hyd.html')
def vizag(request):
    return render(request,'cities/vizag.html') 
def amaravathi(request):
    return render(request,'cities/amaravathi.html')  
def vijayawada(request):
    return render(request,'cities/vijayawada.html')  
def mainpage(request):
    
    return render(request,'mainpage.html')
# login logout signup

def login_user(request): 
    if request.method == 'POST':
        username = request.POST['username']

        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request,('you have successfully logged in'))
            return redirect('home')
        else:
            messages.success(request,('error login'))
            return redirect('login')

    else:
        return render(request,'profile/login.html')    
def logout_user(request):
    logout(request)
    messages.success(request,('you have been logged out....'))
    return redirect('home')

def register_user(request):
    if request.method=='POST':
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request,('you have Registered...'))
            return redirect('home')

    else:
        form =SignUpForm()
    context = {'form':form}
    return render(request,'profile/register.html',context)

def edit_profile(request):
    if request.method=='POST':
        form =EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
           
            messages.success(request,('you have Edited your profile...'))
            return redirect('home')

    else:
        form =EditProfileForm (instance=request.user)
    context = {'form':form}
   
    return render(request,'profile/edit_profile.html',context)

def change_password(request):
    if request.method=='POST':
        form =PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,('you have Edited your password...'))
            return redirect('home')

    else:
        form =PasswordChangeForm (user=request.user)
    context = {'form':form}
   
    return render(request,'profile/change_password.html',context)
    # events
def birthday(request):
    return render(request,'events/birthday.html')
def wedding(request):
    return render(request,'events/wedding.html')
def babyshower(request):
    return render(request,'events/babyshower.html')
def surprise(request):
    return render(request,'events/surpriseparty.html')
def saree(request):
    return render(request,'events/sareefn.html')
def bachelor(request):
    return render(request,'events/bachelorsparty.html')    

# event items
def cupcakes(request):
    context={

'cupcakes':CupCakes.objects.all()
    }
    return render(request,'eventitems/cipcakes.html',context)

def returngifts(request):
    context={

'returngift':ReturnGift.objects.all()
    }
    return render(request,'eventitems/ReturnGift.html',context)

class cupcakeView(LoginRequiredMixin,ListView):
    template_name = 'eventitems/cipcakes.html'
    model = CupCakes
    context_object_name = 'cupcakes'


class cupcakeDetailView(DetailView):
    template_name = 'details/_detail.html'
    model = CupCakes
    context_object_name = 'cupcake'    

class ReturngiftView(LoginRequiredMixin,ListView):
    template_name = 'eventitems/ReturnGift.html'
    model = ReturnGift
    context_object_name = 'Gifts'
class ReturngiftDetailView(DetailView):
    template_name = 'details/detailgifts.html'
    model = ReturnGift
    context_object_name = 'gift'   

class HydHallView(LoginRequiredMixin,ListView):
    template_name = 'eventitems/Hydhalls.html'
    model = Hydhalls
    context_object_name = 'halls'


class HydHallDetailView(DetailView):
    template_name = 'details/detailhall.html'
    model = Hydhalls
    context_object_name = 'hall'


# 88***************************************************8


class HydGiftView(LoginRequiredMixin,ListView):
    template_name = 'eventitems/hydgifts.html'
    model = Hydbdaygifts
    context_object_name = 'gifts'


class HydGiftDetailView(DetailView):
    template_name = 'details/detailchocolate.html'
    model = Hydbdaygifts
    context_object_name = 'gift'


# *****************************************************************

class HydDecorateView(LoginRequiredMixin,ListView):
    template_name = 'eventitems/hyddecoration.html'
    model = Hydbdaydecoration
    context_object_name = 'decorations'


class HydDecorateDetailView(DetailView):
    template_name = 'details/detaildecoration.html'
    model = Hydbdaydecoration
    context_object_name = 'decoration'

#***********************************************************************

class HydCakeView(LoginRequiredMixin,ListView):
    template_name = 'eventitems/hydcake.html'
    model = Hydbdaycakes
    context_object_name = 'cakes'


class HydCakeDetailView(DetailView):
    template_name = 'details/detailcake.html'
    model = Hydbdaycakes
    context_object_name = 'cake'



#!@#$%^&*()_+*******************
#marriage
class MrghallView(LoginRequiredMixin,ListView):
    template_name = 'eventitems/marriage/halls.html'
    model = Hydmrghalls
    context_object_name = 'halls'

class MrgfoodView(ListView):
    template_name = 'eventitems/marriage/food.html'
    model = Hydmrgfood
    context_object_name = 'food'

class MrgfoodDetailView(DetailView):
    template_name = 'details/_detail.html'
    model = Hydmrgfood
    context_object_name = 'foo'    

class MrggiftsView(ListView):
    template_name = 'eventitems/marriage/gifts.html'
    model = Hydmrggifts
    context_object_name = 'gifts'

class MrgmandapView(ListView):
    template_name = 'eventitems/marriage/mandap.html'
    model = Hydmrgmandapdecoration
    context_object_name = 'mandap'

class MrgsangeethView(ListView):
    template_name = 'eventitems/marriage/sangeeth.html'
    model = Hydmrgsangeethdecoration
    context_object_name = 'sangeeth'

class MrgpartyView(ListView):
    template_name = 'eventitems/marriage/party.html'
    model = Hydmrgbachelorparty
    context_object_name = 'party'
#*******************************************
#bachelor
class Farmhouseview(LoginRequiredMixin,ListView):
    template_name = 'eventitems/bachelor/farm.html'
    model = Farmhouses
    context_object_name = 'farm'


class FarmhouseDetailView(DetailView):
    template_name = 'details/party/farm.html'
    model = Farmhouses
    context_object_name = 'farm'
class VillasView(LoginRequiredMixin,ListView):
    template_name = 'eventitems/bachelor/villas.html'
    model = Villas
    context_object_name = 'villa'


class villasDetailView(DetailView):
    template_name = 'details/party/villa.html'
    model = Villas
    context_object_name = 'villa'
class pubView(LoginRequiredMixin,ListView):
    template_name = 'eventitems/bachelor/pub.html'
    model = pubs
    context_object_name = 'pub'


class pubDetailView(DetailView):
    template_name = 'details/party/pub.html'
    model = pubs
    context_object_name = 'pub'
class outstationView(LoginRequiredMixin,ListView):
    template_name = 'eventitems/bachelor/outstation.html'
    model = outstation
    context_object_name = 'out'


class outstationDetailView(DetailView):
    template_name = 'details/party/out.html'
    model = outstation
    context_object_name = 'out'
class entertainmentView(LoginRequiredMixin,ListView):
    template_name = 'eventitems/bachelor/entertainment.html'
    model = entertainment
    context_object_name = 'enter'


class entertainmentDetailView(DetailView):
    template_name = 'details/party/entertainment.html'
    model = entertainment
    context_object_name = 'enter'                
#****************************************888
#ADD TO CART    
   
@login_required
def cart(request):
    user=request.user
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    c=0
    context={
                'cartitems':Add_to_cart.objects.all()
                
            } 
    print(request.POST.get("btnminus"))
    print("--------------------")
    print(type(request.POST.get("btnminus")))
    tp=0
    
    for e in Products.objects.all():
        if (e.person in user.username ):
            print("im here")
            
            if(e.name == request.POST.get("name")):
                c=100
                if(request.POST.get("btnminus") == "-1"):

                    e.noofitems=e.noofitems-1
                    e.totalprice=e.totalprice-e.price
                    e.save()
                    break
                else:
                    e.noofitems=e.noofitems+1
                    e.totalprice=e.totalprice+e.price
                    e.save()
                    print(6666666666666666666666666666666,"im in if",777777777777)
                    break;
        else:
            c=0
            
    if( c == 0):
        
        print('0000000000')
        # print(pro)   
        a=Add_to_cart()
        p=Products()
        p.name=request.POST.get("name")
        p.price=request.POST.get("price")
        p.noofitems=1
        p.image=request.POST.get("image")
        p.totalprice=request.POST.get("price")
        p.person=request.user
        a.manager=request.user
        p.save()
        a.save()

        a.product.add(p)
       
        
        context={
                'cartitems':Add_to_cart.objects.all()
                
            }   

    
    return render(request,'cart.html',context)



    
def gotocart(request):
    context={
        'cartitems':Add_to_cart.objects.all()
        
    }
    return render(request,'cart.html',context)
def payment(request):
    return render(request,'payment.html')

class CartDetailView(DetailView):
    model = Add_to_cart
    template_name = "cart.html"
    context_object_name='cart'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for key,value in context:
            print(value)
        return context
    

class CartDeleteView(DeleteView):
    model = Add_to_cart
    template_name = "checkout.html"


def success(request):
    cartitems=Add_to_cart.objects.all()
    for i in cartitems:
        print(i.manager)
        print(request.user.username ==  i.manager )
        if(i.manager.username == request.user.username):
            
            i.delete()



    return render(request,'additional/paymentsuccessfull.html')

def thankyou(request):
    return render(request,'additional/thankyou.html')

def confirmation(request):
    return render(request,'additional/conformation.html')

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'form/feedback_form.html', {'form': form})    
def contact(request):
    return render(request,'additional/contact.html')

def about(request):
    return render(request,'additional/aboutus.html')
def gallery(request):
    return render(request,'additional/gallery.html')    