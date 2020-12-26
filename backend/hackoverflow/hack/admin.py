from django.contrib import admin

# Register your models here.
from .models import userData,Hackathon,Group,GroupMember,Team,TeamMember,Messages

admin.site.register(userData)
admin.site.register(Hackathon)
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Messages)