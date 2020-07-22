from rest_framework import serializers

from escola.models import Disciplina, Aluno, AlunoAtividade


class DisciplinaSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)

    class Meta:
        model = Disciplina
        fields = ('id', 'nome')


class AlunoAtividadeSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)

    class Meta:
        model = AlunoAtividade
        """aluno ficou de fora, pois vai ser inserido a posteriori"""
        fields = ('id', 'descricao')


class AlunoSerializer(serializers.ModelSerializer):

    """aluno-atividade aqui é similar a um inline. O nome desse campo 'atividades' é o mesmo nome do 'related_name'
        que está no Model AlunoAtividade, no campo 'aluno'. Isso é para que o rest faça o relacionamento reverso,
        do Aluno para alunoatividade, mesmo aluno não possuindo fk para alunoatividade, ele busca reversamente. """
    atividades = AlunoAtividadeSerializer(many=True, read_only=False)

    class Meta:
        model = Aluno
        fields = ('id', 'nome', 'tel', 'atividades')

    """ Criar metodo que simula formset com o cadastro de aluno """
    def create(self, validated_data):

        atividades = validated_data['atividades']
        del validated_data['atividades']

        aluno = Aluno.objects.create(**validated_data)

        for atividade in atividades:
            AlunoAtividade.objects.create(**atividade, aluno=aluno)

        return aluno

    """ Método que atualiza o aluno, e suas atividades.
        Atualiza, quando tem o id, quando não, cria uma nova atividade para aquele aluno."""
    def update(self, instance, validated_data):

        atividades = validated_data['atividades']
        del validated_data['atividades']

        instance = super().update(instance, validated_data)

        # formset de aluno-atividade:
        for atividade in atividades:
            atividade_id = atividade.get('id', None)

            if atividade_id:
                atividade_upd = AlunoAtividade.objects.get(id=atividade_id)
                atividade_upd.descricao = atividade.get('descricao', atividade_upd.descricao)
                atividade_upd.save()
            else:
                new_atividade = AlunoAtividade.objects.create(**atividade, aluno=instance)

        return instance
