"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
## 모든 접속 요청을 blog.urls로 전송함.

# 정규식 규칙
# ^ : 문자열이 시작할 떄
# $ : 문자열이 끝날 때
# \d : 숫자
# : 바로 앞에 나오는 항목이 계속 나올 때
# () : 패턴의 부분을 저장할 때

# ^post/ : url이(오른쪽부터) post/로 시작합니다.
# (\d+) : 숫자(한 개 이상)가 있습니다. 이 숫자로 조회하고 싶은 게시글을 찾을 수 있어요.
# / : /뒤에 문자가 있습니다.
# $ : url 마지막이 /로 끝납니다.
