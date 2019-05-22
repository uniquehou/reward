import xadmin
from .models import *
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class StuDepart(admin.SimpleListFilter):
    title = _("院系")

    parameter_name = "department"

    def lookups(self, request, model_admin):
        departments = Department.objects.all()
        res = []
        for d in departments:
            tmp = (str(d.id), _(d.name))
            res.append(tmp)
        return res

    def queryset(self, request, queryset):
        department = Department.objects.get(id=int(self.value()))
        return queryset.filter(grade__department=department)




class StudentAdmin(object):
    list_display = ('name', 'dormitory', 'phone', 'date', 'ctime')
    list_filter = ('dormitory', 'date', 'ctime')

class GradeAdmin(object):
    list_display = ('name', 'department')
    list_filter = ('department', )
    search_fields = ('name', )

class DepartmentAdmin(object):
    list_display = ('name', )
    ordering = ('id', )

class DormitoryAdmin(object):
    list_display = ('name', )
    ordering = ('id', )


xadmin.site.register(Student, StudentAdmin)
xadmin.site.register(Dormitory, DormitoryAdmin)
# xadmin.site.register(Grade, GradeAdmin)
# xadmin.site.register(Department, DepartmentAdmin)