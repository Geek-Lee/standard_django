from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(null=True, blank=True,max_length=200)
    job = models.CharField(null=True, blank=True, max_length=200)
    def __str__(self):
        return self.name

class Article(models.Model):
    headline = models.CharField(null=True, blank=True, max_length=500)
    content = models.TextField(null=True, blank=True)
    TAG_CHOICES = (
        ('tech', 'Tech'),
        ('life', 'Life'),
    )#标签
    tag = models.CharField(null=True, blank=True, max_length=5, choices=TAG_CHOICES)#标签字段
    def __str__(self):
        return self.headline

class Comment(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    comment = models.TextField()
    belong_to = models.ForeignKey(to=Article, related_name='under_comments', null=True, blank=True)
    # 归属=模型.外键（归属于Article，从外部查询叫under_comments，没有是True，空格是True）【article.unser_comment.all】
    best_comment = models.BooleanField(default=False)
    # 默认都不是最优评论，最优评论需在admin后台中手动选择
    def __str__(self):
        return self.comment