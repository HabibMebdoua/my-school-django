from django.db import models

# اختيارات المادة
SUBJECT_CHOICES = [
    ('math', 'الرياضيات'),
    ('arabic', 'اللغة العربية'),
    ('french', 'اللغة الفرنسية'),
    ('english', 'اللغة الانجليزية'),
    ('nature', 'علوم الطبيعة والحياة'),
    ('physics', 'الفيزياء'),
    ('social', 'الإجتماعيات'),
    ('islamic', 'التربية الإسلامية'),
    ('it', 'الإعلام الآلي'),
]



# اختيارات السنة الدراسية
ACADEMIC_YEAR_CHOICES = [
    ('year1', 'السنة الأولى'),
    ('year2', 'السنة الثانية'),
    ('year3', 'السنة الثالثة'),
    ('year4', 'السنة الرابعة'),
]

# اختيارات نوع الاختبار
EXAM_TYPE_CHOICES = [
    ('exam', 'اختبار'),
    ('test', 'فرض'),
]

# اختيارات حالة التصحيح
CORRECTION_CHOICES = [
    ('available', 'متوفر التصحيح'),
    ('not_available', 'غير متوفر التصحيح'),
]


class Lesson(models.Model):
    """مودل الدروس"""
    title = models.CharField(max_length=200, verbose_name='عنوان الدرس')
    subject = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES,
        verbose_name='المادة'
    )
    academic_year = models.CharField(
        max_length=10,
        choices=ACADEMIC_YEAR_CHOICES,
        verbose_name='السنة الدراسية'
    )
    pdf_file = models.FileField(
        upload_to='lessons/%Y/%m/',
        verbose_name='ملف الدرس PDF'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'دروس'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['subject', 'academic_year']),
        ]

    def __str__(self):
        return f"{self.title} - {self.get_subject_display()} ({self.get_academic_year_display()})"


class Exam(models.Model):
    """مودل الاختبارات والفروض"""
    title = models.CharField(max_length=200, verbose_name='عنوان الاختبار')
    subject = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES,
        verbose_name='المادة'
    )
    exam_type = models.CharField(
        max_length=10,
        choices=EXAM_TYPE_CHOICES,
        verbose_name='النوع'
    )
    academic_year = models.CharField(
        max_length=10,
        choices=ACADEMIC_YEAR_CHOICES,
        verbose_name='السنة الدراسية'
    )
    correction_status = models.CharField(
        max_length=20,
        choices=CORRECTION_CHOICES,
        verbose_name='حالة التصحيح'
    )
    exam_file = models.FileField(
        upload_to='exams/%Y/%m/',
        verbose_name='ملف الاختبار'
    )
    correction_file = models.FileField(
        upload_to='corrections/%Y/%m/',
        blank=True,
        null=True,
        verbose_name='ملف التصحيح'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'اختبار'
        verbose_name_plural = 'اختبارات'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['subject', 'academic_year', 'exam_type']),
        ]

    def __str__(self):
        return f"{self.title} ({self.get_exam_type_display()}) - {self.get_subject_display()} ({self.get_academic_year_display()})"


class Tip(models.Model):
    """مودل النصائح والإرشادات"""
    title = models.CharField(max_length=200, verbose_name='عنوان النصيحة')
    subject = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES,
        verbose_name='الموضوع'
    )
    academic_year = models.CharField(
        max_length=10,
        choices=ACADEMIC_YEAR_CHOICES,
        verbose_name='السنة الدراسية'
    )
    content = models.TextField(verbose_name='محتوى النصيحة')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'نصيحة'
        verbose_name_plural = 'نصائح'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['subject', 'academic_year']),
        ]

    def __str__(self):
        return f"{self.title} - {self.get_subject_display()} ({self.get_academic_year_display()})"


class AccessPassword(models.Model):
    """مودل كلمة السر للوصول للموقع"""
    password = models.CharField(
        max_length=255,
        verbose_name='كلمة السر',
        unique=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='مفعلة'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'كلمة السر'
        verbose_name_plural = 'كلمات السر'
        ordering = ['-created_at']

    def __str__(self):
        return f"كلمة السر - {'مفعلة' if self.is_active else 'معطلة'}"

