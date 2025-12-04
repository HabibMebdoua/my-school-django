from django.urls import path, include
from . import views

app_name = 'lessons'

urlpatterns = [
    # عرض جميع السنوات الدراسية
    path('', views.all_years_view, name='all_years'),
    
    # مسارات السنوات الدراسية الفردية
    path('year/year1/', views.year_one_view, name='year_detail'),
    path('year1/', views.year_one_view, name='year1'),
    
    path('year/year2/', views.year_two_view, name='year2_detail'),
    path('year2/', views.year_two_view, name='year2'),
    
    path('year/year3/', views.year_three_view, name='year3_detail'),
    path('year3/', views.year_three_view, name='year3'),
    
    path('year/year4/', views.year_four_view, name='year4_detail'),
    path('year4/', views.year_four_view, name='year4'),
    
    # مسارات النصائح
    path('year/year1/tips/', views.tips_view, {'year_code': 'year1'}, name='tips_year1'),
    path('year/year2/tips/', views.tips_view, {'year_code': 'year2'}, name='tips_year2'),
    path('year/year3/tips/', views.tips_view, {'year_code': 'year3'}, name='tips_year3'),
    path('year/year4/tips/', views.tips_view, {'year_code': 'year4'}, name='tips_year4'),
    path('tips/<str:year_code>/', views.tips_view, name='tips'),
]

