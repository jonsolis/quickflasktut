
from flask import Flask, render_template
 
app = Flask(__name__)

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
	app.run()

