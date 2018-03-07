from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


User = settings.AUTH_USER_MODEL

class Inscricao(models.Model):
    nome          = models.CharField     ( 'Nome',            max_length=100,  null =False, blank=False)
    documento     = models.CharField     ( 'Documento',       unique    =True, null =False, blank=False, max_length=20 )
    orgao         = models.CharField     ( 'Órgão expedidor', max_length=50,   null =False, blank=False)
    ano_conclusao = models.CharField     ( 'Ano de conclusão do ensino médio', max_length=4, null=False, blank=False)
    telefone      = models.CharField     ( 'Telefone',  max_length=11, null=True,  blank=False)
    email         = models.EmailField    ( 'Email',     max_length=50, null=False, blank=False)
    observacao    = models.TextField     ( 'Descrição', blank=True)
    criado        = models.DateTimeField ( 'Criado em',     auto_now_add=True)
    atualizado    = models.DateTimeField ( 'Atualizado em', auto_now    =True)
    
    def __str__(self):
        return 'ID: {} | Nome: {} | Documento: {} | Email: {}'.format(self.pk, self.nome, self.documento, self.email)

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
