from django.shortcuts import render

# Create your views here.
def blog(request):
    # print("passei pelo artigo")
    return render(
        request,
        'blog/index.html'
    )
