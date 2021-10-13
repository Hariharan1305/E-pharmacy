from django.urls import path

from . import views
urlpatterns=[
    path('',views.ao,name="ao"),
    path('vo/',views.vo,name="vo"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.destroy,name="delete"),

    path('favdelete/<int:id>',views.wishdelete,name="favdelete"),
    path('favorite_album/<int:id>', views.favorite_project, name='favorite_project'),
    path('favorite_remove/<int:id>',views.favorite_remove,name="favoriteremove"),
    path('favorite/',views.favorite,name="fav"),

    path('add_to_cart_album', views.addtocart, name='addcart'),
    path('add_to_cart_buy', views.addtocartbuy, name='addcartbuy'),

    path('add_to_remove/<int:id>', views.removetocart, name='removecart'),
    path('orderdetails/', views.orderdetails, name='order'),
    path('add_to_cart_buy/quty/', views.changequty, name='ajaxfoo'),
    path('wishlist_album', views.addwishlist, name='addwishcart'),
]
