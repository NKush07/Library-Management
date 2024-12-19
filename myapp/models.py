from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=20)
    name = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=20, null=True)
    phone = models.IntegerField(null=True)
    password = models.TextField()
    class Meta:
        db_table='user'
        

class Book(models.Model):
    b_date = models.DateField(null=True, blank=True)
    b_category = models.CharField(max_length=50, null=True, blank=True)
    b_name = models.CharField(max_length=50, null=True, blank=True)
    b_author = models.CharField(max_length=20, null=True, blank=True)
    b_publish = models.CharField(max_length=50, null=True, blank=True)
    b_year = models.IntegerField(null=True, blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
	    db_table='book'
  
  
class Rental(models.Model):
    r_date = models.DateField(null=True, blank=True)
    r_time = models.TimeField(null=True, blank=True)
    person_name = models.CharField(max_length=50, null=True, blank=True)
    rb_name = models.CharField(max_length=20, null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)  
    submit = models.CharField(max_length=5, null=True, blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    class Meta:
	    db_table='rental'
