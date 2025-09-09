import uuid
from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('transfer', 'Transfer'),
        ('update', 'Update'),
        ('exclusive', 'Exclusive'),
        ('match', 'Match'),
        ('rumor', 'Rumor'),
        ('analysis', 'Analysis'),
    ]
    
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=80)
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