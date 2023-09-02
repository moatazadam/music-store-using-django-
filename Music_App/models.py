from django.db import models



class Artist(models.Model) :
    name = models.CharField(max_length=150)
    bio = models.TextField(max_length=1000)
    image = models.ImageField(blank=True , null=True)


    def __str__(self) :
        return self.name
    


class Album(models.Model) :
    choices = [
        ('Rap' , 'Rap') ,
        ('Pop' , 'Pop') , 
        ( 'Jazz' , 'Jazz'),
        ('Hip-Hop' , 'Hip-Hop')
    ]
    s = [
        ('available', 'available'),
        ('out of stock' , 'out of stock')
     ]
    title = models.CharField(max_length=150)
    oldprice = models.DecimalField(max_digits=6 , decimal_places=2)
    newprice = models.DecimalField(max_digits=6 , decimal_places=2)
    favorite = models.BooleanField(default=False )
    special = models.BooleanField(default=False )
    desciption = models.TextField(max_length=150)
    type = models.CharField(max_length=50 , choices=choices )
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    status = models.CharField( max_length=50 , choices=s ,blank=True , null=True)
    image = models.ImageField(blank=True , null=True)

    def __str__(self) :
        return self.title


class Contact(models.Model) :
    name = models.CharField(max_length= 100)
    email = models.CharField(max_length= 100)
    mobile = models.IntegerField(max_length=11)
    subject = models.TextField(max_length= 500)
    
    def __str(self):
        return self.name