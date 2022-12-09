from django.shortcuts import render


def index(request):
    context = {

    }
    return render(request, 'posts/index.html', context)


def profile(request, username):
    context = {

    }
    return render(request, 'posts/profile.html', context)