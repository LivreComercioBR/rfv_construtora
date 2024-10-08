# Generated by Django 5.1 on 2024-08-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultora_app', '0002_bannercliente_foto_video_obra'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaAtuacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='area_atuacao')),
            ],
        ),
    ]
