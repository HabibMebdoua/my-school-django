from django import template

register = template.Library()

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
