from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponse
from datetime import datetime

import json


def index(request, *args, **kwargs):
    return render(request, 'banco_chile/index.html')


@login_required(login_url='/')
def details(request, *args, **kwargs):
    user = request.user
    current_datetime = datetime.now()

    context = { 'user': user, 'current_datetime': current_datetime }
    return render(request, 'banco_chile/details.html', context=context)


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('index')


def asset_logo_file(response):
    img = open('banco_chile/static/banco_chile/assets/images/logo-bec.png', 'rb')
    response = FileResponse(img)

    return response


def favicon(response):
    img = open('banco_chile/static/banco_chile/assets/images/favicon.ico', 'rb')
    response = FileResponse(img)

    return response


def auth_cred_submit(request, *args, **kwargs):
    data = json.loads(request.body)
    user = authenticate(request=request, username=data["username"], password=data["password"])

    if user is not None:
        login(request, user)
        return HttpResponse('ok')

    return HttpResponse("Usuario o contraseña incorrectos", status=401)