from django.db import  models
from .category import Category

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    @staticmethod
    def get_all_subcategories():
        return Subcategory.objects.all()

    def get_all_subcategories_by_category_id(category_id):
        if category_id:
            return Subcategory.objects.filter(category = category_id)

    def __str__(self):
        return self.name