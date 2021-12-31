from django.shortcuts import render

import contatos


def index(request):
    return render(request, 'contatos/index.html')