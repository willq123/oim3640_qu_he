# William Qu
# Lisa He

The goal of our project is to create an interactive book recommendation website that tailors recommendations based on user preferences. Users can sign in or sign up, rate books they've read, receive personalized book suggestions from ChatGPT along with links to Open Library, and compare similarities with other users. We have utilized ChatGPT for book recommendations, data storage - JSON files - for user information, and utilized Open Library API to check validity of ISBN and provide access links. The more inputs the system collects, the more accurate and engaging book recommendations it delivers. 

We have spent time to focusing on validating books through library APIs to ensure quality and accuracy, creating the platform where users input 5 books, and using JSON files to store user profiles and still have the access to the history.

## User Instructions:
1. First access the website: enter the username to sign up. If you are a new user, your username will be saved to database.
2. Input 5 books you've recently read and their ratings (1-5 scales), then the system will store them into the reading history and suggest 3 similar books
3. Using Getting recommendation option: you are able to access to the reading history, previous recommended history, and all information you have entered before, like book titles, rating, etc.
4. Getting Recommendations -> How many new books would you like to add: You can choose 1-5 new books recommended. Then enter the corresponding numbers of books you've read from the previous recommended book lists or you read before and the system will generate more books tailored to your preference and store in your account.
5. Using Similarity options: input another username to compare reading tastes and get shared-interest recommendations
6. Using Sign out option: return to the homepage and choose to continue or sign out

Relogin: enter the username to log in.
1. Using Getting recommendations option: you are able to access to the reading history, previous recommended history, and all information you have entered before, like book titles, rating, etc.
2. Getting Recommendations -> How many new books would you like to add: You can choose 1-5 new books recommended. Then enter the corresponding numbers of books you've read from the previous recommended book lists or you read before and the system will generate more books tailored to your preference and store in your account.
3. Using similarity options: input another username to compare reading tastes and get shared-interest recommendations

## FlowChart
![Flowchart](image.jpg)