from django.shortcuts import render
from .search_apk import *
from .search_exe import *
from .search_file import *
from .search_query import*


def index(request):
    data = request.POST.get('query')
    if request.POST.get('alls'):
        # Yippy search query
        search = Yippy().yippy(data)
        result = zip(
            search["urls"],
            search["title"],
            search["datetime"],
            search["decription"],
        )
        results = {"results": result}
    elif request.POST.get('image'):
        search = picSearch().search(data)['page1']
        result = zip(
            search['image'],
            search['sites'],
            search['width'],
            search['height'],
        )
        results = {"results": result}
        return render(request, 'snippets/path/image.html', results)
    elif request.POST.get('video'):
        print(request.POST.get('query'))
        print(request.POST.get('video'))
    elif request.POST.get('news'):
        print(request.POST.get('query'))
        print(request.POST.get('news'))
    elif request.POST.get('apps'):
        search = HappyMod().happymod(data)['happymod_search_apps']
        result = zip(
            search['urls'],
            search['title'],
            search['ratting'],
            search['img'],
        )
        results = {'results': result}
        return render(request, 'snippets/path/apps.html', results)
    elif request.POST.get('files'):
        search = Github_search_enggine().page1(data)['page1']
        result = zip(
            search['url_git'],
            search['url_zip'],
            search['title'],
            search['like'],
            search['lang'],
            search['update'],
        )
        results = {'results': result}
        return render(request, 'snippets/path/files.html', results)
    return render(request, "index.html", results)
