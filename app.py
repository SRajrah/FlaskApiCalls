from flask import Flask, render_template
import urllib.request, json
import os


app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def get_movies():
    url = "https://api.themoviedb.org/3/discover/movie?api_key="
    print("***********************",url)
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    print("printing **************",dict)

    return render_template ("movies.html", movies=dict["results"])

@app.route("/movies")
def get_movies_list():
    url = "https://api.themoviedb.org/3/discover/movie?api_key="

    response = urllib.request.urlopen(url)
    movies = response.read()
    dict = json.loads(movies)

    movies = []
    for movie in dict["results"]:
        movie = {
            "title": movie["title"],
            "overview": movie["overview"],
        }
        
        movies.append(movie)

    return {"results": movies}

if __name__ == '__main__':
    app.run(debug=True)