from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from first.models import *
from random import choice, sample
import json
import string


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
        awardCode = ClickMapAwardCode.objects.filter(code=code).first()
        result = {}
        if awardCode:
            result['status'] = int(awardCode.use)
            result['codeid'] = awardCode.id
            result['name'] = awardCode.award.name
            result['use'] = awardCode.get_use_display()
        else:
            result['status'] = 0
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json")


def codeExchange(request):
    codeId = request.POST.get("codeId", "")
    code = ClickMapAwardCode.objects.get(id=int(codeId))
    code.use = '2'
    code.save()
    return HttpResponse(json.dumps({"status": 1}), content_type="application/json")


def meng(request):
    return render(request, 'meng.html')


class onClickMap(View):
    def get(self, request):
        id = request.GET.get("imgid", "")
        img = ClickMap.objects.filter(id=int(id)).first()
        maps = img.clickmaparea_set.all()
        res = {
            'img': img,
            'maps': maps,
        }
        return render(request, 'clickmap.html', res)

    def post(self, request):
        id = request.POST.get("areaid", "")
        awards = ClickMapAward.objects.filter(area_id=int(id))
        award = choice(awards)
        code = ClickMapAwardCode()
        code.award = award
        code.code = self.getCode()
        code.use = '1'
        code.save()
        res = {
            "award": award.name,
            "code": code.code,
        }
        return HttpResponse(json.dumps(res), content_type="application/json")

    def getCode(self):
        pre = "LT"
        code = ""
        field = string.ascii_letters + string.digits
        while True:
            code = ''.join(sample(field, 6))
            if not ClickMapAwardCode.objects.filter(code=pre+code).first():
                break
        return pre+code