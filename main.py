# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample movie data and collaborative recommendation method
movies = [
    'The Dark Knight', 'Inception', 'Die Hard', 'Mad Max: Fury Road',
    'Anchorman', 'Superbad', 'Bridesmaids', 'Dumb and Dumber',
    'The Shawshank Redemption', 'Forrest Gump', 'The Godfather', 'Schindler\'s List'
    # Add more movies as needed
]

def collaborative_recommendation(user_input):
    # Replace this with your actual collaborative recommendation logic
    # For simplicity, just return a subset of movies
    return movies[:8]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['movie']

    # Call the collaborative recommendation method
    recommended_movies = collaborative_recommendation(user_input)

    # Return the result as JSON
    return jsonify({'movies': recommended_movies})

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', debug=True, port=12000)
