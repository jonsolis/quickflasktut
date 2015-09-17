from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy

from wtforms import fields, widgets

import flask_admin as admin
#from flask_admin.contrib import sqla

# Create application 
app = Flask(__name__)

# Create dummy secret key so we can use sessions
app.config['SECRET_KEY'] = '1234567890'

# Create in-memory database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample_db.sqlite'
app.config['SQLALCHEMY_ECHO'] = True
#db = SQLAlchemy(app)

''' Define a wtforms widget and field.
    WTForms documentation on custom widgets:
    http://wtforms.readthedocs.org/en/latest/widgets.html#custom-widgets
'''
class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        # add WYSIWYG class to existing classes
        existing_classes = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class'] = u'%s %s' % (existing_classes, "ckeditor")
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()


# Model
#class Page(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.Unicode(64))
#    text = db.Column(db.UnicodeText)

#    def __unicode__(self):
#        return self.name


# Customized admin interface
#class PageAdmin(sqla.ModelView):
#    form_overrides = dict(text=CKTextAreaField)

#    create_template = 'create.html'
#    edit_template = 'edit.html'



# Flask views
@app.route('/admin/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'





@app.route('/')
def homepage():

    title = "Epic Tutorials"
    paragraph = ["wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!","wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!"]

    try:
        return render_template("index.html", title = title, paragraph=paragraph)
    except Exception, e:
        return str(e)

@app.route('/about')
def aboutpage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("about.html", title=title, paragraph=paragraph, pageType=pageType)


@app.route('/about/contact')
def contactPage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("index.html", title=title, paragraph=paragraph, pageType=pageType)

@app.route('/graph')
def graph_Example(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
        subtitleText = {"text": 'finally a subtitle'}
	#topPairs, bottomPairs = datafunctions.twoPaneGraphData('btceHistory',1, 3, 4)
        dataSet = [[1408395614.0, 430.2], [1408395614.0, 431.13], [1408395617.0, 431.354], [1408395623.0, 432.349], [1408395623.0, 432.017], [1408395640.0, 430.195], [1408395640.0, 430.913], [1408395640.0, 430.913], [1408395647.0, 430.211], [1408395647.0, 430.297], [1408395647.0, 430.913], [1408395648.0, 432.996], [1408395648.0, 432.996], [1408395648.0, 432.349], [1408395654.0, 431.0]]
        pageType = 'graph'
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, "zoomType":'x'}
	series = [{"name": 'Label1', "data": dataSet}]
	graphtitle = {"text": 'interesting numbers WOW'}
	xAxis = {"type":"datetime"}
	yAxis = {"title": {"text": 'yAxis Label'}}
	return render_template('graph.html',pageType=pageType,subtitleText=subtitleText, chartID=chartID, chart=chart, series=series, graphtitle=graphtitle, xAxis=xAxis, yAxis=yAxis)




@app.route('/wysiwyg/')
def thefinalcountdown():

    title = "you got this bro"
    paragraph = ["ezpzaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzz"]

    pageType = 'about'

    return render_template("wysiwyg.html", title=title, paragraph=paragraph, pageType=pageType)




if __name__ == "__main__":
	# Create admin
	admin = admin.Admin(app, name="Example: Wysiwyg")

	# Add views
	admin.add_view(PageAdmin(Page, db.session))

	# Create DB
	db.create_all()
	
	# Start app
	app.run(debug=True)

