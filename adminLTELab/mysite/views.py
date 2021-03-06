from django import apps
from django.views.generic.base import TemplateView
from django.apps import apps  # 추가


#--- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # mysite 프로젝트 하위에 있는 애플리케이션들의 리스트를 보여주기 위해 컨텍스트 변수 app_list에 담아서 템플릿 시스템에 넘겨준다.
        #context['app_list'] = ['polls','books']
        dictVerbose = {}
        for app in apps.get_app_configs():
            if 'site-packages' not in app.path:
                dictVerbose[app.label] = app.verbose_name
        context['verbose_dict'] = dictVerbose
        return context