from django.test import TestCase
from .models import Todo

# Create your tests here.

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="Test title", body="test body")

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        title = f'{todo.title}'
        self.assertEqual(title, 'Test title')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        body = f'{todo.body}'
        self.assertEqual(body, 'test body')