from django.contrib import admin

# Register your models here.
from .models import Profile
admin.site.register(Profile)

from .models import Member
admin.site.register(Member)

from .models import Dashboardview
admin.site.register(Dashboardview)