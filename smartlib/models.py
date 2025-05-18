from django.db import models
from django.conf import settings


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f"""{self.title} — {self.author}

        {self.description}
        """
    
    def short_description(self, length=100):
        if len(self.description) > length:
            return self.description[:length] + '...'
        return self.description
    

class Note(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Текст заметки")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="notes", verbose_name="Книга")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор заметки")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заметка «{self.title}» к книге «{self.book}»"
    
    




