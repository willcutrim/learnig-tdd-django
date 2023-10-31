from django.db import models
from django.urls import reverse


class Entry(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'entradas'


    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('entry_detail', kwargs={'pk': self.pk})