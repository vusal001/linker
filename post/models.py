from django.db import models
from django_resized import ResizedImageField
from django.utils.timezone import now
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True, related_name='posts', verbose_name='İstifadəçi')
    
    link = models.CharField(verbose_name='Link', max_length=1000)
    
    title = models.CharField(max_length=100, verbose_name='Qrupun adı')
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriya')
    
    TYPE = (
        ('Whatsapp', 'Whatsapp'),
        ('Telegram', 'Telegram'),
        ('Facebook', 'Facebook'),
        ('Youtube', 'Youtube'),
        ('TikTok', 'TikTok'),
        ('Instagram', 'Instagram'),
    )
    
    linktype = models.CharField(choices=TYPE ,max_length=100, verbose_name='Platforma', blank=True, null=True)

    image = ResizedImageField(size=[1280, 720], quality=80, verbose_name="Sekil", blank=True, null=True, force_format='JPEG')

    sssss = models.IntegerField(verbose_name="Like sayı", default=0, blank=True, null=True)

    liked = models.ManyToManyField(User, blank=True, related_name='post_like')

    views = models.IntegerField(verbose_name="Baxış sayı", default=0, blank=True, null=True)

    preminium = models.BooleanField(verbose_name="Preminium", default=False)

    posting_date = models.DateTimeField(auto_now_add=True, verbose_name="Yüklənmə vaxtı")

    updatedate = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self) -> str:
        return self.title






LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)




# Create your models here.
