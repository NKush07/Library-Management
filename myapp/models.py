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
    b_date = models.DateField()
    b_category = models.CharField(max_length=50)
    b_name = models.CharField(max_length=50)
    b_author = models.CharField(max_length=20)
    b_publish = models.CharField(max_length=50)
    b_year = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
	    db_table='book'
  
  
class Rental(models.Model):
    r_date = models.DateField()
    r_time = models.TimeField()
    person_name = models.CharField(max_length=50)
    rb_name = models.CharField(max_length=20)
    return_date = models.DateField()  
    submit = models.CharField(max_length=5)
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    class Meta:
	    db_table='rental'
