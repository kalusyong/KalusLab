import sae
from kalusbook import wsgi

application = sae.create_wsgi_app(wsgi.application)