from django.contrib import admin
from .models        import Inscricao
import requests 

class InscricaoAdmin(admin.ModelAdmin):
    list_display  = ['id','nome','documento','orgao','telefone','email','observacao']
    search_fields = ['id','nome','documento','orgao','telefone','email','observacao']

    def save_model(self, request, obj, form, change):
        data = {
            'nome'      : request.POST.__getitem__('nome'),
            'documento' : request.POST.__getitem__('documento'),
            'orgao'     : request.POST.__getitem__('orgao'),
            'telefone'  : request.POST.__getitem__('telefone'),
            'email'     : request.POST.__getitem__('email')
        }
        requests.post('https://vc-2018-api.herokuapp.com/api/email/inscricao',data)
        obj.save()


admin.site.register(Inscricao, InscricaoAdmin)
