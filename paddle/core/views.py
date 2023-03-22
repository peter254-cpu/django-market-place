from django.shortcuts import render,redirect
from items.models import Category,Item
from .forms import SignUpForm,LoginForm

def contact(request):
    return render(request,'core/contact.html')


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request, 'core/index.html',locals())

# Create your views here.
def signUp(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('/login')
    else:
       form = SignUpForm()
    return render(request, 'core/signup.html',locals())

