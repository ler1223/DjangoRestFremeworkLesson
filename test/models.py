from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name