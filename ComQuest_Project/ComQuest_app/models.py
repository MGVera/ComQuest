from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

# Create your models here.
class Category(models.Model):
		user = models.ForeignKey(User)
		name = models.CharField(max_length=128, unique=True)
		views = models.IntegerField(default=0)
		likes = models.IntegerField(default=0)
		slug = models.SlugField()

		def save(self, *args, **kwargs):
				self.slug = slugify(self.name)
				if self.likes < 0:
					self.likes = 0

				super(Category, self).save(*args, **kwargs)


		def __unicode__(self):
				return self.name

		class Meta:
				verbose_name_plural = "categories"


class Page(models.Model):
		category = models.ForeignKey(Category)
		user = models.ForeignKey(User)
		title = models.CharField(max_length=128)
		url = models.URLField()
		views = models.IntegerField(default=0)
		video = EmbedVideoField(blank=True)

		def __unicode__(self):
				return self.title

class UserProfile(models.Model):
		user = models.OneToOneField(User, related_name='user')
		website = models.URLField(blank=True)
		picture = models.ImageField(upload_to='profile_images', blank=True)
		bio = models.TextField(blank=True)#add


	# Override the __unicode__() method to return out something meaningful!
		def __unicode__(self):
				return self.user.username