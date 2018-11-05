from problems.models import Problem
from problems.serializers import ProblemSerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView


class ProblemList(ListAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


class ProblemDetail(RetrieveAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
