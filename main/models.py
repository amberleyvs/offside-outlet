import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    wishlisted_by = models.ManyToManyField(User, related_name="wishlist", blank=True)
    stock = models.PositiveIntegerField(default=0)

    #optional attributes
    discount = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Discount Percentage (0-100). e.g 20 = 20% off"
    )

    is_limited = models.BooleanField(
        default=False,
        help_text="True if limited edition"
    )
    
    def __str__(self):
        return self.name
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()
    
    def price_after_discount(self) -> int:
        d = max(0, min(100, int(self.discount or 0)))
        return int(round(self.price * (100 - d) / 100))


# model employee 3 fields: name (less than2 255), age (int), persona (gaboleh pake charfield)
class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    persona = models.TextField()

#car: name max len 255; brand sama; stock int
class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    stock = models.IntegerField()

# # book: id(uuid), title(cgarfiels 255)
# class Book(models.Model):
#     id = models.UUIDField()
#     title = models.CharField(max_length=255)

# # author: bio(textfield), user(satu user satu author)
# class Author(models.Model):
#     bio = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

# # satu author bisa banyak book, satu book ditulis banyak outhor
# class AuthorWrittenBy(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     authorID = models.UUIDField
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
