from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from models import Category, Page
from models import UserProfile

class CategoryAdmin(admin.ModelAdmin):
		prepopulated_fields = {'slug':('name',)}

class PageAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass
		
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
# Register your models here.



