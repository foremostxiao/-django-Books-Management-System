from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from app01.models import Book,Publisher,Author
from app01 import models

#主页
def index(request):
    return render(request,"index.html")

#添加书籍
def addbook(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        price = request.POST.get('price')
        # 出版社
        publish_id = request.POST.get("publish_id")
        publish_date = request.POST.get("pub_date")
        authors_id_list = request.POST.getlist('authors_id_list')
        if title == '' or price == '' or  publish_date == '' or publish_id == '' or authors_id_list == '':
            return HttpResponse('<h3 style="color: #c7254e">所有选项不为空</h3>')

        book_obj=Book.objects.create(title=title,price=price,publish_date=publish_date,publisher_id=publish_id)
        # new_book = models.Book.objects.get(title=title)
        book_obj.authors.set(authors_id_list)
        return redirect("/book/")
    pub_list = models.Publisher.objects.all()
    author_list = models.Author.objects.all()
    return render(request, "addbook.html", {"pub_list": pub_list, "author_list": author_list})

#查看图书
def book(request):
    book_list = Book.objects.all()
    return render(request, "book.html", {"book_list":book_list})
#删除书籍
def delbook(request,id):
    book_obj = models.Book.objects.filter(pk=id).first()
    book_obj.delete()
    return redirect("/book/")
#编辑书籍
def editbook(request,id):

    #---------------------------------
    book_obj = Book.objects.filter(pk=id).first()
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get('price')
        publish_date = request.POST.get("pub_date")
        publish_id = request.POST.get('publish_id')
        authors_id_list = request.POST.getlist('authors_id_list')

        Book.objects.filter(pk=id).update(title=title, publish_date=publish_date,price=price, publisher_id=publish_id)
        book_obj.authors.set(authors_id_list)
        return redirect("/book/")
    pub_list = Publisher.objects.all()
    author_list = Author.objects.all()
    return render(request,"editbook.html",{"book_obj":book_obj,"pub_list": pub_list, "author_list": author_list})



#查看出版社
def publisher(request):
    publisher_list = models.Publisher.objects.all()
    return render(request, "publisher.html",{"publisher_list":publisher_list} )

def pub_is_valid(xname):
    """验证出版社信息"""
    if models.Publisher.objects.filter(pname=xname).count() != 0:
        return {"status": "该出版社已存在！"}
#增加出版社
def addpublisher(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        city = request.POST.get("city")
        email = request.POST.get("email")
        # ret = pub_is_valid(pname)
        # # print(ret)
        # if ret:
        #     ret["pname"] = pname
        #     return render(request,"addpublisher.html",ret)
        # else:

        models.Publisher.objects.create(name=name,city=city,email=email)
        return redirect("/publisher/")
    return render(request, "addpublisher.html")

#编辑出版社
def editpublisher(request,id):

    pub_obj = models.Publisher.objects.filter(pk=id).first()
    if request.method == "POST":
        name = request.POST.get("name")
        city = request.POST.get("city")
        email = request.POST.get("email")

        models.Publisher.objects.filter(pk=id).update(name=name,city=city,email=email)
        return redirect("/publisher/")
    return render(request, "editpublisher.html", {"pub_obj":pub_obj})

#删除出版社
def delpublisher(request,id):
    publisher_obj = models.Publisher.objects.filter(pk=id).first()
    publisher_obj.delete()
    return redirect("/publisher/")

#出版社关联书籍
def publisher_book(request,id):
    print('111111111111')
    pub_obj = models.Publisher.objects.filter(pk=id).first()
    book_list = pub_obj.book_set.all()

    return render(request, 'publisher_book.html',{'book_list':book_list})

#查看作者
def author(request):
    author_list = models.Author.objects.all()
    return render(request, "author.html", {"author_list":author_list})

def addauthor(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        age = request.POST.get("age")

        # ret = author_is_valid(name)
        # if ret:
        #     ret["name"] = name
        #     return render(request,"addauthor.html",ret)
        # else:
        models.Author.objects.create(name=name,age=age)
        return redirect("/author/")

    return render(request, "addauthor.html")

def delauthor(request,id):
    author_obj = models.Author.objects.filter(id=id).first()
    author_obj.delete()
    return redirect("/author/")

# 编辑作者
def editauthor(request,id):

    author_obj = models.Author.objects.filter(id=id).first()
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get('age')
        # ret = author_is_valid(aname)
        # if ret:
        #     author_obj.aname = aname
        #     ret["author_obj"] = author_obj
        #     return render(request,"editauthor.html",ret)
        # else:
        models.Author.objects.filter(id=id).update(name=name,age=age)
        return redirect("/author/")
    return render(request,"editauthor.html",{"author_obj":author_obj})

#作者关联书籍；多对多
def author_book(request,id):
    author_obj = models.Author.objects.filter(pk=id).first()
    # 反向查询表名小写——set.all()
    book_list = author_obj.book_set.all()
    return render(request, "author_book.html",{'book_list':book_list})