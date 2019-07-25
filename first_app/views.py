from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator 
from .models import Blog
from django.utils import timezone

from .forms import BlogPost

def blogpost(request):
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form' : form})
    


def create(hoho):
    blog = Blog()
    # Blog 클래스인 인스턴스를 blog란 이름으로 만들고
    blog.title = hoho.GET['title']
    # hoho 요청이 title 파라미터를 blog의 title 속성에 담고
    blog.body = hoho.GET['body']
    # body 파라미터로 날아온 건 body 속성에 담고
    blog.pub_date = timezone.datetime.now()
    # 새로 import 해온 timezone에서 현재시각 구하는 method
    blog.save()
    # save()를 해줘야 DB에도 저장
    return redirect('/blog/' + str(blog.id))
    # redirect는 괄호 안의 url주소를 가진 페이지로 가게 함
    # 새로 만든 blog란 인스턴스에 id(이 경우 pk와 같은)가 부여됐을 텐데
    # url주소는 정수가 아닌 문자열이므로 str()로 데이터 타입 변환

def new(request):
    return render(request, 'new.html')

def home(haha):
    #blogs_list = Blog.objects.all()
    blog_list = Blog.objects.get_queryset().order_by('id')
    # 이전엔 .all()을 home.html에서 사용했지만 이번엔 views.py에서 적용
    sliced = Paginator(blog_list, 3)
    #blog_list에 담은 Blog 클래스의 objecte들을 3개씩 묶기

    page_num = haha.GET.get('page')
    #
    send_this = sliced.get_page(page_num)
    #화면에 띄울 페이지를 send_this에 담기
    return render(haha, 'home.html', {'posts' : send_this})
    '''두 번째 인자를 받을 때 자동으로 templates 폴더 안을 찾아본다.
    templates 폴더 안의 blog 폴더 아래에 있었다면 'blog/home.html'을 입력했어야함 '''
    
def detail(request, abc):
    blog_detail = get_object_or_404(Blog, pk=abc)
    return render(request, 'detail.html', {'a' : blog_detail})
