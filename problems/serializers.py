from problems.models import Problem

from drf_enum_field.serializers import EnumFieldSerializerMixin
from rest_framework.serializers import ModelSerializer


class ProblemSerializer(EnumFieldSerializerMixin, ModelSerializer):
    class Meta:
        model = Problem
        fields = ('id', 'title', 'summary', 'description', 'difficulty', 'solved')


class ProblemSummarySerializer(EnumFieldSerializerMixin, ModelSerializer):
    class Meta:
        model = Problem
        fields = ('id', 'title', 'summary', 'difficulty', 'solved')