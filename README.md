# Book Recommendation App

This is a Flask application that allows users to sign up, sign in, rate books, and receive book recommendations based on their preferences.

## Features

1. User Management
   - Sign up and sign in functionality.
   - Store user information in a dictionary.

2. Book Rating
   - Users can rate up to 5 books on a scale of 1-10.

3. Book Recommendations
   - Generate book recommendations using OpenAI's GPT API.
   - Ensure at least 5 recommended books are available on Project Gutenberg.

## Requirements

- Python 3.x
- Flask
- OpenAI Python client

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install Flask openai
   ```

3. Set your OpenAI API key in the `Project.py` file:
   ```python
   openai.api_key = 'YOUR_API_KEY'
   ```

## Running the Application

To run the application, execute the following command:
```bash
python Project.py
```

The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. Navigate to the home page.
2. Sign up or sign in with a username.
3. Rate books using the provided interface.
4. Get book recommendations based on your ratings.

## License

This project is licensed under the MIT License.
