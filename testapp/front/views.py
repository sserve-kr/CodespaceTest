from django.http import HttpResponse
# 기존의 render import는 이 프로젝트에서 사용하지 않을 것이기 때문에 제거했다.

def index(request):
  return HttpResponse('Hello World!')