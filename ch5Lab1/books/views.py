from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Book, Author, Publisher


#--- TemplateView
class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context


#--- ListView
#   Book 테이블로부터 모든 레코드를 가져와 object_list라는 컨텍스트 변수를 구성한다.
#   템플렛 파일은 디폴트로 books/book_list.html 파일이 된다.
class BookList(ListView):
    model = Book


class AuthorList(ListView):
    model = Author


class PublisherList(ListView):
    model = Publisher


#--- DetailView
class BookDetail(DetailView):
    model = Book


class AuthorDetail(DetailView):
    model = Author


class PublisherDetail(DetailView):
    model = Publisher
