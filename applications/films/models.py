from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Films(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Films'
        verbose_name = 'Film'
    
    
RATE_CHOICES = [
    (1, '1 - Too bad'),
    (2, '2 - Bad'),
    (3, '3 - Normal'),
    (4, '4 - Good'),
    (5, '5 - Perfect')
]
    
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    film = models.ForeignKey(Films , on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000 , null=True, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    likes= models.PositiveIntegerField(default=0, null=True, blank=True)
    

    def __str__(self):
        return self.film.title

    
    class Meta:
        verbose_name_plural = 'Review'
        verbose_name = 'Review'    
    
    
    
    
