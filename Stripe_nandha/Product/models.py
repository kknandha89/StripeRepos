from django.db import models

class Product(models.Model):
    productId =  models.AutoField(primary_key=True)
    productName =  models.CharField(max_length=100,null=True)
    productPrice =  models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.productName

    # def get_display_price(self):
    #     dis_price = int(self.productPrice) * 100
    #     return "{0:.2f}".format(dis_price)

    class Meta:
        db_table = 'Product'
