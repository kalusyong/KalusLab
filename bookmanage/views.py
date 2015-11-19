import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.shortcuts import render_to_response
from bookmanage.models import Book, Author
#此处添加
def search_form(request):
    return render_to_response('search_form.html')

def manage(request):
    return render_to_response('manage.html')

def Return_to_Searchresults(request):
    return render_to_response('search_results.html')

def AddBook(request):
    return render_to_response('AddBook.html')


def AddAuthor(request):
    return render_to_response('AddAuthor.html')

def AddAuthorSuccess(request):
    if request.POST:
        author = Author()
        author = Author(AuthorID = request.POST["AuthorID"],
                        name = request.POST["name"],
                        age = request.POST["age"],
                        Country = request.POST["Country"])
        author.save()
        return render_to_response('AddAuthorSuccess.html',{'Name':author.name})
    else:
        return render_to_response('AddAuthor.html')

def search(request):
    errors = []
    if 'AuthorName' in request.GET and request.GET['AuthorName']:
        q = request.GET['AuthorName']
        if not q:
            errors.append('输入不可为空')
        elif len(q) > 20:
            errors.append('输入数据过长，请保证输入数据长度少于20')
        else:
            author = Author.objects.filter(name=q)
            if author :

                book = Book.objects.filter(AuthorID=author[0].AuthorID)
                if book:
                    return render_to_response('search_results.html',{'authors':author[0],'books': book, 'query': q})
                else:
                    errors.append('您查询的作者没有书籍被录入')
            else:
                errors.append('查询的作者不存在')
    return render_to_response('search_form.html',{'errors':errors})

def AddBookSuccess(request):
    book = Book()
    if request.POST:
        try:
            book.ISBN = request.POST["ISBN"]
            book.Title = request.POST['Title']
            book.AuthorID = request.POST['AuthorID']
            book.Publisher = request.POST['Publisher']
            book.PublicationDate = request.POST['PublicationDate']
            book.price = request.POST['price']
            book.save()
            return render_to_response('AddBookSuccess.html',{'book':book})
        except Author.DoesNotExist:
            return render_to_response('AuthorNotExist.html')
    else:
        return render_to_response('AddBook.html')

def BookDetails(request,bookName):
    book = Book.objects.filter(Title__icontains=bookName)
    authors = Author.objects.filter(AuthorID__icontains = book[0].AuthorID)
    return render_to_response('BookDetails.html', {'books':book[0],'author':authors[0]})

def DeleteBook(request,bookName):
    books = Book.objects.filter(Title__icontains=bookName)
    booktemp = books[0]
    books[0].delete()
    return render_to_response('DeleteBook.html',{'book':booktemp})

def UpdateBook(request):
    ISBN = request.GET['ISBN']
    if request.method=='POST':
        book = Book.objects.filter(ISBN__icontains=ISBN)
        booktemp = book[0].AuthorID
        book.update(ISBN = request.POST['ISBN'],
                    Title = request.POST['Title'],
                    AuthorID = request.POST['AuthorID'],
                    Publisher = request.POST['Publisher'],
                    PublicationDate = request.POST['PublicationDate'],
                    price = request.POST['price'],)
        author = Author.objects.filter(AuthorID=booktemp)
        author.update(name = request.POST['name'],
                      age = request.POST['age'],
                      Country = request.POST['Country'],)
        return render_to_response('UpdateBookSuccess.html')
    books=Book.objects.filter(ISBN=ISBN)
    author=Author.objects.filter(AuthorID=books[0].AuthorID)
    return render_to_response('UpdateBook.html',{'book':books,'author':author})
