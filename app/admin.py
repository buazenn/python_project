from django.contrib import admin
from .models import PersonalData, WorkedTime, WorkedList, Statistic, NewsModel, Contribution, RetirementValue

admin.site.register(WorkedList)
admin.site.register(PersonalData)
admin.site.register(WorkedTime)
admin.site.register(Statistic)
admin.site.register(NewsModel)
admin.site.register(Contribution)
admin.site.register(RetirementValue)
