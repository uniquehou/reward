from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from first.models import *
from random import choice, sample, random, uniform
import json
import string


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
        awards = ClickMapAreaAward.objects.filter(area_id=int(id))
        award = self.random_pick(awards)
        if award:
            code = ClickMapAwardCode()
            code.award = award
            code.code = self.getCode()
            code.use = '1'
            code.save()
            res = {
                "status": 1,
                "award": award.name,
                "code": code.code,
            }
        else:
            res = {
                "status": 0
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

    def getAward(self, awards):
        num = random()
        for award in awards:
           if num<=award.rate and award.award.count>0:
                return award.award
        return None

    def random_pick(self, awards):
        x = random()
        print(x)
        cumulative_probability = 0.0
        for item, item_probability in zip([award.award for award in awards], [award.rate for award in awards]):
            cumulative_probability += item_probability
            if x <= cumulative_probability:
                return item
        return None