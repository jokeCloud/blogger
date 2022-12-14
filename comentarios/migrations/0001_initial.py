# Generated by Django 4.1.4 on 2022-12-08 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_alter_post_autor_post_alter_post_categoria_post_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_comentario', models.CharField(max_length=150)),
                ('email_comentario', models.EmailField(max_length=254, verbose_name='Email')),
                ('comentario', models.TextField()),
                ('data_comentario', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
                ('publicado_comentario', models.BooleanField(default=False, verbose_name='Publicado')),
                ('post_comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('usuario_comentario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
