# assignment4350
stack overflow webscrapper

Author: Humayra Anjum Rafi
gutHub username: Humayra98
gitHub repo: https://github.com/Humayra98/assignment4350
---------------------------------------------------------------

**App Description:**

Most hot questions and most recent questions of a particular tag T on Stack Overflow (https://stackoverflow.com) can be fetched and viewed. View questions and their related answers, comments, votes, dates. Displays the titles of the 10 newest questions and the 10 most voted questions posted in the past week related to tag T, on one page. In this way we can easily keep track of the relevant questions. In addition, we can read the full information of these questions in a convenient way. 

---------------------------------------------------------------

**Run the following commands to run the code from IDE:**

Setup environment:
pip3 install -r requirements.txt

Running in debug mode:
python app.py

Running without debugger:
python -m flask run

Browse:
http://localhost:5000/

-----------------------------------------------------------------

**Run the following commands to run the app from Docker image:**

Pull Image:
docker pull humayraanjum/swe2-assignment:latest

Running app:
docker run -p 8000:5000 assignment

Browse:
http://localhost:8000/

DockerHub repo:
[https://hub.docker.com/repository/docker/humayraanjum/swe2-assignment]

-----------------------------------------------------------------

Browser actions:

1. Type in a keyword/tag related to your search.
2. Click search.
3. Result shows a list of 10 newest and 10 highest(total 20) voted questions.
4. Clicking on each question opens a collapsible displaying the description, answers and respective comments as a thread.
5. The creation date, last edit date as well as the score/vote on each question, answer and comment is also shown.
6. The response time can be seen at the bottom of the page.
