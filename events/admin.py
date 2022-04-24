from django.contrib import admin


from .models import Event
from .models import MyClubUser
from .models import Venue

admin.site.register(Event)
admin.site.register(MyClubUser)
admin.site.register(Venue)
