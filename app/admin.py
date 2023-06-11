from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(Year)
admin.site.register(Course)
admin.site.register(Qualification)
admin.site.register(StudentData)
admin.site.register(Coding)
admin.site.register(Theory)
admin.site.register(Comunication)
admin.site.register(StudentRating)

