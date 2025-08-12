from django.contrib import admin
from .models import StickyNote


@admin.register(StickyNote)
class StickyNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'pinned', 'due_date', 'updated_at')
    list_filter = ('pinned', 'due_date')
    search_fields = ('title', 'content')
