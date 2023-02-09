from django.contrib import admin

from Academia.models import Aluno, Professor, Aulas
# Register your models here.

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Aulas)