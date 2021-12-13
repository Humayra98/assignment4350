# assignment4350
stack overflow webscrapper

Author: Humayra Anjum Rafi

email: rafiha@myumanitoba.ca

gitHub username: Humayra98

gitHub repo: https://github.com/Humayra98/assignment4350

---------------------------------------------------------------

**App Description:**

Most hot questions and most recent questions of a particular tag T on Stack Overflow (https://stackoverflow.com) can be fetched and viewed. View questions and their related answers, comments, votes, dates. Displays the titles of the 10 newest questions and the 10 most voted questions posted in the past week related to tag T, on one page. In this way we can easily keep track of the relevant questions. In addition, we can read the full information of these questions in a convenient way. 

---------------------------------------------------------------

**Run the following commands to run the code from IDE:**

Setup environment:  
`pip3 install -r requirements.txt`

Running in debug mode:  
`python app.py`

Running without debugger:  
`python -m flask run`

Browse:  
http://localhost:5000/

-----------------------------------------------------------------

**Run the following commands to run the app from Docker image:**

Pull Image:  
`docker pull humayraanjum/swe2-assignment:latest`

Running app:  
`docker run -p 8000:5000 humayraanjum/swe2-assignment`

Browse:  
http://localhost:8000/

DockerHub repo:  
[https://hub.docker.com/repository/docker/humayraanjum/swe2-assignment]

Tag: (latest)  
https://hub.docker.com/repository/registry-1.docker.io/humayraanjum/swe2-assignment/tags?page=1&ordering=last_updated

-----------------------------------------------------------------

Browser actions:

1. Type in a keyword/tag related to your search.
2. Click search.
3. Result shows a list of 10 newest and 10 highest(total 20) voted questions from past week.
4. Clicking on each question opens a collapsible displaying the description, answers and respective comments as a thread.
5. The creation date, last edit date as well as the score/vote on each question, answer and comment is also shown.
6. The response time can be seen at the bottom of the page.


-----------------------------------------------------------------

Technology:

1. Used python for backend logic
2. Flask framework
3. The main logic is in app.py
4. The html pages are in ./templates 
5. stlylesheet in ./static/css/style.css
6. Dockerfile for initiating docker image
7. requirements.txt has all required packages listed
8. Used web scrapping/crawling to retrieve info from the site directly. No use of API.

