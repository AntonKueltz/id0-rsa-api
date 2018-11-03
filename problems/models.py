from forum.models import Thread

from django.db import models
from django.db.models.signals import post_save
from enumfields import Enum, EnumField


class Difficulty(Enum):
    NOVICE = 'Very Easy'
    EASY = 'Easy'
    MODERATE = 'Moderate'
    HARD = 'Hard'
    EXPERT = 'Very Hard'


class Problem(models.Model):
    """represents a single coding problem"""
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = EnumField(Difficulty, default=Difficulty.MODERATE)
    solution = models.CharField(max_length=255)

    problem_thread = models.OneToOneField(
        Thread,
        related_name='problem',
        on_delete=models.SET_NULL,
        null=True
    )
    solution_thread = models.OneToOneField(
        Thread,
        related_name='solved_problem',
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)


def create_problem_threads(sender, instance, created, **kwargs):
    if created:
        # create the discussion thread
        Thread.objects.create(
            title=instance.title,
            problem=instance,
            restricted=False
        )
        # create the solution thread
        Thread.objects.create(
            title=instance.title,
            solved_problem=instance,
            restricted=True
        )


post_save.connect(create_problem_threads, sender=Problem)
