from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario, Video, Obra, BannerCliente, AreaAtuacao, Cliente, Team
from .utils import enviar_email
# Create your views here.


def homepage(request):
    video = Video.objects.get(id=1)
    banner = BannerCliente.objects.get(id=1)
    areas_atuacao = AreaAtuacao.objects.all()

    return render(request, "index.html", {"video": video, "banner": banner, "areas_atuacao": areas_atuacao})


def areas_atuacao(request):
    areas = AreaAtuacao.objects.all()

    return render(request, 'areas_atuacao.html', {"areas": areas})


def area_atuacao(request, id):
    areas = AreaAtuacao.objects.filter(id=id)

    return render(request, 'area_atuacao.html', {"areas": areas})


def obras(request):
    obras = Obra.objects.all()

    return render(request, 'obras.html', {"obras": obras})


def obra(request, id):
    obra = Obra.objects.get(id=id)

    return render(request, 'obra.html', {"obra": obra})


def clientes(request):
    clientes = Cliente.objects.all()

    return render(request, "clientes.html", {"clientes": clientes})


def contato(request):
    if request.method == "GET":
        return render(request, "contatos.html")
    elif request.method == "POST":
        nome = request.POST.get("username")
        assunto = request.POST.get("assunto")
        email = request.POST.get("email")
        mensagem = request.POST.get("mensagem")

        enviar_mensagem = enviar_email(
            subject=assunto, message=mensagem, email=email, nome=nome)

    return render(request, "contatos.html")


def institucional(request):
    team = Team.objects.all()
    return render(request, 'institucional.html', {"team": team})
