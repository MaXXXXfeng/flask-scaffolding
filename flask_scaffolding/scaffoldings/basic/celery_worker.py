from proj import create_app
from proj.extensions import celery

app = create_app()
app.app_context().push()

