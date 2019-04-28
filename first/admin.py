from first.models import *
import xadmin

class QuestionAdmin(object):
    list_display = ('username', 'phone', 'address', 'nick', 'count')
    search_fields = ('username', )
    list_filter = ('nick', )

xadmin.site.register(Question, QuestionAdmin)