from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Todo
from rest_framework.renderers import JSONRenderer

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(max_length=25)
    date = serializers.DateTimeField()
    finished = serializers.BooleanField()
    def create(self, validated_data):
        return Todo(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.email)
        instance.date = validated_data.get('date', instance.content)
        instance.finished = validated_data.get('finished', instance.created)
        instance.save()
        return instance
    class Meta:
        model = Todo
        fields = ('name', 'date', 'finished')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
