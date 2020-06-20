from django.db import models

# Criando a classe que ira comportar os campos que tera no banco de dados

class Task(models.Model):

    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices = STATUS,
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    