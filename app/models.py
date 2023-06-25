from django.db import models
from django.contrib.auth.models import User


class PersonalData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=15, default='')
    gender = models.CharField(max_length=20)
        
    def __str__(self):
        return str(f"Object [{self.user}]")

class WorkedTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    employment_period_months = models.PositiveIntegerField(default=0)
    gross_salary = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    contribution_amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return str(f"Object [{self.user}]")

class WorkedList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    worked_time = models.ForeignKey(WorkedTime, on_delete=models.CASCADE)

    def __str__(self):
        return str(f"Object [{self.user}]")

class Statistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    months_worked = models.PositiveIntegerField()
    salary_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)

    def __str__(self):
        return str(f"Object [{self.user}]")

class NewsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return str(f"Object [{self.title}]")

class Contribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    initial_capital = models.DecimalField(max_digits=20, decimal_places=2)
    indexed_contributions = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    current_payment = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    
    def __str__(self):
        return str(f"Object [{self.user}]")
    
class RetirementValue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contribution = models.ForeignKey(Contribution, on_delete=models.CASCADE)
    retirement_payment = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return str(f"Object [{self.user}]")