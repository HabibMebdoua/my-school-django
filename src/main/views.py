from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden
from lessons.models import AccessPassword


def home(request):
    # التحقق من وجود جلسة تسجيل دخول
    if 'is_authenticated' not in request.session:
        return redirect('main:login')
    return render(request, 'main/index.html')


def login_view(request):
    """صفحة تسجيل الدخول"""
    if request.method == 'POST':
        password = request.POST.get('password', '')
        
        # التحقق من كلمة السر
        access_pass = AccessPassword.objects.filter(password=password, is_active=True).first()
        
        if access_pass:
            # تعيين جلسة تسجيل الدخول
            request.session['is_authenticated'] = True
            request.session.set_expiry(86400 * 30)  # 30 يوم
            messages.success(request, 'تم تسجيل الدخول بنجاح!')
            return redirect('main:home')
        else:
            messages.error(request, 'كلمة السر غير صحيحة!')
    
    return render(request, 'main/login.html')


def logout_view(request):
    """تسجيل الخروج"""
    if 'is_authenticated' in request.session:
        del request.session['is_authenticated']
    messages.info(request, 'تم تسجيل الخروج بنجاح!')
    return redirect('main:login')


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