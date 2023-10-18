from django.contrib import admin
from django.urls import path
from .models import Task
from django.http import HttpResponseRedirect
from django.utils.html import format_html
admin.site.site_header = "Babat mord admin"

class Koskesh(admin.ModelAdmin):
    list_display = ("title", "created_at", "font_size_html_display")
    list_filter = ("created_at",)
    change_list_template = "admin/snippets/snippets_change_list.html"
    
    def get_urls(self):
        urls =  super().get_urls()
        custom_urls = [path("fontsize/<int:size>/", self.babat)]
    
        return custom_urls + urls
    def babat(self,req,size):
        self.model.objects.all().update(font_size = size)
        self.message_user(req,message="ok shod")
        return HttpResponseRedirect("../")
    
    def font_size_html_display(self, obj):
        return format_html(f"<span style = 'font-size:{obj.font_size}px;'>{obj.font_size}</span>")
    font_size_html_display.short_description = "font size"
admin.site.register(Task, Koskesh)
