import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shorts', 'Shorts'),
        ('socks', 'Socks'),
        ('training', 'Training Equipment'),
        ('bag', 'Sports Bag'),
        ('accessory', 'Accessory'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=80, choices=CATEGORY_CHOICES, default='other')
    is_featured = models.BooleanField(default=False)

    #optional attributes
    discount = models.PositiveIntegerField(
        default=0,
        help_text="Persentase diskon (0-100). Misal 20 = 20% off"
    )
    is_limited = models.BooleanField(
        default=False,
        help_text="True kalau produk edisi terbatas"
    )
    
    def __str__(self):
        return self.title
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()

    # model employee 3 fields: name (less than2 255), age (int), persona (gaboleh pake charfield)

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    persona = models.TextField()

