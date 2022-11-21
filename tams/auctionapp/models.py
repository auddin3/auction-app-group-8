from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    '''
    Our User models is a sub-class of Django's AbstractUser
    So we can make use of Django's authentication system
    '''
    username = models.CharField(max_length=50, unique=True, primary_key=True)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    email = models.EmailField(max_length = 254)
    dob = models.DateField(auto_now=True)

    bids = models.ManyToManyField(
        to='self',
        blank=True,
        symmetrical=False,
        through='Bid',
        related_name='submits'
    )


    def __str__(self):
        return self.username

class Item(models.Model):

    '''
    An Item is is an object with detailed properties
    that a User can bid on
    '''
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=4096)
    startPrice = models.DecimalField(max_digits=10, decimal_places=2)
    endOfAuction = models.DateField(auto_now=True)

    owner = models.ForeignKey(
        to=User,
        related_name='owner',
        on_delete=models.CASCADE
    )

    messages = models.ManyToManyField(
        to='self',
        blank=True,
        symmetrical=False,
        through='Message',
        related_name='causes'
    )
    

class Bid(models.Model):
    topBidder = models.ForeignKey(
        to=User,
        related_name='places',
        on_delete=models.CASCADE
    )

    itemId = models.ForeignKey(
        to=Item,
        related_name='bidded_on',
        on_delete=models.CASCADE
    )

    bidPrice = models.DecimalField(max_digits=10, decimal_places=2)

class Message(models.Model):
    '''
    The Message models is the 'through' model for
    the 'message' ManyToMany relationship between Members
    '''

    itemId = models.ForeignKey(
        to=Item,
        related_name='about',
        on_delete=models.CASCADE
    )

    sender = models.ForeignKey(
        to=User,
        related_name='sent',
        on_delete=models.CASCADE
    )
    recip = models.ForeignKey(
        to=User,
        related_name='received',
        on_delete=models.CASCADE
    )
    question = models.CharField(max_length=4096)
    answer = models.CharField(max_length=4096)

    def __str__(self):
        return f"From {self.sender} to {self.recip}"