from django import template

register = template.Library()

# قاموس الأيقونات والألوان للمواد
SUBJECT_ICONS = {
    'الرياضيات': {'icon': 'fa-calculator', 'color': '#ff6b6b'},
    'اللغة العربية': {'icon': 'fa-book', 'color': '#4ecdc4'},
    'اللغة الفرنسية': {'icon': 'fa-globe', 'color': '#45b7d1'},
    'اللغة الانجليزية': {'icon': 'fa-language', 'color': '#96ceb4'},
    'علوم الطبيعة والحياة': {'icon': 'fa-leaf', 'color': '#6bcf7f'},
    'الفيزياء': {'icon': 'fa-flask', 'color': '#ffa502'},
    'الإجتماعيات': {'icon': 'fa-globe-americas', 'color': '#9b59b6'},
    'التربية الإسلامية': {'icon': 'fa-book-quran', 'color': '#e74c3c'},
    'الإعلام الآلي': {'icon': 'fa-computer', 'color': '#3498db'},
}

@register.filter
def subject_icon(subject):
    """إرجاع فئة الأيقونة فقط"""
    if subject in SUBJECT_ICONS:
        return SUBJECT_ICONS[subject]['icon']
    return ''

@register.filter
def subject_color(subject):
    """إرجاع لون المادة الدراسية"""
    if subject in SUBJECT_ICONS:
        return SUBJECT_ICONS[subject]['color']
    return '#000000'

@register.filter
def add_three(value, arg1, arg2):
    """إضافة ثلاث قيم معاً"""
    try:
        return int(value) + int(arg1) + int(arg2)
    except (ValueError, TypeError):
        return 0


@register.filter
def total_items(lessons, exams, tests):
    """حساب إجمالي الدروس والاختبارات والفروض"""
    try:
        return int(lessons) + int(exams) + int(tests)
    except (ValueError, TypeError):
        return 0
