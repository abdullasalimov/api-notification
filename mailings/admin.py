from django.contrib import admin

from .models import Contact, Mailing, Message

admin.site.site_title = "API Уведомления"
admin.site.site_header = 'API Администрирование'
admin.site.index_title = "Админ панель"


admin.site.register(Contact)
admin.site.register(Mailing)
admin.site.register(Message)
