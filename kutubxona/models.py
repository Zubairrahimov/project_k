from django.db import models

# Create your models here.
class AuthorModel(models.Model):
    name = models.CharField(max_length=101)
    dateofbirth = models.DateField()
    status = models.BooleanField(default=False)
    description = models.TextField()
    date_of_birth = models.CharField(max_length=1000)


        
    # def __str__(self) -> str:
    #     return self.name
    

    class Meta:
        db_table = "Author"


class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    # def __str__(self) -> str:
    #     return self.title
    
    class Meta:
        db_table = 'Book'