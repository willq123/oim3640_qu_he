from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import json
import os
import openai
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

openai.api_key = os.getenv("OPENAI_API_KEY")  

# Load user data from JSON file
def load_users():
    if os.path.exists('user.json'):
        with open('user.json', 'r') as f:
            return json.load(f)
    return {}

# Save user data to JSON file
def save_users(users):
    with open('user.json', 'w') as f:
        json.dump(users, f, indent=4)

def get_book_recommendations(books_with_ratings, read_books):
    """
    Uses Chat GPT API to generate book recommendations with the following parameters:
        1. Books and Ratings
        2. Previous (if there are) Books and Ratings from user.json
    """
    prompt = (
        f"Based on the following books and ratings: {books_with_ratings}, "
        f"and excluding the books the user has already read: {read_books}, "
        "recommend 3 new books in JSON format with the following structure: "
        "{'Book title': 'title', 'Author': 'author name'}. Response in JSON format and no additional text."
    )
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        
        recommendations = response['choices'][0]['message']['content']
        
        try:
            recommendations_json = json.loads(recommendations)
            return recommendations_json
        except json.JSONDecodeError as e:
            return render_template('error.html', error=str(e))
    except Exception as e:
        return render_template('error.html', error=str(e))

def check_books_in_open_library(book_title):
    """
    Check with Open Library API if the book is real by verifying the title and author.
    If it does not exist, it will return FALSE.
    If it does exist, it will return the ISBN.
    """
    response = requests.get(f"https://openlibrary.org/search.json?title={book_title}")
    if response.status_code == 200:
        data = response.json()
        if data['numFound'] > 0:
            return data['docs'][0]['isbn'][0] if 'isbn' in data['docs'][0] else False
    return False

@app.route('/')
def index():
    """
    Welcomes the user and prompts them to sign up or sign in.
    If 'sign in button' is pressed, it directs them towards '/signin'
    If 'sign up button' is pressed, it directs them towards '/signup'
    """
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Prompts user for username and saves it to user.json
    Checks if the username already exists within user.json, if it does, it will redirect them back to '/signup' and display a message, "Username already exists"
    After signing up, it will direct them after to '/recommend_books/<username>' and prompt them for 5 books
    """
    if request.method == 'POST':
        username = request.form['username']
        users = load_users()
        if username in users:
            flash("Username already exists", "error")
            return redirect(url_for('signup'))
        users[username] = {"books": [], "recommended_books": []}  # Initialize with proper structure
        save_users(users)
        return redirect(url_for('recommend_books', username=username))
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """
    Prompts user for username and checks if it exists within user.json
    If it does not exist, it will redirect them back to '/signin' and display a message, "Username does not exist"
    After signing in, it will direct them after to '/homepage/<username>'
    """
    if request.method == 'POST':
        username = request.form['username']
        users = load_users()
        if username not in users:
            flash("Username does not exist", "error")
            return redirect(url_for('signin'))
        return redirect(url_for('homepage', username=username))
    return render_template('signin.html')

@app.route('/recommend_books/<username>', methods=['GET', 'POST'])
def recommend_books(username):
    """
    Takes in variable "n" (default is 5), which is the number of books to prompt the user for
    Each entry will be a book title and a rating (1-10)
    Each entry will on their own line
    When submitted, it will first save the books and ratings to user.json and then direct them to '/show_recommendations/<username>'
    """
    n = request.args.get('n', default=5, type=int)  # Get n from query parameters
    if request.method == 'POST':
        books_with_ratings = request.form.getlist('books')  # Expecting a list of books and ratings
        users = load_users()
        if "books" in users[username]:
            users[username]["books"].extend(books_with_ratings)  # Add books to user's list
        else:
            users[username]["books"] = books_with_ratings
        save_users(users)
        return redirect(url_for('show_recommendations', username=username))
    return render_template('recommend_books.html', username=username, n=n)

@app.route('/show_recommendations/<username>', methods=['GET', 'POST'])
def show_recommendations(username):
    """
    Based on the books and ratings inputted and the books the user has already read, it will generate 3 recommendations for the user
    Uses get_book_recommendations function to generate recommendations, and verifies with check_books_in_open_library function
    If there are no recommendations, it will repeat the process one more time
    If there are no recommendations after the 2nd time, displays the message "No recommendations available at this time."
    There will be a button to return to '/homepage/<username>'
    """
    users = load_users()
    read_books = users[username]["books"]
    recommendations = get_book_recommendations(read_books, read_books)
    if not recommendations:
        return render_template('show_recommendations.html', username=username, message="No recommendations available at this time.")
    return render_template('show_recommendations.html', username=username, recommendations=recommendations)

@app.route('/homepage/<username>', methods=['GET', 'POST'])
def homepage(username):
    """
    There will be a button to go to '/more_recommendations/<username>' called "Another Recommendation"
    There will be a button to go to '/similarity/<username>' called "Similarity"
    There will be a button to sign out which will direct them to '/'
    """
    return render_template('homepage.html', username=username)

@app.route('/more_recommendations/<username>', methods=['GET', 'POST'])
def more_recommendations(username):
    """
    Prompts user for number of new books to input
    Directs them towards '/recommend_books/<username>' with n being the number of new books
    """
    if request.method == 'POST':
        n = int(request.form['num_books'])
        return redirect(url_for('recommend_books', username=username, n=n))  # Pass n as a query parameter
    return render_template('more_recommendations.html', username=username)

@app.route('/similarity/<username>', methods=['GET', 'POST'])
def similarity(username):
    """
    Prompt user for another user within the database
    After submitting, it will direct them to '/user_similarity/<username>/<other_username>'
    """
    return render_template('similarity.html', username=username)

@app.route('/user_similarity/<username>', methods=['GET', 'POST'])
def user_similarity(username):
    """
    Take both username data and input into GPT API and display % similarity and 1 book recommendation
    Book recommendation will be verified with check_books_in_open_library function
    If there are no recommendations, it will repeat the process one more time
    After the second time, it will display "No recommendations available at this time."
    There will be a button to return to '/homepage/<username>'
    """
    return render_template('user_similarity.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
