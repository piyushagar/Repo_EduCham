from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
LABEL_CHOICES = (
    ('y', 'fa fa-youtube-play'),
    ('l', 'fa fa-lightbulb-o'),
    ('f', 'fa fa-file-text'), 
)
BUTTON_CHOICES = (
    ('s', 'Start'),
    ('p', 'Preview'),
    )
COLOR_CHOICES = (
    ('#F0F8FF', 'AliceBlue'),
    ('#FAEBD7', 'AntiqueWhite'),
    ('#00FFFF', 'Aqua'), 
    ('#343a40!important;', 'Default')
)

# Create your models here.
class Cschool(models.Model):
	
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=100, default="yours scool title", null=True, blank=True,)
	subtitle = models.CharField(max_length=100, default="yours scool subtitle", null=True, blank=True,)
	owner = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	img = models.ImageField(upload_to = "images", null=True, blank=True,)
	def __str__(self):
		return self.name

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	

class  Author(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to = "images", null=True)
	introduction = models.TextField()
	facebook = models.CharField(max_length=200, null=True, blank=True,)
	twitter = models.CharField(max_length=200, null=True, blank=True,)
	linkedin = models.CharField(max_length=200, null=True, blank=True,)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(upload_to = "images", null=True, blank=True)
	subtitle = models.CharField(max_length=100, null=True, blank=True,)
	author = models.OneToOneField(Author, null=True, blank=True, on_delete=models.CASCADE)
	discription = models.TextField(null=True, blank=True,)
	cr_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		
		return url

	@property
	def leasons(self):
		return self.leason_set.all()
	
	

class Order(models.Model):
	customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems ])
		return total

	# @property
	# def get_cart_items(self):
	# 	orderitems = self.orderitem_set.all()
	# 	total = sum([item for item in orderitems ])
	# 	return total
	
class OrderItem(models.Model):
	product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	# quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price
		return total
	


class Leason(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=200, unique=True, null=True)
	label = models.CharField(choices=LABEL_CHOICES, max_length=1, default="y")
	button = models.CharField(choices=BUTTON_CHOICES, max_length=1, default="s")
	cr_date = models.DateTimeField(auto_now_add=True)
	video= models.FileField(upload_to = "images", null=True, blank=True)
	product = models.ForeignKey('student.Product', null=True, blank=True, on_delete=models.SET_NULL)
	content = models.TextField(null="True", blank="True")
	
	

	def __str__(self):
		return self.title

class Comment(models.Model):
    leason = models.ForeignKey(Leason,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return 'Comment {} by {}'.format(self.leason.title, self.user.username)


class Faq(models.Model):
	question = models.CharField(max_length=200)
	ans = models.TextField()

	def __str__(self):
		return self.question

class Customize(models.Model):
	navbar = ColorField(default="#FF0000")
	footer = ColorField(default="#FF0000")
	homepageimage = models.ImageField(upload_to = "images", null=True, blank=True)
	logo = models.ImageField(upload_to = "images", null=True, blank=True)
	favicon = models.ImageField(upload_to = "images", null=True, blank=True)


	def __str__(self):
		return self.navbar
	
class ShippingAddress(models.Model):
	customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address