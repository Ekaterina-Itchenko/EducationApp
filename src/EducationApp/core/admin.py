from django.contrib import admin
from core.models import Lesson, Product, Group, AvailableProduct, GroupMember


class MembersInline(admin.TabularInline):
    model = GroupMember
    extra = 3


class PupilesInline(admin.TabularInline):
    model = AvailableProduct
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "author",
        "min_pupiles",
        "max_pupiles",
        "start_date",
        "price",
    ]
    list_display_links = ["id", "name"]
    list_editable = ["min_pupiles", "max_pupiles"]
    inlines = (PupilesInline,)
    list_per_page = 10


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "product",
    ]
    list_display_links = ["id", "name"]
    inlines = (MembersInline,)
    list_per_page = 10


class LessonAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "product",
        "video_link",
    ]
    list_display_links = ["id", "name"]
    list_per_page = 10


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Product, ProductAdmin)
