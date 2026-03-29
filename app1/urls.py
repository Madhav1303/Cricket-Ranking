
from django.urls import path,include
from .views  import  player_rankings_odi_view,player_rankings_test_view,player_rankings_t20_view,add_player_view,player_list_view,delete_player_view,update_player_view

urlpatterns = [
    #path('', PlayerView.as_view(), name='player'),
    #path('delete/<int:id>/', PlayerView.as_view(), name='player_detail'),
    #path('testrankings',PlayerListSortedView_test.as_view(),name ='test_rankings'),
    #path('odirankings',PlayerListSortedView_odi.as_view(),name ='odi_rankings'),
    #path('t20rankings',PlayerListSortedView_t20.as_view(),name ='t20_rankings'),

    #frontend
    path('players-list/', player_list_view, name='players_list'),
    path('add/', add_player_view, name='add_player'),
    path('odirankings/', player_rankings_odi_view, name='odi_rankings'),
    path('testrankings/', player_rankings_test_view, name='test_rankings'),
    path('t20rankings/', player_rankings_t20_view, name='t20_rankings'),
    #path('view/<int:id>/', view_player_view, name='view_player'),
    path('delete/<int:id>/', delete_player_view, name='delete_player'),
    path('update/<int:pk>/',update_player_view,name ='update_player'),

]
