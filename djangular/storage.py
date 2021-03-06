from django.contrib.staticfiles.storage import AppStaticStorage
import os
from re import sub

class AngularAppStorage(AppStaticStorage):
    source_dir = 'app'

    def __init__(self, app, *args, **kwargs):
        # app is the actual app module
        print "----------------------------->", app
        self.prefix = os.path.join(*(app.split('.')))
        super(AngularAppStorage, self).__init__(app, *args, **kwargs)

    def path(self, name):

    	print "---------------->", name

        name = sub('^' + self.prefix + os.sep, '', name)
        return super(AngularAppStorage, self).path(name)