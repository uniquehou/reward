from django.db import models

class Question(models.Model):
    username = models.CharField(u"姓名", blank=True, default="", max_length=50)
    phone = models.CharField(u"手机号", blank=True, default="", max_length=50)
    address = models.CharField(u"地址", blank=True, default="", max_length=50)
    nick = models.CharField(u"称号", blank=True, default="", max_length=50)
    count = models.CharField(u"获奖数", blank=True, default="", max_length=50)

    def __str__(self):
        return "{}-{}".format(self.username, self.nick)

    class Meta:
        verbose_name = "答题抽奖"
        verbose_name_plural = '答题抽奖'


class ClickMap(models.Model):
    name = models.CharField(u'名称', max_length=100, default='', blank=True)
    img = models.FileField(u'抽奖图片', upload_to='clickmap', blank=True)
    url = models.CharField(u'抽奖链接', max_length=50, blank=True)
    note = models.CharField(u'二次未中提示语', max_length=100, blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "抽奖图片"
        verbose_name_plural = '抽奖图片'

class ClickMapArea(models.Model):
    img = models.ForeignKey(ClickMap, verbose_name=u'图片', on_delete=models.CASCADE)
    name = models.CharField(u'区域名', max_length=50)
    area = models.CharField(u'抽奖区域', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "奖品区域"
        verbose_name_plural = '奖品区域'


class ClickMapAward(models.Model):
    area = models.ForeignKey(ClickMapArea, verbose_name='绑定区域', on_delete=models.CASCADE)
    name = models.CharField("奖品名", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "奖品"
        verbose_name_plural = '奖品'


class ClickMapAwardCode(models.Model):
    useChoice = (
        ('1', '未使用'),
        ('2', '已使用')
    )

    award = models.ForeignKey(ClickMapAward, verbose_name="奖品", on_delete=models.CASCADE)
    code = models.CharField("兑奖码", max_length=20)     # LTxxxxx
    use = models.CharField("使用情况", max_length=2, choices=useChoice, default='1')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "兑奖码"
        verbose_name_plural = '兑奖码'
