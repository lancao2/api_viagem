from django.shortcuts import render

# Create your views here.
def blog(request):
    # print("passei pelo artigo")
    contexto = {
            'titulo': 'Jornada Viagem | blog'
    }
    return render(request, 'blog/index.html', contexto )
