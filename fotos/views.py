from django.shortcuts import render

# Create your views here.
def fotos(request):
    # print("passei pelo artigo")
    return render(
        request,
        'fotos/index.html'
    )
