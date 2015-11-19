from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from bookmanage import  views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'library.views.home', name='home'),
    # url(r'^library/', include('library.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search_form/$', views.search_form),
    url(r'^search/$',views.search),
    url(r'^search_results/$',views.Return_to_Searchresults),
    url(r'^BookDetails/(.+)/$',views.BookDetails),
    url(r'^DeleteBook/(.+)/$',views.DeleteBook),
    url(r'^UpdateBook/$',views.UpdateBook),
    url(r'^$',views.manage),
    url(r'^AddBook/$',views.AddBook),
    url(r'^AddBookSuccess/$',views.AddBookSuccess),
    url(r'^AddAuthor/$',views.AddAuthor),
    url(r'^AddAuthorSuccess/$',views.AddAuthorSuccess),
)
