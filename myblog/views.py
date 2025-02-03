from django.shortcuts import render, redirect
from article.models import ArticlePost

def show(request):
    # get articles to render
    articles = []
    filter_titles = [
        '研究生学习计划2022-2025',
        '算法题型总结',
        '算法模板',
        'bitcoin入门',
        '菜谱'
    ]
    articles = ArticlePost.objects.none()
    for t in filter_titles:
        articles = articles | ArticlePost.objects.filter(title=t)

    # get tools to render
    tools = [
        {'icon': "https://www.cainiaojc.com/favicon.ico", 'name': "C run", 'url': "https://www.cainiaojc.com/tool/c/"},
        {'icon': "https://www.cainiaojc.com/favicon.ico", 'name': "C++ run", 'url': "https://www.cainiaojc.com/tool/cpp/"},
        {'icon': "https://www.cainiaojc.com/favicon.ico", 'name': "py run", 'url': "https://www.cainiaojc.com/tool/python3/"},
        # {'icon': "https://www.aigei.com/favicon.ico", 'name': "爱给网", 'url': "https://www.aigei.com"},
        # {'icon': "https://app.diagrams.net/favicon.ico", 'name': "流程图", 'url': "https://www.cainiaojc.com/tool/c/"},
        {'icon': "https://static.deepl.com/img/logo/DeepL_Logo_darkBlue_v2.svg", 'name': "DeepL", 'url': "https://www.deepl.com/translator"},
        # {'icon': "https://shared-https.ydstatic.com/images/favicon.ico", 'name': "有道翻译", 'url': "https://fanyi.youdao.com"},
        # {'icon': "https://getemoji.com/favicon.ico", 'name': "emoji", 'url': "https://getemoji.com"},
        {'icon': "https://m.media-amazon.com/images/I/41da3NERJ4L.png", 'name': "ToDo", 'url': "http://101.35.183.71:10000/todo/show/"},
        {'icon': "https://github.githubassets.com/assets/apple-touch-icon-144x144-b882e354c005.png", 'name': "GitHub", 'url': "https://www.github.com"},
        {'icon': "https://file.ipadown.com/tophub/assets/images/favicon/ms-icon-144x144.png", 'name': "今日热榜", 'url': "https://tophub.today/"},
        {'icon': "https://cncdn.dida365.com/static/img/favicon.ico", 'name': "滴答清单", 'url': "https://dida365.com/webapp"},
        {'icon': "https://www.qmjianli.com/favicon.ico", 'name': "全民简历", 'url': "https://www.qmjianli.com/my/cv"},
        {'icon': "https://cdn.oaistatic.com/_next/static/media/apple-touch-icon.82af6fe1.png", 'name': "ChatGPT", 'url': "https://chat.openai.com/chat"},
        {'icon': "https://statics.moonshot.cn/kimi-chat/favicon.ico", 'name': "Kimi Chat", 'url': "https://kimi.moonshot.cn/"},
        {'icon': "https://scholar.google.com/favicon.ico", 'name': "Google Scholar", 'url': "https://scholar.google.com"}
        # {'icon': "https://www.chatpdf.com/favicon.ico", 'name': "ChatPDF", 'url': "https://www.chatpdf.com/"},
        # {'icon': "https://file.ipadown.com/tophub/assets/images/logo.png", 'name': "新闻聚合", 'url': "https://tophub.today/"}
        # {'icon': "https://www.zju.edu.cn/_upload/article/images/98/48/66593c0c4487972f8c5c36c5df97/05381ac0-bd09-4d39-acc7-86f64fc1f5dd.png", 'name': "webvpn", 'url': "https://webvpn.zju.edu.cn/portal/#!/login"}
    ]
    context = {
        'articles': articles,
        'tools': tools,
    }
    return render(request, 'home.html', context)
