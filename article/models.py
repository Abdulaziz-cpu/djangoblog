from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):       
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE,verbose_name="İstifadəçi adı")#vorbose_name default ingisilce ad yox dirnaq icinde yazdigimiz sozun cixmasi ucundur
    title = models.CharField(max_length= 50,verbose_name="Başlıq")
    content = RichTextField(verbose_name="Mətn")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yaranma Tarixi")
    article_image = models.FileField(blank=True,null=True,verbose_name="Məqaləyə Şəkil yükləyin")
    def __str__(self):
        return self.title #bu kod bizim cedvelimizde title'da basanda article'mizin acilmagina komek edir
    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Məqalə",related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="Ad")
    comment_content = models.CharField(max_length=200,verbose_name="Şərh")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']

