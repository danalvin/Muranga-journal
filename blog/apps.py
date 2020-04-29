from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class BlogConfig(AppConfig):
    
    # Short name for the application, used to get attributes
    label = 'Blog'                                        

    # Name for the application to be included in INSTALLED_APPS
    name = 'blog'                                        

    # App name for the Administration Site
    verbose_name  = "Django Blog"
    
    # Application settings 
    pagination          = 5                                             # Pagination elements