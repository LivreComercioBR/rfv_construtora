from django.shortcuts import render
from .models import Usuario, Video, Obra, BannerCliente, AreaAtuacao, Cliente, Team
from django.contrib import messages
from django.contrib.messages import constants
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket


def homepage(request):
    # video = Video.objects.get(id=1)
    # banner = BannerCliente.objects.get(id=1)
    areas_atuacao = AreaAtuacao.objects.all()
    obras = Obra.objects.all()[0:6]

    if request.method == "GET":

        return render(request, "index.html", {"obras": obras, "areas_atuacao": areas_atuacao})

    elif request.method == "POST":
        nome = request.POST.get("username")
        assunto = request.POST.get("assunto")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        mensagem = request.POST.get("mensagem")

        server_smtp = 'mail.livrecomerciobrasil.com'
        port = 465
        from_addr = 'administrador@livrecomerciobrasil.com'
        to_addrs = 'comercial@construtorarfv.com.br'
        password = ' '

        # Configurações do email
        body = f"""
        <!doctype html>
        <html lang="pt-br">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Contato via Site</title>
        </head>
        <body>
            <h4>Olá o meu nome é {nome}</h4>
            <p><b>Assunto</b>: {assunto}</p>
            <p><b>E-mail</b>: {email}</p>
            <p><b>Telefone</b>: {telefone}</p>
            <p>{mensagem}</p>
        </body>
        </html>
        """
        message = MIMEMultipart()
        message["from"] = from_addr
        message["to"] = to_addrs
        message["subject"] = assunto
        message.attach(MIMEText(body, "html"))

        # Conectando o servidor de smtp
        try:

            server = smtplib.SMTP_SSL(host=server_smtp, port=port)
            # server.starttls()

            server.login(from_addr, password)
            socket.getaddrinfo('localhost', 8080)

            server.sendmail(from_addr, to_addrs, message.as_string())
            print("Email enviado com sucesso! Em breve retornaremos o seu contato")
            messages.add_message(request, constants.SUCCESS,
                                 "Email enviado com sucesso! Em breve retornaremos o seu contato.")
        except Exception as erro:
            print(f"O erro encontrado foi {erro}")
            messages.add_message(request, constants.ERROR,
                                 f"Lamento, houve um erro {erro}")

        finally:
            server.quit()

    return render(request, "index.html", {"obras": obras, "areas_atuacao": areas_atuacao})


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
        telefone = request.POST.get("telefone")
        mensagem = request.POST.get("mensagem")

        server_smtp = 'mail.livrecomerciobrasil.com'
        port = 465
        from_addr = 'administrador@livrecomerciobrasil.com'
        to_addrs = 'ronaldocorreiadesouza@gmail.com'
        password = 'Rv604180*'

        # Configurações do email
        body = f"""
        <!doctype html>
        <html lang="pt-br">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Contato via Site</title>
        </head>
        <body>
            <h4>Olá o meu nome é {nome}</h4>
            <p><b>Assunto</b>: {assunto}</p>
            <p><b>E-mail</b>: {email}</p>
            <p><b>Telefone</b>: {telefone}</p>
            <p>{mensagem}</p>
        </body>
        </html>
        """
        message = MIMEMultipart()
        message["from"] = from_addr
        message["to"] = to_addrs
        message["subject"] = assunto
        message.attach(MIMEText(body, "html"))

        # Conectando o servidor de smtp
        try:

            server = smtplib.SMTP_SSL(host=server_smtp, port=port)
            # server.starttls()

            server.login(from_addr, password)
            socket.getaddrinfo('localhost', 8080)

            server.sendmail(from_addr, to_addrs, message.as_string())

            messages.add_message(request, constants.SUCCESS,
                                 "Email enviado com sucesso! Em breve retornaremos o seu contato.")
        except Exception as erro:

            messages.add_message(request, constants.ERROR,
                                 f"Lamento, houve um erro {erro}")

        finally:
            server.quit()

    return render(request, "contatos.html")


def institucional(request):
    team = Team.objects.all()
    return render(request, 'institucional.html', {"team": team})
