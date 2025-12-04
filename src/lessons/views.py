from django.shortcuts import render
from django.db.models import Count, Q
from .models import Lesson, Exam, Tip, ACADEMIC_YEAR_CHOICES


def all_years_view(request):
    """عرض جميع السنوات الدراسية"""
    academic_years = []
    
    for code, name in ACADEMIC_YEAR_CHOICES:
        year_data = {
            'code': code,
            'name': name,
            'lessons_count': Lesson.objects.filter(academic_year=code).count(),
            'exams_count': Exam.objects.filter(academic_year=code, exam_type='exam').count(),
            'tests_count': Exam.objects.filter(academic_year=code, exam_type='test').count(),
        }
        academic_years.append(year_data)
    
    context = {
        'academic_years': academic_years
    }
    
    return render(request, 'lessons/academic_years.html', context)


def year_one_view(request):
    """عرض الدروس والاختبارات - السنة الأولى"""
    year_code = 'year1'
    year_name = 'السنة الأولى'
    
    lessons = Lesson.objects.filter(academic_year=year_code).order_by('-created_at')
    exams = Exam.objects.filter(academic_year=year_code, exam_type='exam').order_by('-created_at')
    tests = Exam.objects.filter(academic_year=year_code, exam_type='test').order_by('-created_at')
    tips = Tip.objects.filter(academic_year=year_code).order_by('-created_at')
    
    # تجميع حسب المادة
    lessons_by_subject = _group_by_subject(lessons)
    exams_by_subject = _group_by_subject(exams)
    tests_by_subject = _group_by_subject(tests)
    
    context = {
        'year_code': year_code,
        'year_name': year_name,
        'lessons': lessons,
        'exams': exams,
        'tests': tests,
        'tips': tips,
        'lessons_by_subject': lessons_by_subject,
        'exams_by_subject': exams_by_subject,
        'tests_by_subject': tests_by_subject,
        'total_lessons': lessons.count(),
        'total_exams': exams.count(),
        'total_tests': tests.count(),
        'total_tips': tips.count(),
    }
    
    return render(request, 'lessons/year_one.html', context)


def year_two_view(request):
    """عرض الدروس والاختبارات - السنة الثانية"""
    year_code = 'year2'
    year_name = 'السنة الثانية'
    
    lessons = Lesson.objects.filter(academic_year=year_code).order_by('-created_at')
    exams = Exam.objects.filter(academic_year=year_code, exam_type='exam').order_by('-created_at')
    tests = Exam.objects.filter(academic_year=year_code, exam_type='test').order_by('-created_at')
    tips = Tip.objects.filter(academic_year=year_code).order_by('-created_at')
    
    # تجميع حسب المادة
    lessons_by_subject = _group_by_subject(lessons)
    exams_by_subject = _group_by_subject(exams)
    tests_by_subject = _group_by_subject(tests)
    
    context = {
        'year_code': year_code,
        'year_name': year_name,
        'lessons': lessons,
        'exams': exams,
        'tests': tests,
        'tips': tips,
        'lessons_by_subject': lessons_by_subject,
        'exams_by_subject': exams_by_subject,
        'tests_by_subject': tests_by_subject,
        'total_lessons': lessons.count(),
        'total_exams': exams.count(),
        'total_tests': tests.count(),
        'total_tips': tips.count(),
    }
    
    return render(request, 'lessons/year_two.html', context)


def year_three_view(request):
    """عرض الدروس والاختبارات - السنة الثالثة"""
    year_code = 'year3'
    year_name = 'السنة الثالثة'
    
    lessons = Lesson.objects.filter(academic_year=year_code).order_by('-created_at')
    exams = Exam.objects.filter(academic_year=year_code, exam_type='exam').order_by('-created_at')
    tests = Exam.objects.filter(academic_year=year_code, exam_type='test').order_by('-created_at')
    tips = Tip.objects.filter(academic_year=year_code).order_by('-created_at')
    
    # تجميع حسب المادة
    lessons_by_subject = _group_by_subject(lessons)
    exams_by_subject = _group_by_subject(exams)
    tests_by_subject = _group_by_subject(tests)
    
    context = {
        'year_code': year_code,
        'year_name': year_name,
        'lessons': lessons,
        'exams': exams,
        'tests': tests,
        'tips': tips,
        'lessons_by_subject': lessons_by_subject,
        'exams_by_subject': exams_by_subject,
        'tests_by_subject': tests_by_subject,
        'total_lessons': lessons.count(),
        'total_exams': exams.count(),
        'total_tests': tests.count(),
        'total_tips': tips.count(),
    }
    
    return render(request, 'lessons/year_three.html', context)


def year_four_view(request):
    """عرض الدروس والاختبارات - السنة الرابعة"""
    year_code = 'year4'
    year_name = 'السنة الرابعة'
    
    lessons = Lesson.objects.filter(academic_year=year_code).order_by('-created_at')
    exams = Exam.objects.filter(academic_year=year_code, exam_type='exam').order_by('-created_at')
    tests = Exam.objects.filter(academic_year=year_code, exam_type='test').order_by('-created_at')
    tips = Tip.objects.filter(academic_year=year_code).order_by('-created_at')
    
    # تجميع حسب المادة
    lessons_by_subject = _group_by_subject(lessons)
    exams_by_subject = _group_by_subject(exams)
    tests_by_subject = _group_by_subject(tests)
    
    context = {
        'year_code': year_code,
        'year_name': year_name,
        'lessons': lessons,
        'exams': exams,
        'tests': tests,
        'tips': tips,
        'lessons_by_subject': lessons_by_subject,
        'exams_by_subject': exams_by_subject,
        'tests_by_subject': tests_by_subject,
        'total_lessons': lessons.count(),
        'total_exams': exams.count(),
        'total_tests': tests.count(),
        'total_tips': tips.count(),
    }
    
    return render(request, 'lessons/year_four.html', context)


def tips_view(request, year_code):
    """عرض النصائح لسنة دراسية معينة"""
    # التحقق من صحة كود السنة
    valid_years = [code for code, _ in ACADEMIC_YEAR_CHOICES]
    if year_code not in valid_years:
        return render(request, 'lessons/error.html', {'message': 'سنة دراسية غير صحيحة'})
    
    # الحصول على اسم السنة
    year_name = dict(ACADEMIC_YEAR_CHOICES).get(year_code, 'غير معروف')
    
    # جلب النصائح المتعلقة بهذه السنة
    tips = Tip.objects.filter(academic_year=year_code).order_by('-created_at')
    
    # تجميع حسب الموضوع
    tips_by_subject = _group_by_subject(tips)
    
    context = {
        'year_code': year_code,
        'year_name': year_name,
        'tips': tips,
        'tips_by_subject': tips_by_subject,
        'total_tips': tips.count(),
    }
    
    return render(request, 'lessons/tips.html', context)


def _group_by_subject(queryset):
    """دالة مساعدة لتجميع البيانات حسب المادة"""
    grouped = {}
    for item in queryset:
        subject = item.get_subject_display()
        if subject not in grouped:
            grouped[subject] = []
        grouped[subject].append(item)
    return grouped
