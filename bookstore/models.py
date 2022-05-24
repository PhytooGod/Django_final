from django.db import models
from django.utils import timezone

class BookJournalBase(models.Model):
	name = models.CharField(max_length=30)
	price = models.IntegerField(default=100)
	description = models.TextField(max_length=300)
	created_at = models.DateField(default=timezone.now)

	class Meta:
		abstract = True

class Book(BookJournalBase):
	num_pages = models.IntegerField(default=500)
	genre = models.CharField(max_length=50)

	class Meta:
		verbose_name = 'Book'
		verbose_name_plural = 'Books'

	def __str__(self):
		return self.name

	def to_json(self):
		return {
			'id' : self.id,
			'name' : self.name,
			'price' : self.price,
			'description' : self.description
		}

class Journal(BookJournalBase):
	BULLET = 'BT'
	FOOD = 'FT'
	TRAVEL = "TL"
	SPORT = 'ST'

	JOURNAL_TYPE = ((BULLET, 'Bullet'), (FOOD, 'Food'), (TRAVEL, 'Travel'), (SPORT, 'Sport'))
	type = models.CharField(max_length=30, choices=JOURNAL_TYPE, default=FOOD)

	publisher = models.CharField(max_length=100)

	class Meta:
		verbose_name = 'Journal'
		verbose_name_plural = 'Journals'

	def __str__(self):
		return self.name

	def to_json(self):
		return {
			'id' : self.id,
			'name' : self.name,
			'price' : self.price,
			'description' : self.description
		}