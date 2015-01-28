from django.contrib.staticfiles.storage import AppStaticStorage
import os

class AngularAppStorage(AppStaticStorage):
   source_dir = 'app'

   def __init__(self, app, *args, **kwargs):
       # app is the actual app module
       self.prefix = os.path.join(*(app.split('.')))
       super(MyAngularAppStorage, self).__init__(app, *args, **kwargs)

   def path(self, name):
       name = sub('^' + self.prefix + os.sep, '', name)
       return super(MyAngularAppStorage, self).path(name)