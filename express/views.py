from django.shortcuts import render
from django.views.generic import View
from express.models import *
from django.http import HttpResponse
import json

class Reserve(View):
    def get(self, request):
        grades = Grade.objects.all()
        return render(request, 'express/reserve.html', {"grades": grades})

    def post(self, request):
        grade = request.POST.get("grade", "")
        name = request.POST.get("name", "")
        address = request.POST.get("address", "")
        phone = request.POST.get("phone", "")
        if grade and name and address and phone:
            Student.objects.create(grade_id=int(grade), name=name, address=address, phone=phone)
            return HttpResponse(json.dumps({"status": 1}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"status": 2}), content_type="application/json")
