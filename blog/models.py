from django.db import models
from django.utils import timezone

# 모델을 정의하는 코드. 모델 == object(객체)
# 모델명 특수문자와 공백 제외하면 다른 이름 붙일 수 있다.
class Post(models.Model):
    author = models.ForeignKey('auth.User') # 다른 모델에 대한 링크 의미
    title = models.CharField(max_length=200) # 글자 수가 제한된 텍스트를 정의할 때 사용
    text = models.TextField() # 글자 수가 제한이 없는 긴 텍스트
    created_date = models.DateTimeField(default=timezone.now) # 날짜와 시간 의미
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self): # 메서드
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title