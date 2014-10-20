import os
import pyak as pk
from flask import Flask, render_template, send_from_directory
import json
# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/listing")
def listing():
	location = pk.Location(40.423705, -86.921195)
	testyakker = pk.Yakker(None, location, False)
	#yaklist = testyakker.get_area_tops()
	yaks_new = []
	for yak in testyakker.get_yaks():
	    yaks_new.append(yak.return_yak())
	yaks_top = []
	for yak in testyakker.get_area_tops():
	    yaks_top.append(yak.return_yak())
	yaks_greatest =[]
	for yak in testyakker.get_greatest():
	    yaks_greatest.append(yak.return_yak())
	return render_template('listing.html',yaks_new=yaks_new,yaks_top=yaks_top,yaks_greatest=yaks_greatest)

@app.route("/")
def index():
	return render_template('index.html')

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)