from django.contrib import admin

from .models import Inbox, Like, Post, UserProfile, Comment, User



class PostAdmin(admin.ModelAdmin):
    model = Post
    exclude = ('author',)
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Inbox)