from flask import Flask, render_template

app = Flask(__name__)

# Dashboard sebagai halaman Utama (Luar)
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Latihan 1 sebagai halaman Dalam
@app.route('/latihan1')
def latihan1():
    return render_template('latihan1.html')

@app.route('/latihan2')
def latihan2():
    return render_template('latihan2.html')

@app.route('/latihan3')
def latihan3():
    return render_template('latihan3.html')

@app.route('/latihan4')
def latihan4():
    return render_template('latihan4.html')

if __name__ == '__main__':
    app.run(debug=True)