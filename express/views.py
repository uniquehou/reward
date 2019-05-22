from django.shortcuts import render
from django.views.generic import View
from express.models import *
from django.http import HttpResponse
import json
import datetime

class Reserve(View):
    def get(self, request):
        dors = Dormitory.objects.all()
        return render(request, 'express/reserve.html', {"dors": dors})

    def post(self, request):
        dormitory = request.POST.get("dormitory", "")
        name = request.POST.get("name", "")
        ctime = request.POST.get("ctime", "")
        phone = request.POST.get("phone", "")
        date = request.POST.get("date", "")
        if dormitory and name and ctime and phone:
            date = list(map(int, date.split('-')))
            Student.objects.create(dormitory_id=int(dormitory), name=name, ctime=ctime, phone=phone, date=datetime.date(*date))
            return HttpResponse(json.dumps({"status": 1}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"status": 2}), content_type="application/json")
