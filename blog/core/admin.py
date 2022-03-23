from django.contrib import admin
from .models import Profile, Post, User,Work_site, Skill_set, UserRole


admin.site.register(Profile)


class PostAdmin(admin.ModelAdmin):  # keiciam post contenta
    list_filter = ['post_label', 'post_date', 'name']
    list_per_page = 2
    list_display = ['post_label', 'title', 'post_msg']
    list_display_links = ['title', 'post_label', 'post_msg']  # <a href='http://127.0.0.1:8000/admin/core/post/11/change/?_changelist_filters=all%3D%26o%3D2'> i objecta
    ordering = ['post_msg']


admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(Work_site)
admin.site.register(Skill_set)
admin.site.register(UserRole)
