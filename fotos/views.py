from django.shortcuts import render

# Create your views here.
def fotos(request):
    # print("passei pelo artigo")
    contexto = {
            'titulo': 'Jornada Viagem | Fotos'
    }
    return render(
        request,
        'fotos/index.html',
        contexto
    )
