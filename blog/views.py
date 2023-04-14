from django.shortcuts import render


def base(request, name):
    return render(request, 'blog/index.html', {'name': name})

