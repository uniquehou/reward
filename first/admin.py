from first.models import *
import xadmin

class QuestionAdmin(object):
    list_display = ('username', 'phone', 'address', 'nick', 'count')
    search_fields = ('username', )
    list_filter = ('nick', )


class ClickMapAdmin(object):
    list_display = ('name', 'id', 'url', 'note' )

class ClickMapAreaAdmin(object):
    list_display = ('img', 'name', 'area')
    list_filter = ('img', )

class ClickMapAwareAdmin(object):
    list_display = ('area', 'name', 'rate')
    list_filter = ('area', )

class ClickMapAwareCodeAdmin(object):
    list_display = ('award', 'code', 'use')
    list_filter = ('award', )

# xadmin.site.register(Question, QuestionAdmin)
xadmin.site.register(ClickMap, ClickMapAdmin)
xadmin.site.register(ClickMapArea, ClickMapAreaAdmin)
xadmin.site.register(ClickMapAward, ClickMapAwareAdmin)
xadmin.site.register(ClickMapAwardCode, ClickMapAwareCodeAdmin)
