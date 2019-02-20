from django.contrib.auth import login, authenticate
from .consumer_reg_form import Consumer_registration_form
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User


def index(request):
	return render(request,'consumer/index.html',{})


def register(request):
    if request.method == 'POST':
        form = Consumer_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')

    else:
        form = Consumer_registration_form()

    return render(request, 'conReg.html', {'form':form})


# check if a user name exists
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__icontains=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = '{} already exists'.format(username)
    return JsonResponse(data)
