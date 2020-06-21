from django.shortcuts import render, get_object_or_404
from .models import Blog, Product
from math import ceil
# from history.mixins import ObjectViewMixin
# from django.views.generic import ListView, DetailView, ObjectView
# Create your views here.
from django.http import HttpResponse

# def index(request):
#     return render(request, 'shop/index.html')

def index(request):
        model = Product
        # products = Product.objects.all()
        # print(products)
        # n = len(products)
        # nSlides = n//4 + ceil((n/4)-(n//4))

        allProds = []
        catprods = Product.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Product.objects.filter(category=cat)
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append([prod, range(1, nSlides), nSlides])
        params = {'allProds':allProds}
        return render(request, 'shop/index.html', params)
        # myitem = Product.objects.all()
        # print(myitem)
        # return render(request, 'shop/index.html',{'myitem': myitem})


# class index(ListView):
#     def get(self, request):
#         model = Product
#         # products = Product.objects.all()
#         # print(products)
#         # n = len(products)
#         # nSlides = n//4 + ceil((n/4)-(n//4))
#
#         allProds = []
#         catprods = Product.objects.values('category', 'id')
#         cats = {item['category'] for item in catprods}
#         for cat in cats:
#             prod = Product.objects.filter(category=cat)
#             n = len(prod)
#             nSlides = n // 4 + ceil((n / 4) - (n // 4))
#             allProds.append([prod, range(1, nSlides), nSlides])
#         params = {'allProds':allProds}
#         return render(request, 'shop/index.html', params)
#

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)
#

def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product':product[0]})
# class productView(ObjectViewMixin, DetailView):
#     model = Product
#     template_name = 'shop/prodView.html'
    # def get(self, request):
    #     Fetch the product using the id
    #     product = Product.objects.filter(id=pk)
    #     return render(request, 'shop/prodView.html')

def about(request):
    return render(request, 'shop/about.html')

def blog(request):
    # return render(request, 'shop/blog.html')
    myposts = Blog.objects.all()
    print(myposts)
    return render(request, 'shop/blog.html',{'myposts': myposts})

def contact(request):
    thank = False
    if request.method=="POST":
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        query = request.POST.get('query', '')
        contact = Contact(username=username, email=email, phone=phone, query=query)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})
#
# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#     return render( request, 'shop/login.html')
