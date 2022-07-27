from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below
@app.route('/cart')
def car-t():
    return render_template(‘cart.html’)

@app.route('/Supercool_Blazers')
def Supercool_Blazers():
    return render_template("Supercool_Blazers.html")
  
@app.route('/Air_Jordan_1_Mid')
def Air_Jordan():
    return render_template("Air_Jordan_1_Mid.html")

@app.route('/Nike_Air_Force')
def NikeAir():
    return render_template("NikeAir_Force.html")

@app.route('/home')
def index():
    return render_template("index.html")



# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
