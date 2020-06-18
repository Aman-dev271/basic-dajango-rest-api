from Apiaap.models import student
from rest_framework import serializers
class studentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = student
        fields = "__all__"

    