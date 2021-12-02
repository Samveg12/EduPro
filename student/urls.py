from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index,name="student"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout_u, name="logout_u"),
    path('product/<int:id>', views.Revieww.updaterating, name="updaterating"),
    # path('payment',views.paymenthandler,name="paymenthandler"),
    path('product/paymenthandler/<int:id>',views.paymenthandler,name="paymenthandler"),
    path('paymenthandler/<int:id>',views.paymenthandler,name="paymenthandler"),
    path('bookings',views.bookings,name="bookings"),
    path('review/<int:id>',views.createReview,name="createReview"),
    path('updatereview/<int:pk>',views.updates.as_view()),
    path('deletereview/<int:pk>',views.deletes.as_view()),
    path('chooseslot/<int:id>',views.chooseslot,name="as_view()"),
    path('updateratingreview',views.Revieww.updatereview,name="views.Review.updatereview"),
    path('event',views.meet,name="event")




    
]