from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Create your views here.
def create_item (request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'myapp/item_form.html',{'form':form})

def item_list(request):
    items = Item.objects.all()
    return render(request,'myapp/item_list.html',{'items': items})


def update_item(request, id):
    item = get_object_or_404(Item, id = id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance= item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request,'myapp/item_form.html',{'form':form})


def delete_item(request, id ):
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'myapp/item_confirm_delete.html',{'item':item})