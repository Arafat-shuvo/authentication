from django.db import models

# Create your models here.
class StudentModel(models.Model):
    Gender_types = [
    ('male','male'),  ('female','female'),  ('others','others'),  
    ]
    gender = models.CharField(max_length=20, choices=Gender_types)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=100)
    student_phone = models.CharField(max_length=15)
    student_address = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    
def __str__(self):
    return self.student_name
