from flask import render_template, request, Blueprint
from webui.main.forms import AddStartStopForm
# from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')


@main.route("/timepoint/new", methods=['GET', 'POST'])
def new_time():
    form = AddStartStopForm()
    return render_template('time_point_new.html', title= "New Time point", form=form)

@main.route("/about")
def about():
    return render_template('about.html', title='About')