from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator

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


class Book(models.Model):
    title = models.CharField(max_length = 50)
    rating = models.IntegerField(validators = [MinValueValidator(1),MaxValueValidator(5)])
    author = models.CharField(null = True ,max_length = 100)
    is_bestSelling = models.BooleanField(default = False)


    def __str__(self):
            return self.title
    
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
    #https://docs.djangoproject.com/en/5.0/topics/db/queries/














