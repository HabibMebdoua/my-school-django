from django.contrib import admin
from django.utils.html import format_html
from django.utils.html import mark_safe
from .models import Lesson, Exam, Tip


# تخصيص موقع الإدارة الرئيسي
admin.site.site_header = mark_safe(
    '<span style="color: white; font-weight: bold;">📚 My School</span>'
)
admin.site.site_title = "My School Admin"
admin.site.index_title = "Welcome to My School Admin Panel"

# إضافة CSS مخصص
class AdminMediaMixin:
    class Media:
        css = {'all': ('css/admin.css',)}


@admin.register(Lesson)
class LessonAdmin(AdminMediaMixin, admin.ModelAdmin):
    list_display = ('colored_title', 'colored_subject', 'colored_year', 'created_at')
    list_filter = ('subject', 'academic_year', 'created_at')
    search_fields = ('title', 'subject')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('title', 'subject', 'academic_year')
        }),
        ('الملفات', {
            'fields': ('pdf_file',)
        }),
        ('التواريخ', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    def colored_title(self, obj):
        return format_html(
            '<span style="color: #007bff; font-weight: bold;">📖 {}</span>',
            obj.title
        )
    colored_title.short_description = 'عنوان الدرس'
    
    def colored_subject(self, obj):
        colors = {
            'math': '#ff6b6b',
            'arabic': '#4ecdc4',
            'french': '#45b7d1',
            'english': '#96ceb4',
            'nature': '#6bcf7f',
            'physics': '#ffa502',
            'social': '#9b59b6',
            'islamic': '#e74c3c',
        }
        color = colors.get(obj.subject, '#007bff')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold;">{}</span>',
            color,
            obj.get_subject_display()
        )
    colored_subject.short_description = 'المادة'
    
    def colored_year(self, obj):
        colors = {
            'year1': '#007bff',
            'year2': '#28a745',
            'year3': '#ffc107',
            'year4': '#dc3545',
        }
        color = colors.get(obj.academic_year, '#6c757d')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold;">{}</span>',
            color,
            obj.get_academic_year_display()
        )
    colored_year.short_description = 'السنة الدراسية'


@admin.register(Exam)
class ExamAdmin(AdminMediaMixin, admin.ModelAdmin):
    list_display = ('colored_title', 'exam_type_badge', 'colored_subject', 'colored_year', 'correction_badge', 'created_at')
    list_filter = ('exam_type', 'subject', 'academic_year', 'correction_status', 'created_at')
    search_fields = ('title', 'subject')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('title', 'subject', 'exam_type', 'academic_year')
        }),
        ('حالة التصحيح', {
            'fields': ('correction_status',)
        }),
        ('الملفات', {
            'fields': ('exam_file', 'correction_file')
        }),
        ('التواريخ', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    def colored_title(self, obj):
        return format_html(
            '<span style="color: #28a745; font-weight: bold;">✏️ {}</span>',
            obj.title
        )
    colored_title.short_description = 'عنوان الاختبار'
    
    def exam_type_badge(self, obj):
        if obj.exam_type == 'exam':
            return format_html(
                '<span style="background-color: #17a2b8; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold;">📝 اختبار</span>'
            )
        else:
            return format_html(
                '<span style="background-color: #ffc107; color: black; padding: 4px 8px; border-radius: 4px; font-weight: bold;">📄 فرض</span>'
            )
    exam_type_badge.short_description = 'نوع الاختبار'
    
    def colored_subject(self, obj):
        colors = {
            'math': '#ff6b6b',
            'arabic': '#4ecdc4',
            'french': '#45b7d1',
            'english': '#96ceb4',
            'nature': '#6bcf7f',
            'physics': '#ffa502',
            'social': '#9b59b6',
            'islamic': '#e74c3c',
        }
        color = colors.get(obj.subject, '#007bff')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold;">{}</span>',
            color,
            obj.get_subject_display()
        )
    colored_subject.short_description = 'المادة'
    
    def colored_year(self, obj):
        colors = {
            'year1': '#007bff',
            'year2': '#28a745',
            'year3': '#ffc107',
            'year4': '#dc3545',
        }
        color = colors.get(obj.academic_year, '#6c757d')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold;">{}</span>',
            color,
            obj.get_academic_year_display()
        )
    colored_year.short_description = 'السنة الدراسية'
    
    def correction_badge(self, obj):
        if obj.correction_status == 'available':
            return format_html(
                '<span style="background-color: #28a745; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold;">✓ متاح</span>'
            )
        else:
            return format_html(
                '<span style="background-color: #dc3545; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold;">✗ غير متاح</span>'
            )
    correction_badge.short_description = 'حالة التصحيح'


@admin.register(Tip)
class TipAdmin(AdminMediaMixin, admin.ModelAdmin):
    list_display = ('colored_title', 'colored_subject', 'colored_year', 'content_preview', 'created_at')
    list_filter = ('subject', 'academic_year', 'created_at')
    search_fields = ('title', 'subject', 'content')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('title', 'subject', 'academic_year')
        }),
        ('المحتوى', {
            'fields': ('content',)
        }),
        ('التواريخ', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    def colored_title(self, obj):
        return format_html(
            '<span style="color: #ffc107; font-weight: bold;">💡 {}</span>',
            obj.title
        )
    colored_title.short_description = 'عنوان النصيحة'
    
    def colored_subject(self, obj):
        colors = {
            'math': '#ff6b6b',
            'arabic': '#4ecdc4',
            'french': '#45b7d1',
            'english': '#96ceb4',
            'nature': '#6bcf7f',
            'physics': '#ffa502',
            'social': '#9b59b6',
            'islamic': '#e74c3c',
        }
        color = colors.get(obj.subject, '#007bff')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold;">{}</span>',
            color,
            obj.get_subject_display()
        )
    colored_subject.short_description = 'المادة'
    
    def colored_year(self, obj):
        colors = {
            'year1': '#007bff',
            'year2': '#28a745',
            'year3': '#ffc107',
            'year4': '#dc3545',
        }
        color = colors.get(obj.academic_year, '#6c757d')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold;">{}</span>',
            color,
            obj.get_academic_year_display()
        )
    colored_year.short_description = 'السنة الدراسية'
    
    def content_preview(self, obj):
        preview = obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
        return format_html(
            '<span style="color: #6c757d; font-style: italic;">{}</span>',
            preview
        )
    content_preview.short_description = 'معاينة المحتوى'


