from forum.models import Thread

from django.test import TestCase


class ThreadTestCase(TestCase):
    def test_auto_thread_creation(self):
        from problems.models import Problem

        p = Problem.objects.create(
            title='', summary='', description='', solution='')

        self.assertEqual(Thread.objects.count(), 2)

        self.assertNotEqual(p.problem_thread, None)
        self.assertFalse(p.problem_thread.restricted)
        self.assertEqual(p.problem_thread.title, p.title)

        self.assertNotEqual(p.solution_thread, None)
        self.assertTrue(p.solution_thread.restricted)
        self.assertEqual(p.solution_thread.title, p.title)
