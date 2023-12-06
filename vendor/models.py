# yourappname/models.py
from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    vendor_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=20, unique=True)
    vendor_reference = models.CharField(max_length=50)
    order_date = models.DateField()
    items = models.TextField()
    quantity = models.PositiveIntegerField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    quality_rating = models.DecimalField(max_digits=5, decimal_places=2)
    response_time = models.DecimalField(max_digits=5, decimal_places=2)
    fulfilled_without_issue = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ], default='draft')

    def __str__(self):
        return f"PO #{self.po_number} - {self.vendor_reference}"
    
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateField()
    on_time_delivery_rate = models.DecimalField(max_digits=5, decimal_places=2)
    quality_rating_avg = models.DecimalField(max_digits=5, decimal_places=2)
    average_response_time = models.DecimalField(max_digits=5, decimal_places=2)
    fulfillment_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"    