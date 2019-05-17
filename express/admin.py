import xadmin
from .models import *

class StudentAdmin(object):
    list_display = ('grade', 'name', 'address', 'phone')
    list_filter = ('grade', )

class GradeAdmin(object):
    list_display = ('name', )


xadmin.site.register(Student, StudentAdmin)
xadmin.site.register(Grade, GradeAdmin)
