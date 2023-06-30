from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import *


class UserModel(UserAdmin):
    list_display = ['username', 'user_type']


admin.site.register(CustomUser, UserModel)
admin.site.register(Home)
admin.site.register(Know_about_us)
admin.site.register(Images)
admin.site.register(Website_team)
admin.site.register(Home_Video)
admin.site.register(Home_seasons)
admin.site.register(Home_seasons_step)
admin.site.register(Big_about)
admin.site.register(Admin_mine)
admin.site.register(Tournament_Lucky)
