import requests
from django.forms import ModelForm

from .models import Comentario


class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6Lfey3IjAAAAANGHMt1jRzS7RIlU860URVU5_Udw',
                'response': recaptcha_response
            }
        )
        recaptcha_result = recaptcha_request.json()

        if not recaptcha_result.get('success'):
            self.add_error(
                'comentario',
                'Desculpe Mr. Robot, ocorreu um erro'
            )

        # https://www.google.com/recaptcha/api/siteverify
        # secret key
        # resposta captcha

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        # email = data.get('email_comentario')
        # comentario = data.get('comentario')

        if len(nome) < 5:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais que 5 caracteres.'
            )

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')
