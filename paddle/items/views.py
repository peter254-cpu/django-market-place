from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import NewItemForm

def detail(request,pk):
	item=get_object_or_404(Item, pk=pk)
	related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
	return render(request, 'items/detail.html',locals())

@login_required
def new(request):
	if request.method=='POST':
		form=NewItemForm(request.POST,request.FILES)

		if form.is_valid():
			item = form.save(commit=False)
			item.created_by = request.user
			item.save()
			return redirect('items:detail', pk = item.id)
	else:
		form =NewItemForm()
		
	title = 'new item'
	return render(request, 'items/form.html',locals())


# Create your views here.
