# import flask here
from flask import Flask, render_template

# create new Flask App here
app = Flask(__name__)

# define routes for your new flask app
@app.route('/')
def index():
    return '<h1>Welcome to my flask app</h1> <p>be careful, it\'s still under construction...</p>'
2
# @app.route('/profile/<name>')
# def profile_name(name):
#     return f'<h1>Welcome to {name}\'s profile</h1>'

@app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
def profile_info(name,age,favorite_hobby,hometown):
    hometown_1 = hometown.replace('_', ' ').replace(',' , ', ')[:-2].title()
    hometown_2 = hometown[-2:].upper()
    hometown = hometown_1 + hometown_2

    name = name.title()
    age = age.title()
    favorite_hobby = favorite_hobby.title()

    #
    # return f'<h1>Welcome to {name.title()}\'s Profile</h1> <h3>About {name.title()}:</h3> <ul> <strong>Age:</strong> <li>{age.title()}</li> <strong>Favorite Hobby:</strong> <li>{favorite_hobby.title()}</li> <strong>Hometown:</strong> <li>{hometown}</li> </ul>'

    return render_template('profile.html',name=name,age=age,favorite_hobby=favorite_hobby,hometown=hometown)





@app.route('/hello-world-template')
def hello_world_template():
    return render_template('hello_world.html')



# tell your flask app to run with debug mode on
if __name__ == '__main__':
    app.run(debug=True)
