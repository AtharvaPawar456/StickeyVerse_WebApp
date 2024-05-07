# stickeyverse_app/views.py

from django.shortcuts import render
from .models import Sticker

def home(request):
    stickers = Sticker.objects.all()
    return render(request, 'stickeyverse_app/home.html', {'stickers': stickers})

def all_sticker(request):
    stickers = Sticker.objects.all()
    return render(request, 'stickeyverse_app/all_sticker.html', {'stickers': stickers})

def categories(request):
    categories = Sticker.objects.all()

    all_prods = []
    catProds = Sticker.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Sticker.objects.filter(category=cat)
        n = len(categories)
        all_prods.append([prod, n]) 

    params = {
        'catproducts' : all_prods,
        'allproducts' : categories,
              }

    # return render(request,'tze/index.html', params)
    return render(request, 'stickeyverse_app/categories.html', params)

def new_arrivals(request):
    stickers = Sticker.objects.order_by('-id')[:5]
    return render(request, 'stickeyverse_app/new_arrivals.html', {'stickers': stickers})

def contact(request):
    return render(request, 'stickeyverse_app/contact.html')

def about(request):
    return render(request, 'stickeyverse_app/about.html')
