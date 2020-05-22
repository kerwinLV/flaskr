from flask import (
    Blueprint,flash,g,redirect,render_template,request,url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

blog_bp=Blueprint('blog',__name__)