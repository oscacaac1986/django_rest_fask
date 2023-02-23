from rest_framework import serializers

from .models import project


class ProjectSerialiser(serializers.ModelSerializer):
    class Meta:
        model=project
        fields=('id','title','description','technology','create_at')
        read_only_fields=('create_at',)