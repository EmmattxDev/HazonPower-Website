from django_hosts import patterns, host
from django.conf import settings



host_patterns = patterns('',
                    host(r'www', settings.ROOT_URLCONF, name='www'),
                    # host(r'blog', 'blog.urls', name='blog'),
                    # Admin subdomain
                    host(r'admin', 'backend.admin_urls', name='admin'),
                )