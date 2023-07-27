from django.contrib import admin
from .models import *

admin.site.register(short_link)
admin.site.register(full_link)
#admin.site.register(s_l)

admin.site.site_header = 'URL Shortener App'
