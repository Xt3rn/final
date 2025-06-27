from django.db import models

class Diplom(models.Model):
    org_name = models.CharField("Название образовательной организации", max_length=200)
    qualification = models.CharField("Квалификация", max_length=100)
    ser_number = models.IntegerField("Номер серии", max_length=13)
    reg_number = models.CharField("Регистрационный номер", max_length=10)
    grant_date = models.DateField("Дата выдачи")
    student_name = models.CharField("Настоящий диплом"
                                    "свидетельствует о том, что", max_length=200)
    complete = models.CharField("Осовил(а) образовательную программу"
                                "среднего профессионального образования и успешно"
                                "прошёл(шла) государственную итоговую аттестацию"
                                "по специальности", max_length=100)
    title = models.CharField("Название диплома", max_length=300)
    supervisor = models.CharField("Руководитель", max_length=200)
    year = models.DateField("Дата решения")
    copy = models.FileField("Копия диплома")


    def __str__(self):
        return f"{self.student_name} - {self.title} ({self.year})"