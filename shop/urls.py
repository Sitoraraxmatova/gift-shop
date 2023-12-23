from django.urls import path
from.views import home_page, contact, shop, why, testimonial

app_name='shopapp'
urlpatterns=[
    path('',home_page),
    path('contact/',contact,name="contact"),
    path('shop/',shop,name="shop"),
    path('testimonial/',testimonial,name="testimonial"),
    path('why/',why, name="why")



]