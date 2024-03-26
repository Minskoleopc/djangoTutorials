from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
# address has one to one with author
class Address(models.Model):
    stree= models.CharField(max_lenght = 80)
    post_code = models.CharField(max_length = 6)
    city = models.CharField(max_length = 50)

# author has one to many with books 
class Author(models.Model):
    first_name = models.CharField(max_lenth = 100)
    last_name  = models.CharField(max_lenght = 100)
    address = models.OneToOneField(Address,on_delete = models.CASCADE)

class Book(models.Model):
    title = models.CharField(max_length = 50)
    rating  = models.IntegerField()
    author = models.ForeignKey(Author,on_delete = models.CASCASE)
    is_bestselling = models.BooleanField(default = False)







    









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
 
# Temporary       Semi- persistent      Persistent data 
# user input       fb example            Data store in db
# blog              usersession,token

# Data 2 types 
#SQL               No Sql
#Mysql             MongoDB 
#Oracle             Cansandra
#Postgres


# create table and set Table
# insert the data into date
# update the data from the table 
# retrive the data frmom

# focus on data , not the quries 
# define data models and use object and run common queries
# python and indrirectly will be converted to sql lite querues


# class Book(models.Model):
#     title = models.CharField(max_length = 50)
#     rating = models.IntegerField()


# class Book(models.Model):
#     title = models.CharField(max_length = 50)
#     rating = models.IntegerField(validators = [MinValueValidator(1),MaxValueValidator(5)])
#     author = models.CharField(null = True ,max_length = 100)
#     is_bestSelling = models.BooleanField(default = False)

#     def __str__(self):
#             return self.title

    #create
    # b1 = Book(title = "k",rating =5,author= "chinmay",is_bestSelling=True)
    # b1.save()
    #Book.objects.create(title = "k",rating =5,author= "chinmay",is_bestSelling=True)

    #retrive 
    #b1 = Books.object.all()[0]

    # update 
    #b1.title = "ram"
    #b1.delete()

    #---------------------------------------------------------------------->
    #Book.objects.get(id = 1)
    #Book.objects.get(id = 2)
    #queries executed
    #Book.objects.get(id = 2) 
    #Book.objects.get(title = "ramayan")
    #Book.objects.filter(is_bestSelling = True)
    #Book.objects.filter(id__gte=2)
    #Book.objects.filter(id__lte=2)
    #Book.objects.filter(id__gte=2)
    #Book.objects.filter(id__gt=2)
    # AND operation
    #Book.objects.filter(id__gt=2,is_bestSelling=False)
    #Book.objects.filter(title__startswith="r").values() 
    #Book.objects.filter(title__endswith="e").values() 
    






   











