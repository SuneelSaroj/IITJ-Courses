
# Create your models here.
from django.db import models


class FirstSemesterCourse(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100, default="", blank=True)
    ltp = models.CharField(max_length=100, default="", blank=True)
    offered_for = models.CharField(max_length=100, default="", blank=True)
    course_code = models.CharField(max_length=100, default="", blank=True)
    type = models.CharField(max_length=100, default="", blank=True)
    prerequisite = models.CharField(max_length=100, default="Nil", blank=True)
    objective1 = models.CharField(max_length=500, default="", blank=True)
    objective2 = models.CharField(max_length=500, default="", blank=True)
    objective3 = models.CharField(max_length=500, default="", blank=True)
    learning_outcome1 = models.CharField(
        max_length=500, default="", blank=True)
    learning_outcome2 = models.CharField(
        max_length=500, default="", blank=True)
    learning_outcome3 = models.CharField(
        max_length=500, default="", blank=True)

    content1 = models.TextField(default="", blank=True)
    content2 = models.TextField(default="", blank=True)
    content3 = models.TextField(default="", blank=True)
    content4 = models.TextField(default="", blank=True)
    content5 = models.TextField(default="", blank=True)
    content7 = models.TextField(default="", blank=True)
    content8 = models.TextField(default="", blank=True)

    laboratory1 = models.CharField(max_length=1000, default="", blank=True)
    laboratory2 = models.CharField(max_length=1000, default="", blank=True)
    laboratory3 = models.CharField(max_length=1000, default="", blank=True)
    laboratory4 = models.CharField(max_length=1000, default="", blank=True)
    laboratory5 = models.CharField(max_length=1000, default="", blank=True)
    laboratory6 = models.CharField(max_length=1000, default="", blank=True)
    laboratory7 = models.CharField(max_length=1000, default="", blank=True)
    laboratory8 = models.CharField(max_length=1000, default="", blank=True)
    laboratory9 = models.CharField(max_length=1000, default="", blank=True)
    laboratory10 = models.CharField(max_length=1000, default="", blank=True)

    textbook1 = models.CharField(max_length=1000, default="", blank=True)
    textbook2 = models.CharField(max_length=1000, default="", blank=True)
    textbook3 = models.CharField(max_length=1000, default="", blank=True)
    textbook4 = models.CharField(max_length=1000, default="", blank=True)
    textbook5 = models.CharField(max_length=1000, default="", blank=True)
    textbook6 = models.CharField(max_length=1000, default="", blank=True)

    reference_book1 = models.CharField(max_length=500, default="", blank=True)
    reference_book2 = models.CharField(max_length=500, default="", blank=True)
    reference_book3 = models.CharField(max_length=500, default="", blank=True)
    reference_book4 = models.CharField(max_length=500, default="", blank=True)
    self_mearning_material1 = models.CharField(
        max_length=500, default="", blank=True)
    self_mearning_material2 = models.CharField(
        max_length=500, default="", blank=True)
    self_mearning_material3 = models.CharField(
        max_length=500, default="", blank=True)

    activities1 = models.CharField(max_length=1000, default="", blank=True)
    activities2 = models.CharField(max_length=1000, default="", blank=True)
    activities3 = models.CharField(max_length=1000, default="", blank=True)

    def __str__(self):
        return self.title


class SecondSemesterCourse(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100, default="", blank=True)
    ltp = models.CharField(max_length=100, default="", blank=True)
    offered_for = models.CharField(max_length=100, default="", blank=True)
    course_code = models.CharField(max_length=100, default="", blank=True)
    type = models.CharField(max_length=100, default="", blank=True)
    prerequisite = models.CharField(max_length=100, default="Nil", blank=True)
    objective1 = models.CharField(max_length=500, default="", blank=True)
    objective2 = models.CharField(max_length=500, default="", blank=True)
    objective3 = models.CharField(max_length=500, default="", blank=True)
    objective4 = models.CharField(max_length=500, default="", blank=True)
    objective5 = models.CharField(max_length=500, default="", blank=True)
    learning_outcome1 = models.CharField(
        max_length=500, default="", blank=True)
    learning_outcome2 = models.CharField(
        max_length=500, default="", blank=True)
    learning_outcome3 = models.CharField(
        max_length=500, default="", blank=True)
    learning_outcome4 = models.CharField(
        max_length=500, default="", blank=True)
    learning_outcome5 = models.CharField(
        max_length=500, default="", blank=True)

    content1 = models.TextField(default="", blank=True)
    content2 = models.TextField(default="", blank=True)
    content3 = models.TextField(default="", blank=True)
    content4 = models.TextField(default="", blank=True)
    content5 = models.TextField(default="", blank=True)
    content7 = models.TextField(default="", blank=True)
    content8 = models.TextField(default="", blank=True)

    laboratory1 = models.CharField(max_length=1000, default="", blank=True)
    laboratory2 = models.CharField(max_length=1000, default="", blank=True)
    laboratory3 = models.CharField(max_length=1000, default="", blank=True)
    laboratory4 = models.CharField(max_length=1000, default="", blank=True)
    laboratory5 = models.CharField(max_length=1000, default="", blank=True)
    laboratory6 = models.CharField(max_length=1000, default="", blank=True)
    laboratory7 = models.CharField(max_length=1000, default="", blank=True)
    laboratory8 = models.CharField(max_length=1000, default="", blank=True)
    laboratory9 = models.CharField(max_length=1000, default="", blank=True)
    laboratory10 = models.CharField(max_length=1000, default="", blank=True)

    textbook1 = models.CharField(max_length=1000, default="", blank=True)
    textbook2 = models.CharField(max_length=1000, default="", blank=True)
    textbook3 = models.CharField(max_length=1000, default="", blank=True)
    textbook4 = models.CharField(max_length=1000, default="", blank=True)
    textbook5 = models.CharField(max_length=1000, default="", blank=True)
    textbook6 = models.CharField(max_length=1000, default="", blank=True)

    reference_book1 = models.CharField(max_length=500, default="", blank=True)
    reference_book2 = models.CharField(max_length=500, default="", blank=True)
    reference_book3 = models.CharField(max_length=500, default="", blank=True)
    reference_book4 = models.CharField(max_length=500, default="", blank=True)
    reference_book4 = models.CharField(max_length=500, default="", blank=True)
    self_mearning_material1 = models.CharField(
        max_length=500, default="", blank=True)
    self_mearning_material2 = models.CharField(
        max_length=500, default="", blank=True)
    self_mearning_material3 = models.CharField(
        max_length=500, default="", blank=True)
    self_mearning_material4 = models.CharField(
        max_length=500, default="", blank=True)
    self_mearning_material5 = models.CharField(
        max_length=500, default="", blank=True)

    activities1 = models.CharField(max_length=1000, default="", blank=True)
    activities2 = models.CharField(max_length=1000, default="", blank=True)
    activities3 = models.CharField(max_length=1000, default="", blank=True)
    activities4 = models.CharField(max_length=1000, default="", blank=True)

    def __str__(self):
        return self.title
