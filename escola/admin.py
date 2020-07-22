from django.contrib import admin

# Register your models here.
from escola.models import Aluno, Disciplina

admin.site.register(Aluno)
admin.site.register(Disciplina)

