from django.test import TestCase
from resturant.models import Menu


class MenuItemTest(TestCase):
  def test_get_item(self):
    m1 = Menu.objects.create(Title='title', Price=20.21,Inventory= 10)
    self.assertEqual(str(m1), "title : 20.21")


