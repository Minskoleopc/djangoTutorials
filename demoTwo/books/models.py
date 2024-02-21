from django.db import models

# Create your models here.
# what  is data ??

# temporary data   semi persistance   persistance 
# variable           session           db store

# sql             no sql
#table based      document based 
#id  name   age   {id:1,name:"Max",age:31} 
#1    Max   31    {id:2,name:"Manu",age:32}
#2    Mat   32
# MySQL , postgres , Oracle     Mongo
 
class Book(models.Model):
    title = models.CharField(max_length = 50)
    rating = models.IntegerField()




