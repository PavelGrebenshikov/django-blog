from django.test import TestCase
from .models import Posts
from django.utils import timezone

# Create your tests here.


class PostsModelTest(TestCase):
    result = Posts(author='Test')

    self.assertIs(result, True)