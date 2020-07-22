from django.db import models

# Create your models here.


class Aluno(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    tel = models.CharField(max_length=150, verbose_name='Fone')

    def __str__(self):
        return self.nome


class AlunoAtividade(models.Model):
    aluno = models.ForeignKey('Aluno', verbose_name='Aluno', on_delete=models.PROTECT, related_name='atividades',)
    descricao = models.CharField(max_length=150, verbose_name='Tipo atividade:')

    def __str__(self):
        return self.aluno.nome + ' - ' + self.descricao


class Disciplina(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    aluno = models.ForeignKey('Aluno', verbose_name='Aluno',
                              blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

