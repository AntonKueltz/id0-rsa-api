from urllib.parse import unquote

from problems.models import Problem
from problems.serializers import ProblemSerializer, ProblemSummarySerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


class ProblemList(ListAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSummarySerializer


class ProblemDetail(RetrieveAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


class CheckAnswer(APIView):
    def get(self, request, pk):
        problem = Problem.objects.get(pk=pk)
        answer = request.query_params.get('answer')

        correct = (problem.solution == unquote(answer))
        return Response({'correct': correct})
