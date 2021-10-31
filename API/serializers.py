from rest_framework import serializers
from API.models import Projects,Votes

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = [
            "pk","title","image","description","project_link","date_added"
        ]

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "pk","design","ussability","content"
        ]