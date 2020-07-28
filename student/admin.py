from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)

admin.site.register(Cschool)

class LeasonAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'product','cr_date')
    list_filter = ("title",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Leason, LeasonAdmin)


admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Faq)
admin.site.register(Customize)