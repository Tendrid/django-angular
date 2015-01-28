from django.contrib.staticfiles import finders
from storage import * 

class AngularAppFinder(finders.AppDirectoriesFinder):
   storage_class = AngularAppStorage
