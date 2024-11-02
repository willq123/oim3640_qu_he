

## The Big Idea: 
### What is the main idea of your project? What topics will you explore and what will you accomplish? Describe your minimum viable product (MVP) and your stretch goal.

- Main idea is a book recommendation website
- utilize dictionaries and GPT CPI to create a recommendation system
    - create a rudenmentary registering system
- MVP: promppt for 5 books and ratings of the books, returns 1 book recommendation based on those boooks
    - Flask for html
    - GPT API for recommendation 
    - Testing to see if the book they give is an actual book through library APIs
- Stretch Goals: Save the information based on username, remember old user's information and prompt for more book for a more taylored recommendation, allow user to see similarity between themselves and another user
    - "register" users in JSON file
    - storing user's previous book information
    - more prompts given to GPT API for more recommendations
    - either prompting GPT API for similarity or find other website/feature for this

## Learning Objectives: 
### Since this is a team project, you may want to articulate both shared and individual learning goals.

- Utilize GPT API and make sure it returns propper response format
- exploring a verity of library APIs to see which is more applicable
- creating a rudenmentary registration system that invloves prompting then storing the information elsewhere

## Implementation Plan: 
### This part may be somewhat ambiguous initially. You might have identified a library or a framework that you believe would be helpful for your project at this early stage. If you're uncertain about executing your project plan, provide a rough plan describing how you'll investigate this information further.

- Library APIs that might have the books, links to the books, or review of the book, ISBN number
- GPT API for book remmendation
- any examples of simple python registration methods online

## Project Schedule: 
### You have roughly 4-5 weeks to complete the project. Create a general timeline. Depending on your project, this could be a detailed schedule or just an overview. As the project progresses, you’ll likely need to revise this schedule.

- Week 1:
    - Test out GPT prompts to see if they could consistently produce a JSON format with the correct information
    - Look at possible Library APIs that have the information we are looking for
    - Find a way to verify if a book is an actual title (Through ISBN)
- Week 2:
    - Creating the basic recommendation system giving GPT API a prompt to verify it works
    - Try to test edge cases for prompting 
    - Start to develop the registering system
    - Start with a basic GPT API for simiarities of 2 (fake) user information
- Week 3:
    - Develop further with the registering system, using JSON files to store information
    - See if our code works on a smaller scale in python without Flask
    - Create functions for "returning" users
        - Store their previous books and prompt for any other books they have read
- Week 4:
    - Finish the registering system and test it to make sure it works
    - Create the website/HTML using Flask and testing more edge cases for both recommendation and similarity
    - Expand the MVP to ask for more books the user has read and give recommendations
        - Allow user to choose how many books to input into the system and number of recommendation books
- Week 5:
    -  Real life applications with users


## Collaboration Plan: 
### How will you collaborate with your teammates on this project? Will you divide tasks and then incorporate them separately? Will you undertake a comprehensive pair program? Explain how you'll ensure effective team collaboration. This may also entail information on any software development methodologies you anticipate using (e.g. agile development). Be sure to clarify why you've picked this specific organizational structure.

- Split the work up to even smaller pieces 
    - Work on creating a group of functions that could either be grouped or combined together
- For Prompt testing, both teamates will work on that and bring ideas together to see any insights
- we will set weekly deadlines to make we are on track
    - Communicate effectively to make sure that deliverables are being met on time
- Thsoe this the initial plan, we will try to adapt based on how sucsessful we are with both the GPT APIs and any library APIs we can find
- Both team members will look each others code to try to understand the code and see if anything is to confusing/ with comments to explain process
- We are most likely usign the waterfall organizational structure since the output and steps to get to the goal does not require too many varaince

## Risks and Limitations: 
### What do you think is the biggest risk to the success of your project?

- Procrastinating and not meeting deadlines that we set for the project
- Varied sucess with the use of the GPT API in terms of taking the output and interpretting it
- Any potential outliers for the GPT API output
- Methods of verifying the the books GPT API outputs to make sure they are both real not gibberish
    - Done mainly thorugh verifying ISBN which might be tricky as its not too intuitive for GPT API to generate
    - Using that ISBN / Book Title and verifying through Goodread or Amazon or hopefully through a library API which has more up to date books in its catalog

## Additional Course Content: 
### Are there any course topics or content you think would be helpful for your project?

- Learning more about JSON files and how to edit
- Understanding the limitations and capabilities of the GPT API
- Making sure that there are no major issues such as an infinite loop of using the GPT API till it runs out of money


