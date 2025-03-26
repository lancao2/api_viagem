from django.shortcuts import render

# Create your views here.
def pacotes(request):
    # print("passei pelo artigo")
    return render(
        request,
        'pacotes/index.html'
    )