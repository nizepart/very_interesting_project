from django.test import TestCase

# Create your tests here.

from places_remember.forms import MemoryForm



class MemoryFormTest(TestCase):

    def test_UserForm_valid(self):
        form = MemoryForm(data={'title':'Название места', 'task':'Это комментарий','location_0':'ITMO University, Кронверкский проспект, Санкт-Петербург, Россия', 'location_1':'59.95717999999999', 'location_2':'30.3083389'})
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid(self):
        form = MemoryForm(data={'title':'', 'task':'','location_0':'', 'location_1':'', 'location_2':''})
        self.assertFalse(form.is_valid())