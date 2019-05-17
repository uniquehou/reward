from django.db import models

class Grade(models.Model):
    name = models.CharField(u'班级名', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'


class Student(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, verbose_name='班级', default=0, null=True)
    name = models.CharField(u'姓名', max_length=30, default=' ')
    address = models.CharField(u'宿舍号', max_length=20)
    phone = models.CharField(u'联系方式', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '毕业生'
        verbose_name_plural = '毕业生'