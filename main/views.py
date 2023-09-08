from django.shortcuts import render

def show_main(request):
    context = {
        'appname' : 'DEKAPPY',
        'name': 'Dinda Kirana Khairunnisa',
        'class': 'PBP C',
    }

    return render(request, "main.html", context)
