from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class Usuario(AbstractUser, UserManager):
    username = models.CharField(max_length=114, unique=True)
    email = models.EmailField(max_length=264)
    password = models.CharField(max_length=264)

    def __str__(self) -> str:
        return self.username


class Video(models.Model):
    link = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.link


class BannerCliente(models.Model):
    thumb = models.ImageField(upload_to='thumb_banner')

    def __str__(self) -> str:
        return self.thumb.url


class Foto(models.Model):
    img = models.ImageField(upload_to="fotos_obras")

    def __str__(self) -> str:
        return self.img.url


class Obra(models.Model):
    nome_da_obra = models.CharField(max_length=150)
    endereco = models.CharField(max_length=250, blank=True, null=True)
    detalhes = models.TextField(max_length=2000, blank=True, null=True)
    imagens = models.ManyToManyField(
        Foto, related_name="foto_obra", blank=True)
    thumb_video = models.ImageField(
        upload_to='thumb_video', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nome_da_obra


class AreaAtuacao(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="area_atuacao", blank=True, null=True)

    def __str__(self) -> str:
        return self.titulo


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to="logos_clientes", blank=True, null=True)

    def __str__(self) -> str:
        return self.nome


class Team(models.Model):
    nome = models.CharField(max_length=150)
    função = models.CharField(max_length=100, blank=True, null=True)
    foto = models.ImageField(upload_to="fotos_team", blank=True, null=True)

    def __str__(self) -> str:
        return self.nome


class Logomarca(models.Model):
    img = models.ImageField(upload_to="logomarca")

    def __str__(self) -> str:
        return self.img.url
