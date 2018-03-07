from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


User = settings.AUTH_USER_MODEL

class Inscricao(models.Model):
   #cadastrador = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nome        = models.CharField('Nome', max_length=100, null=False, blank=False)
    documento   = models.CharField('Documento', unique=True, max_length=20, null=False, blank=False)
    orgao       = models.CharField('Órgão expedidor', max_length=50, null=False, blank=False)
    telefone    = models.CharField('Telefone', max_length=11, null=True, blank=False)
    email       = models.EmailField('Email', max_length=50, null=False, blank=False)
    observacao  = models.TextField('Descrição', blank=True)
    criado      = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado  = models.DateTimeField('Atualizado em', auto_now=True)
    
    def __str__(self):
        return 'ID: {} | Nome: {} | Documento: {} | Email: {}'.format(self.pk, self.nome, self.documento, self.email)

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

# def inscricao_pos_salvamento(sender, instance, *args, **kwargs):
#     if not kwargs['created']:
#         # CHAMAR TUA FUNÇÃO DE ENVIAR EMAIL DENTRO DESTE IF
#         pass


# post_save.connect(inscricao_pos_salvamento, sender=Inscricao)
