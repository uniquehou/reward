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
    list_display = ('name', 'note', 'count')

class ClickMapAreaAwareAdmin(object):
    list_display = ('area', 'award', 'rate')
    list_filter = ('area', )

class ClickMapAwareCodeAdmin(object):
    list_display = ('award', 'code', 'use')
    list_filter = ('award', )

class LockCodeAdmin(object):
    list_display = ('code', )

# xadmin.site.register(Question, QuestionAdmin)
xadmin.site.register(ClickMap, ClickMapAdmin)
xadmin.site.register(ClickMapArea, ClickMapAreaAdmin)
xadmin.site.register(ClickMapAward, ClickMapAwareAdmin)
xadmin.site.register(ClickMapAreaAward, ClickMapAreaAwareAdmin)
xadmin.site.register(ClickMapAwardCode, ClickMapAwareCodeAdmin)
xadmin.site.register(LockCode, LockCodeAdmin)