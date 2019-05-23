from django.test import TestCase
from MyBlog.models import Category,Article

class BlogTest(TestCase):
    def getCat(self):
        listCat = Category.objects.all()
        print(listCat)
