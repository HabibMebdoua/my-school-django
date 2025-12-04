from django.shortcuts import render
from .models import Lesson, Exam, ACADEMIC_YEAR_CHOICES


def all_years_view(request):
    """عرض جميع السنوات الدراسية"""
    academic_years = [
        {'code': code, 'name': name} 
        for code, name in ACADEMIC_YEAR_CHOICES
    ]
    
    # إحصائيات لكل سنة
    for year in academic_years:
        year['lessons_count'] = Lesson.objects.filter(academic_year=year['code']).count()
        year['exams_count'] = Exam.objects.filter(academic_year=year['code'], exam_type='exam').count()
        year['tests_count'] = Exam.objects.filter(academic_year=year['code'], exam_type='test').count()
    
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
        'lessons_by_subject': lessons_by_subject,
        'exams_by_subject': exams_by_subject,
        'tests_by_subject': tests_by_subject,
        'total_lessons': lessons.count(),
        'total_exams': exams.count(),
        'total_tests': tests.count(),
    }
    
    return render(request, 'lessons/year_one.html', context)


def year_two_view(request):
    """عرض الدروس والاختبارات - السنة الثانية"""
    year_code = 'year2'
    year_name = 'السنة الثانية'
    
    lessons = Lesson.objects.filter(academic_year=year_code).order_by('-created_at')
    exams = Exam.objects.filter(academic_year=year_code, exam_type='exam').order_by('-created_at')
    tests = Exam.objects.filter(academic_year=year_code, exam_type='test').order_by('-created_at')
    
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
        'lessons_by_subject': lessons_by_subject,
        'exams_by_subject': exams_by_subject,
        'tests_by_subject': tests_by_subject,
        'total_lessons': lessons.count(),
        'total_exams': exams.count(),
        'total_tests': tests.count(),
    }
    
    return render(request, 'lessons/year_two.html', context)


def year_three_view(request):
    """عرض الدروس والاختبارات - السنة الثالثة"""
    year_code = 'year3'
    year_name = 'السنة الثالثة'
    
    lessons = Lesson.objects.filter(academic_year=year_code).order_by('-created_at')
    exams = Exam.objects.filter(academic_year=year_code, exam_type='exam').order_by('-created_at')
    tests = Exam.objects.filter(academic_year=year_code, exam_type='test').order_by('-created_at')
    
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
        'lessons_by_subject': lessons_by_subject,
        'exams_by_subject': exams_by_subject,
        'tests_by_subject': tests_by_subject,
        'total_lessons': lessons.count(),
        'total_exams': exams.count(),
        'total_tests': tests.count(),
    }
    
    return render(request, 'lessons/year_three.html', context)


def year_four_view(request):
    """عرض الدروس والاختبارات - السنة الرابعة"""
    year_code = 'year4'
    year_name = 'السنة الرابعة'
    
    lessons = Lesson.objects.filter(academic_year=year_code).order_by('-created_at')
    exams = Exam.objects.filter(academic_year=year_code, exam_type='exam').order_by('-created_at')
    tests = Exam.objects.filter(academic_year=year_code, exam_type='test').order_by('-created_at')
    
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
        'lessons_by_subject': lessons_by_subject,
        'exams_by_subject': exams_by_subject,
        'tests_by_subject': tests_by_subject,
        'total_lessons': lessons.count(),
        'total_exams': exams.count(),
        'total_tests': tests.count(),
    }
    
    return render(request, 'lessons/year_four.html', context)


def _group_by_subject(queryset):
    """دالة مساعدة لتجميع البيانات حسب المادة"""
    grouped = {}
    for item in queryset:
        subject = item.get_subject_display()
        if subject not in grouped:
            grouped[subject] = []
        grouped[subject].append(item)
    return grouped
