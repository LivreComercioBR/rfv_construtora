# from django.core.mail import send_mail
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib import messages
from django.contrib.messages import constants


def enviar_email(name, subject, email, mensagem):

    server_smtp = 'smtp-mail.outlook.com'
    port = 587
    from_addr = 'ronaldo312006@hotmail.com'
    to_addrs = ['ronaldocorreiadesouza@gmail.com', ]
    password = 'tyhcbolvirfiugco'

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
        <h4>Olá o meu nome é {name}</h4>
        <p>{subject}</p>
        <p>Este é o meu endereço de email: {email}</p>
        <p>{mensagem}</p>
    </body>
    </html>
    """
    message = MIMEMultipart()
    message["from"] = from_addr
    message["to"] = to_addrs
    message["subject"] = subject
    message.attach(MIMEText(body, "html"))

    # Conectando o servidor de smtp
    try:
        server = smtplib.SMTP_SSL(host=server_smtp, port=port)
        server.login(from_addr, password)
        server.starttls()

        server.sendmail(from_addr, to_addrs, message.as_string())
        print("Email enviado com sucesso! Em breve retornaremos o seu contato")
        # messages.add_message(request, constants.SUCCESS,
        #                      "Email enviado com sucesso! Em breve retornaremos o seu contato.")
    except Exception as erro:
        print(f"O erro encontrado foi {erro}")
        # messages.add_message(request, constants.ERROR,
        #                      f"Lamento, houve um erro {erro}")

    finally:
        server.quit()

# def enviar_email(subject, message, email, nome):
#     subject = subject
#     message = f"""O meu nome é {nome}
#                   O meu email é: {email}.

#                   {message}"""
#     from_email = "ronaldo@rfvconstrutora.com.livrecomerciobrasil.com"
#     recipient_list = "ronaldo312006@hotmail.com"
#     nome = nome
#     email = email

#     send_mail(subject, message, from_email, [
#               recipient_list, ], fail_silently=False)
