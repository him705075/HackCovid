from flask import Flask, render_template, request
import pickle


app = Flask(__name__, template_folder='templates')
# open a file, where you stored the pickled data
file = open('model.pkl' , 'rb')
clf = pickle.load(file)
file.close()


@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/breathe')
def breathe():
    return render_template('breathe.html')


@app.route('/dos')
def dos():
    return render_template('dos.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/show')
def show():
    return render_template('show.html')

@app.route('/donation')
def donation():
    return render_template('donation.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/yoga')
def yoga():
    return render_template('yoga.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


@app.route('/accountconfig')
def accountconfig():
    return render_template('accountconfig.html')

@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        myDict = request.form
        fever = float(myDict["fever"])
        age = int(myDict["age"])
        pain = int(myDict["pain"])
        runnyNose = int(myDict["runnyNose"])
        diffBreath = int(myDict["diffBreath"])
        # Code for inference
        inputFeatures = [fever, pain, age, runnyNose, diffBreath]
        infProb = clf.predict_proba([inputFeatures])[0][1]
        print(infProb)
    
        return render_template('show.html' , inf=round(infProb*100))
    return render_template('show.html')

@app.route("/about_us")
def about_us():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)