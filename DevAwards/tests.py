from django.test import TestCase
from .models import *
import datetime as dt

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.mo= Profile(user= 'mo', bio ='hello')

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.mo,Profile))

        # Testing Save Method Profile
    def test_save_method(self):
        self.mo.profile()
        users = Profile.objects.all()
        self.assertTrue(len(users) > 0)

class ProjectTestClass(TestCase):

    def setUp(self):
        # Creating a new Project
        self.foodie= Project(caption = 'foodie',pic="logo.png")

    def test_instance(self):
        self.assertTrue(isinstance(self.greece,Project))

    def test_save_method(self):
        self.foodie.post()
        posts = Project.objects.all()
        self.assertTrue(len(posts) > 0)




