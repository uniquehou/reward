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