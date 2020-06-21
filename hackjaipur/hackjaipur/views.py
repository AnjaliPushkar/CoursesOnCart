from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, auth
# from django.contrib import auth

def homepage1(request):
    return render(request, 'shop/homepage.html')

# def login(request):
#     if request.method == 'POST':
#         user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
#         if user is not None:
#             auth.login(request, user)
#             return render(request, 'shop/homepage1.html')
#         else:
#             return render(request, 'shop/login.html', {'error':'user not found..!!'})
#     else:
#         return render(request, 'shop/login.html')
#
# def newuser(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.get(email=request.POST['email'])
#                 return render(request, 'shop/newuser.html', {'error': 'Email Id has already been taken'})
#             except User.DoesNotExist :
#                 user = User.objects.create_user(username =request.POST['username'], password =request.POST['password1'], email=request.POST['email'])
#                 auth.login(request, user)
#                 return render(request, 'shop/login.html')
#         else:
#             return render(request, 'shop/newuser.html', {'error': 'password not matching'})
#     else:
#         return render(request, 'shop/newuser.html')
