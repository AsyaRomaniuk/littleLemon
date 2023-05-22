from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup():
        print("Tested")
    
    def test_getall():
        Menu.objects.get()