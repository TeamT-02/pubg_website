from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
from datetime import timedelta


class CustomUser(AbstractUser):
    USER = (
        (1, 'Hod'),
        ("lobby_admin", "lobby_admin"),
        ("players", 'players'),

    )
    about = models.TextField(max_length=300)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='images/profile_pic')


class Admin_mine(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username


class Admin_mine_Feedback(models.Model):
    staff_id = models.ForeignKey(Admin_mine, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_replay = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name


class Admine_mine_Notification(models.Model):
    staff_id = models.ForeignKey(Admin_mine, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.staff_id.admin.first_name


class Home(models.Model):
    brand_img = models.ImageField(upload_to='images/brand/')
    brand_link = models.CharField(max_length=250)


class Know_about_us(models.Model):
    img = models.ImageField(upload_to='images/about/')
    text = models.TextField()


class Images(models.Model):
    images = models.ImageField(upload_to='images/img/')


class Website_team(models.Model):
    img = models.ImageField(upload_to='images/user/img/')
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    nick_name = models.CharField(max_length=250)


class Home_Video(models.Model):
    title = models.CharField(max_length=400)
    video_link = models.CharField(max_length=500)


class Home_seasons(models.Model):
    title = models.CharField(max_length=250)


class Home_seasons_step(models.Model):
    Color = (
        ('active', 'yes'),
        ('.', 'no')
    )
    title = models.ForeignKey(Home_seasons, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    color = models.CharField(choices=Color, max_length=35)


class Big_about(models.Model):
    title = models.CharField(max_length=90)
    images_one = models.ImageField(upload_to='images/big_about/img_one/')
    images_two = models.ImageField(upload_to='images/big_about/img_two/')
    text = models.TextField()


class Klan(models.Model):
    img = models.ImageField(upload_to='images/klan/img/')
    clan_nickname = models.CharField(max_length=30)
    bio = models.TextField()
    ipaddress = models.GenericIPAddressField()


class Tournament_Lucky(models.Model):
    prize_one = models.IntegerField()
    time = models.CharField(max_length=60)
    max_man = models.CharField(max_length=60)
    prize_two = models.IntegerField()
    prize_three = models.IntegerField()

