from django.test import TestCase

# Create your tests here.
from places_remember.models import Memory
from django.contrib.auth.models import User

class MemoryModeltest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='user', email='123@mail.ru')
        Memory.objects.create(title='Название места', task='Это комментарий', author=user, location='1')

    def test_title_label(self):
        memory = Memory.objects.get(id=1)
        field_label = memory._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название')

    def test_task_label(self):
        memory = Memory.objects.get(id=1)
        field_label = memory._meta.get_field('task').verbose_name
        self.assertEquals(field_label, 'Комментарий')

    def test_task_location(self):
        memory = Memory.objects.get(id=1)
        field_label = memory._meta.get_field('location').verbose_name
        self.assertEquals(field_label, 'Место на карте')

    def test_title_max_length(self):
        memory = Memory.objects.get(id=1)
        max_length = memory._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)

    def test_object_name(self):
        memory = Memory.objects.get(id=1)
        expected_object_name = memory.title
        self.assertEquals(expected_object_name, str(memory))

