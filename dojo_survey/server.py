from flask import Flask, render_template , session, request, redirect
app = Flask(__name__)    
app.secret_key = 'cookie'

@app.route('/')          
def index ():
    return render_template('index.html') 

@app.route('/process', methods = ['post'])
def create_user():
    print(request.form)
    session['name'] = request.form['name']  
    session['dojo_loca'] = request.form['dojo']  
    session['fav_lang'] = request.form['language']  
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def process():
    if 'name' not in session:
        return redirect('/')
    return render_template('result.html')

@app.route('/clear_session')
def clear():
    session.clear()
    return redirect('/')
    
if __name__=="__main__":    
    app.run(debug=True) 
