from django.conf.urls import include, url
from django.contrib import admin


from app import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^delete_state/(?P<pk>\d+)/', 'app.views.delete_state'),
    url(r'^edit_state/(?P<pk>\d+)/' ,'app.views.edit_state'),
    url(r'^create_state/','app.views.create_state'),
    url(r'^delete_city/(?P<pk>\d+)/', 'app.views.delete_city'),
    url(r'^city_edit/(?P<pk>\d+)/', 'app.views.city_edit'),
    url(r'^create_city/', 'app.views.create_city'),
    url(r'^city_search_post/', 'app.views.city_search_post'),
    url(r'^city_search/', 'app.views.city_search'),
    url(r'^city_search_old/', 'app.views.city_search_old'),
    url(r'^list/', 'app.views.list'),
    url(r'^city_list/', 'app.views.city_list'),
    url(r'^detail/(?P<pk>\d+)/', 'app.views.detail'),
    url(r'^capital_list/', 'app.views.capital_list'),
    url(r'^capital_detail/(?P<pk>\d+)', 'app.views.capital_detail'),
    url(r'^template_view2/', 'app.views.template_view2'),
    url(r'^city_detail/(?P<pk>\d+)/', 'app.views.city_detail'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^form_view/', 'app.views.form_view'),

    url(r'^get_post/', 'app.views.get_post'),

    # url(r'^state_list/(?P<letter>\w+)/', 'app.views.state_list'),
    url(r'^first_view/(?P<starts_with>\w+)/$', 'app.views.first_view'),

    url(r'^state_list/', 'app.views.state_list'),
    url(r'^state_list_class_view/', views.StateListView.as_view()),
    url(r'^city_list_class_view/', views.CityListView.as_view()),
    url(r'^state_detail_class_view/(?P<pk>\d+)/', views.StateDetailView.as_view()),
    url(r'^city_detail_class_view/(?P<pk>\d+)/', views.CityDetailView.as_view()),
]
