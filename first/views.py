from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from first.models import *
import json


def trans_phone():
    pass

class Questionnaire(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(Questionnaire, self).dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, 'questionnaire.html')

    def post(self, request):
        username = request.POST.get("username")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        nick = request.POST.get("nick")
        count = request.POST.get("count")
        Question.objects.create(
            username=username,
            phone=phone,
            address=address,
            nick=nick,
            count=count,
        )
        res = json.dumps({"status": "1"})
        return HttpResponse(res, content_type="application/json")


class clickMap(View):
    def get(self, request):
        return render(request, 'click_map.html')


class drawAward(View):
    def get(self, request):
        return render(request, 'DrawAward.html')


class search(View):
    def get(self, request):
        return render(request, 'search.html')

    def post(self, request):
        code = request.POST.get("code", "")
        result = {}
        if code=="LT007":
            result = {
                "status": 1,
                "name": "可乐一瓶",
                "use": "未使用"
            }
        else:
            result = {
                "status": 0
            }
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json")
