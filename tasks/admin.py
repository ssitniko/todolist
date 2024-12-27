from django.contrib import admin
from tasks.models import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category')
    list_filter = ('category',)
    search_fields = ('title',) 
    



# admin.site.register(Task)
# admin.site.register(Category)



