from django.db import models

# Create your models here.

class User(models.Model):
    SEX = (
        ('1', 'Мужчина'),
        ('0', 'Женщина')

    )
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX, null=True, blank=True)
    city = models.CharField(max_length=20, editable=False)
    age = models.IntegerField(default=18)

    def __str__(self):
        return f"{self.first_name.title()} {self.last_name.title()}"
# primary_key=True
class Product(models.Model):
    PRODUCT_TYPE = (
        ('1', 'fruit'),
        ('2', 'veg'),
        (None, 'Unknown')

    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20, choices=PRODUCT_TYPE, null=True, blank = True)

    def __str__(self):
        return f'{self.name}'


class Cart(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product}"

    class Meta:
        unique_together = ('user', 'product')
