from rest_framework import generics
from API.models import Projects,Votes
from API.serializers import ProjectSerializer,VoteSerializer

class ProjectsList(generics.CreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer 

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer 

class VoteList(generics.CreateAPIView):
    queryset = Votes.objects.all()
    serializer_class = VoteSerializer

class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Votes.objects.all()
    serializer_class = VoteSerializer

