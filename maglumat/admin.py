from django.contrib import admin
from .models import*
# {'uniw':'uniw'}

admin.site.register(bash_video)
admin.site.register(yurtlar)
admin.site.register(Teswir)
admin.site.register(register)
admin.site.register(news)


class SearchUni(admin.ModelAdmin):
    search_fields=['at_tm']

    class Meta:
        model=uniwersitetler

admin.site.register(uniwersitetler,SearchUni)