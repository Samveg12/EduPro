from django.contrib import admin
from .models import Belongs,Education,otherDetails,myBookedSlots,Review,FixTimings

admin.site.register(Belongs)
admin.site.register(Review)

admin.site.register(Education)
admin.site.register(myBookedSlots)

admin.site.register(otherDetails)
admin.site.register(FixTimings)



