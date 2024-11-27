from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
import openai
import requests

app = Flask(__name__)

# Load user data from JSON file
def load_users():
    if os.path.exists('user.json'):
        with open('user.json', 'r') as f:
            return json.load(f)
    return {}

# Save user data to JSON file
def save_users(users):
    with open('user.json', 'w') as f:
        json.dump(users, f)

# Function to get book recommendations from OpenAI GPT
def get_book_recommendations(books_with_ratings):
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure your OpenAI API key is set in the environment
    prompt = (
        f"Based on the following books and ratings: {books_with_ratings}, "
        "recommend at most 3 books in JSON format with the following fields: "
        "title, author, and a brief description."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    recommendations = response['choices'][0]['message']['content']
    
    try:
        recommendations_json = json.loads(recommendations)
        return recommendations_json
    except json.JSONDecodeError:
        print("Error decoding JSON from recommendations:", recommendations)
        return []

# Function to check if books are available in Open Library
def check_books_in_open_library(book_titles):
    available_books = []
    for title in book_titles:
        response = requests.get(f"https://openlibrary.org/search.json?title={title}")
        data = response.json()
        if data['docs']:
            available_books.append(data['docs'][0])  # Get the first available book
    return available_books

@app.route('/')
def home():
    """Render the home screen with options for book recommendations and user search."""
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Handle user sign-up and store user information."""
    if request.method == 'POST':
        username = request.form['username']
        users = load_users()
        if username not in users:
            users[username] = {'books': []}
            save_users(users)
            return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """Handle user sign-in and retrieve user information."""
    if request.method == 'POST':
        username = request.form['username']
        users = load_users()
        if username in users:
            return redirect(url_for('recommend_books', username=username))
    return render_template('signin.html')

@app.route('/recommend_books/<username>', methods=['GET', 'POST'])
def recommend_books(username):
    """Recommend books based on user input and GPT prompts."""
    if request.method == 'POST':
        books_with_ratings = {
            request.form['book1']: request.form['rating1'],
            request.form['book2']: request.form['rating2'],
            request.form['book3']: request.form['rating3'],
            request.form['book4']: request.form['rating4'],
            request.form['book5']: request.form['rating5'],
        }
        
        # Load existing users and update the user's book list
        users = load_users()
        if username in users:
            users[username]['books'].extend(books_with_ratings.items())
            save_users(users)

        recommendations = get_book_recommendations(books_with_ratings)
        
        # Ensure recommendations is a list of dictionaries
        if isinstance(recommendations, list):
            recommended_titles = [book['title'] for book in recommendations]
        else:
            recommended_titles = []

        available_books = check_books_in_open_library(recommended_titles)
        
        return render_template('show_recommendations.html', username=username, books=available_books)
    
    return render_template('recommend_books.html', username=username)

@app.route('/show_recommendations')
def show_recommendations():
    """Display the recommended books."""
    return render_template('show_recommendations.html')

if __name__ == '__main__':
    app.run(debug=True)




## problems
# can input the same books over again and will save the books twice
# takes a long time to load
# Might output books that inputted
# might need to change from flask to website