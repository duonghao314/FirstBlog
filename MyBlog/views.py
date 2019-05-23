from django.shortcuts import render
from MyBlog.models import Category,Article
# Create your views here.



def index(request):
    # Cats = {'Categories':Category.objects.all()}
    # Arts = {'NewestArticles' : Article.objects.order_by('id')[:2]}
    return render(request, 'blog/index.html',
                  {'cats': Category.objects.all(),'arts': Article.objects.order_by('-id')[:4],'catsRanked': Category.objects.order_by('-catViews')})
def cat(request, catName):
    try:
        catID = Category.objects.get(catKey=catName).id
        #print(catID)
    except BaseException as be:
        print(be.__str__())
       #, 'arts': Article.objects.get(catID= catID)
    try:
        artByCat = Article.objects.filter(artCatID=catID)
        #print(artByCat)
    except BaseException as be:
        print(be.__str__())

    return render(request, 'blog/category.html',{'cats': Category.objects.all(),'arts':artByCat})
def art(request, artID):
    try:
        getArt=Article.objects.get(id=artID)
        getArt.artView = getArt.artView + 1
        artCatID = getArt.artCatID
        getArt.save()
        print(artCatID)
        getCat = Category.objects.get(catName=artCatID)
        print(getCat.catViews)
        getCat.catViews = getCat.catViews + 1
        getCat.save()
    except BaseException as be:
        print(be.__str__())
    try:
        art=  Article.objects.get(id=artID)
        #print(art)
    except BaseException as be:
        print(be.__str__())
    return render(request,'blog/post.html',{'cats': Category.objects.all(), 'art': art})