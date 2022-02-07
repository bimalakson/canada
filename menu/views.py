from django.shortcuts import render

# Create your views here.
def menu(request):
    context = {}
    return render(request, 'menu/menu.html', context)
