from django.shortcuts import render


def home(request):
    return render(request, 'main/index.html')


def about(request):
    """صفحة حول المدرسة"""
    context = {
        'school_name': 'متوسطة 5 جويلية 1962',
        'principal_name': 'Bouzeriba Rebyha Asma',
        'principal_title': 'استاذة اعلام الي',
        'location': {
            'wilaya': 'الطارف',
            'daira': 'القالة',
            'village': 'وادي الحوت'
        },
        'students_count': 214,
    }
    return render(request, 'main/about.html', context)