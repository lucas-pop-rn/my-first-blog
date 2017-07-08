from django.db import models
from django.utils import timezone#ds
                            # sempre que modificar fazer makemigration e migrate
                            # models.Model significa que Post é modelo Django e deve ser salvo no BD
class Post(models.Model):                       # Define o nosso modelo
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)    # Modelo texto com limite de caracteres
    text = models.TextField()                   # Modelo textos longos
    created_date = models.DateTimeField(
            default=timezone.now)               # Modelo data e hora
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
