from django.db import models
from django.conf import settings


# Category => 1:M Food_Item
# FoodItem => 1:M Order_Item
# Order => 1:M Order_Item
# OrderItem => M:1 Food_Item and Order


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, unique=True)
    category_image = models.ImageField(
        upload_to="categories/",
        default="categories/default.PNG"
        )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class FoodItem(models.Model):
    food_item_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=50, unique=True)
    food_price = models.DecimalField(max_digits=10, decimal_places=2)
    food_description = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    # Relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="food_items")

    def __str__(self):
        return f"{self.food_name} - ${self.food_price}"


class Order(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Preparing", "Preparing"),
        ("Ready", "Ready"),
        ("Delivered", "Delivered")
    ]

    order_id = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="orders"
    )

    customer_id = models.CharField("Customer ID", max_length=30, blank=True)
    customer_name = models.CharField(max_length=50)


    timestamp = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=9, choices=STATUS_CHOICES) 

    def __str__(self):
        return f"Order #{self.order_id} - {self.customer_name} [{self.order_status}]"
    
    @property  
    def total_amount(self):
        total = sum(item.subtotal for item in self.items.all()) 
        return total
    
    def save(self, *args, **kwargs):
        if self.user:
            if not self.customer_name:
                self.customer_name = (self.user.get_full_name() or self.user.username)
            if not self.customer_id:
                self.customer_id = getattr(self.user, "student_id", "") or self.customer_id
        super().save(*args, **kwargs)
    

class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()

    # Relationships
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='order_items')

    # Composite Key order + food_item
    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["order", "food_item"], name="order_item_id"
        )]

    @property
    def subtotal(self):
        return self.food_item.food_price * self.quantity

    def __str__(self):
        return f"{self.food_item.food_name} x {self.quantity}"