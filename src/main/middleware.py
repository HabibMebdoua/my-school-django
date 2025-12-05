from django.shortcuts import redirect
from django.urls import reverse, NoReverseMatch


class AuthenticationMiddleware:
    """middleware للتحقق من تسجيل الدخول"""
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # الصفحات التي لا تحتاج تسجيل دخول
        public_urls = ['/admin/', '/login/']
        
        # السماح للصفحات العامة والـ admin
        if any(request.path.startswith(url) for url in public_urls):
            return self.get_response(request)
        
        # التحقق من تسجيل الدخول للصفحات الأخرى
        if 'is_authenticated' not in request.session:
            return redirect('main:login')
        
        response = self.get_response(request)
        return response
