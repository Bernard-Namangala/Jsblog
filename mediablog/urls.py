from django.urls import path
from.import views

urlpatterns = [
    path('',views.MediaView,name="mediahome"),
    path('(P<id>\d+)/',views.DetailPost,name="mediadetails"),
    # path('reaction/',views.reaction_post,name="reaction"),
    path('react/',views.react,name="react"),
   

]
