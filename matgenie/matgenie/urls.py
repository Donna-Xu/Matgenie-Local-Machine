from django.urls import include, path
from . import views

urlpatterns = [
    path('index/', views.index, name='main-view'),
    path('rest/convert', views.convert_files, name='convert_files'),
    path('rest/symmetry', views.analyze_symmetry, name='analyze_symmetry'),
    path('rest/xrd', views.calculate_xrd, name='calculate_xrd'),
    path('rest/surfaces', views.generate_surfaces, name='generate_surfaces'),
    path('rest/compare', views.compare_structures, name='compare_structures'),
]

