from django.db import models

# Create your models here.

class Material(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog_previews/', verbose_name='изображение')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'