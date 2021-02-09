from django.db import models

# Create your models here.

class Parent(models.Model):
    first = models.CharField(max_length = 64)
    last = models.CharField(max_length = 64)
    user = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
    email = models.EmailField()
    details = models.CharField(max_length = 200, blank = True)

    def __str__(self):
        return f"{self.first} {self.last} {self.email}"

class Student(models.Model):
    first = models.CharField(max_length = 64)
    last = models.CharField(max_length = 64)
    user = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
    email = models.EmailField()
    details = models.CharField(max_length = 200, blank = True)
    parents = models.ManyToManyField(Parent, blank = True, related_name = 'parents')

    def __str__(self):
        return f"{self.first} {self.last} {self.email}"

class Teacher(models.Model):
    first = models.CharField(max_length = 64)
    last = models.CharField(max_length = 64)
    user = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
    email = models.EmailField()
    details = models.CharField(max_length = 200, blank = True)

    def __str__(self):
        return f"{self.first} {self.last} {self.email}"

class Class(models.Model):
    students = models.ManyToManyField(Student, blank = True, related_name = 'students')
    teachers = models.ManyToManyField(Teacher, blank = True, related_name = 'teachers')
    class_name = models.CharField(max_length = 3)

    def __str__(self):
        return f"{self.class_name}"

class Subject(models.Model):
    subject_name = models.CharField(max_length = 64)
    xclass = models.ForeignKey(Class, on_delete = models.CASCADE, related_name = 'xclass')

    def __str__(self):
        return f"{self.subject_name} in {self.xclass}"

class Document(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete = models.CASCADE, related_name = 'subjects')
    doc = models.FileField(upload_to = '')
    date = models.DateField()

class Assignment(models.Model):
    class_id = models.ForeignKey(Class, on_delete = models.CASCADE, related_name = 'classes')
    date = models.DateTimeField()
    details = models.CharField(max_length = 200)
    doc = models.FileField(blank = True)

class Grade(models.Model):
    student = models.OneToOneField(Student, on_delete = models.CASCADE, primary_key = True)
    grade = models.IntegerField()
    date = models.DateTimeField()

class Absence(models.Model):
    student = models.OneToOneField(Student, on_delete = models.CASCADE, primary_key = True)
    date = models.DateTimeField()
    