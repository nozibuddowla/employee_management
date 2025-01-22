from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, editable=True, blank=True, null=True)
    DESIGNATION_CHOICES = [
        ("Manager", "Manager"),
        ("Developer", "Developer"),
        ("Designer", "Designer"),
        ("Tester", "Tester"),
        ("HR", "HR"),
        ("Other", "Other"),
    ]
    designation = models.CharField(max_length=255, choices=DESIGNATION_CHOICES, editable=True, blank=True, null=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if self.pk:
            self.salary = self.__class__.objects.get(pk=self.pk).salary
            self.designation = self.__class__.objects.get(pk=self.pk).designation
        elif not self.salary:
            self.salary = 0
            self.designation = "Other"

        super(Employees, self).save(*args, **kwargs)

    def __str__(self):
        return self.name