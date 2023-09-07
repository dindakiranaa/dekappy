from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Percy Jackson',
        'stocks': '2',
        'description' : 'Twelve-year-old Percy Jackson is on the most dangerous quest of his life. With the help of a satyr and a daughter of Athena, Percy must journey across the United States to catch a thief who has stolen the original weapon of mass destruction — Zeus’ master bolt. Along the way, he must face a host of mythological enemies determined to stop him.'
    }

    return render(request, "main.html", context)
