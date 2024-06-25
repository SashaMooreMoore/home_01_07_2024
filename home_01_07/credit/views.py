from django.shortcuts import render
from django.views import View
from .models import Info
from django.db.models import F

class Credit(View):
    def get(self, request):
        objects_credit = Info.objects.annotate(
            payment = F('credit')*(F('percent')+(F('percent')/(1+F('percent'))*F('duration')-1))
            # payment = (F('credit')*F('percent')*((F('duration')*30)/365))/100
            # payment = F('credit')*F('percent')/100/F('duration')*30
            # payment = F('credit')*F('percent')/100/365*30
        )
        return render(request, 'credit/index.html', {
            'credits': objects_credit
        })
