from django.db import models
from django.utils import timezone

class Department(models.Model):
    name = models.CharField(u'院系名', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '院系'
        verbose_name_plural = '院系'


class Grade(models.Model):
    name = models.CharField(u'班级名', max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, verbose_name="所属院系", default=0, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'


class Dormitory(models.Model):
    name = models.CharField("宿舍号", max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '宿舍'
        verbose_name_plural = '宿舍'


class Student(models.Model):
    ctimeChoice = (
        ('0', '全天'),
        ('1', '上午'),
        ('2', '下午')
    )
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, verbose_name='班级', default=0, null=True)
    name = models.CharField(u'姓名', max_length=30, default=' ')
    dormitory = models.ForeignKey(Dormitory, verbose_name='宿舍号', on_delete=models.SET_NULL, default=0, null=True)
    address = models.CharField(u'地址', max_length=20)
    phone = models.CharField(u'联系方式', max_length=10)
    date = models.DateField(u'预定日期', default=timezone.now())
    ctime = models.CharField(u'时间', max_length=3, choices=ctimeChoice, default='1')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '毕业生'
        verbose_name_plural = '毕业生'