from django.shortcuts import render

# Create your views here.
def pacotes(request):
    # print("passei pelo artigo")
    contexto = {
            'titulo': 'Jornada Viagem | Pacotes'
    }
    return render(
        request,
        'pacotes/index.html',
        contexto
    )