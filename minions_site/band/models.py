from django.db import models


class Show(models.Model):
    title = models.CharField(max_length=120)
    venue = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    is_sold_out = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title} @ {self.venue} ({self.date})"


class BandMember(models.Model):
    name = models.CharField(max_length=80)
    role = models.CharField(max_length=80)
    bio = models.TextField(blank=True)
    def __str__(self):
        return f"{self.name} – {self.role}"


class Member(models.Model):
    """A band member with name, role, photo and a short bio."""
