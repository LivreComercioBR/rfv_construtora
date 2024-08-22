from django.core.mail import send_mail


def enviar_email(subject, message, email, nome):
    subject = subject
    message = f"O meu nome é {nome} e o meu email é: {email}. {message}"
    from_email = "enginner3059@gmail.com"
    recipient_list = "ronaldo312006@hotmail.com"
    nome = nome
    email = email

    send_mail(subject, message, from_email, [
              recipient_list, ], fail_silently=False)
