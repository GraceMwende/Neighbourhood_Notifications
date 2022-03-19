from django.test import TestCase
from .models import Neighbourhood,Users,Business,Profile

# Create your tests here.
class NeighbourhoodTest(TestCase):
  # setup method
  def setUp(self):
    self.kibra = Neighbourhood(neighbourhood_name='Kibra',neighbourhood_location='Kibra',occupants_count=2)

  #Testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.kibra,Neighbourhood)) 

  #Testing saving method 
  def test_save_method(self):
    self.kibra.save_neighbourhood()
    neighourhoods = Neighbourhood.objects.all()
    self.assertTrue(len(neighourhoods)>0)

   # Test delete method
  def test_delete_method(self):
    self.kibra.save_neighbourhood()
    self.kibra.delete_neighbourhood()
    neighourhoods = Neighbourhood.objects.all()
    self.assertTrue(len(neighourhoods)==0)

  # test display neighourhoods
  def test_display_neighbourhoods(self):
    self.kibra.save_neighbourhood()
    neighbourhood = Neighbourhood.display_neighbourhhoods()
    self.assertTrue(len(neighbourhood)>0)