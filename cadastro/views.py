from django.shortcuts import render

# Create your views here.
def cadastro(request):
    # print("passei pelo artigo")
    return render(
        request,
        'cadastro/index.html'
    )
