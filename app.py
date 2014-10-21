import os
import pyak as pk
from flask import Flask, render_template, send_from_directory, session, request, redirect, url_for
import json
import operator
# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
    SECRET_KEY = open("/dev/random","rb").read(32) 
)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/map",methods=['GET', 'POST'])
def map():
	lat=request.args.get('latitude')
	lon=request.args.get('longitude')
	if(lon==None):
		lon="-86.9241416"
	if(lat==None):
		lat="40.42569479"
	print(lat)
	location = pk.Location(lat, lon)
	#testyakker = pk.Yakker(None, location, False)
	for x in range(0, 10):
		testyakker = pk.Yakker(None, location, True)
		# id = pk.Yakker.gen_id(testyakker)
		# pk.Yakker.register_id_new(testyakker, id)
		# test2 = pk.Yakker(id, location, False)
		testyakker.downvote_yak("R/5445e3d3ef33a4d70d616f6b30d44")


	#yaklist = testyakker.get_area_tops()
	yaks_new = []
	words=[]
	for yak in testyakker.get_yaks():
	    yaks_new.append(yak.return_yak())
	yaks_top = []
	for yak in testyakker.get_area_tops():
	    yaks_top.append(yak.return_yak())
	    words += yak.return_yak().get('message').split()
	yaks_greatest =[]
	for yak in testyakker.get_greatest():
	    yaks_greatest.append(yak.return_yak())
	data= {}
	data['latitude']=lat
	data['longitude']=lon
	#print json.dumps(words)
	wordcount = {}
	for word in words:
		try:
			wordcount[word]+=1
		except Exception, e:
			wordcount[word]=1

	# d_view = [ (v,k) for k,v in wordcount.iteritems() ]
	# d_view.sort(reverse=False) # natively sort tuples by first element
	# for v,k in d_view:
	#     print "%s: %d" % (k,v)
	return render_template('map.html',yaks_new=yaks_new,yaks_top=yaks_top,yaks_greatest=yaks_greatest,data=data,words=words)

@app.route("/")
def index():
	return render_template('index.html')

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    session['latitude']="40.425694799999995"
    session['longitude']="-86.9241416"