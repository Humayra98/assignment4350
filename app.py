import flask
from flask import Flask, render_template, url_for, request, Markup
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

#get soup from url
def getSoup(link):
    url = 'https://stackoverflow.com/'+link
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

# Extract a list of dictionaries where each dictionary defines one post(question or answer), the firsts post is question, the rest are answers
def get_post_dictionary_list(link):
    soup = getSoup(link)
    allPosts = soup.find_all('div', {'class': 'post-layout'})
    dict_list = []
    i=0
    for div in allPosts:
        post_dict = {
            'body': '',
            'comments': '',
            'votes': '',
            'dates': ''
        }

        #get comments
        comments = div.findAll('span', {'class': 'comment-copy'})
        commentList = []
        for comment in comments:
           commentList.append(Markup(comment))
        post_dict['comments'] = commentList

        #get body
        body = div.find('div', attrs={'class':'s-prose js-post-body'})
        post_dict['body'] = Markup(body)

        #get votes
        votes = div.find('div', attrs={'itemprop':'upvoteCount'})
        post_dict['votes'] = votes.text

        #get edit and creation date
        dates = div.findAll('span', attrs={'class':'relativetime'})
        post_dict['dates'] = Markup(dates)
 
        dict_list.append(post_dict)
        i+=1
    return dict_list

#add routes and logic
@app.route('/',methods=['GET', 'POST'])
def index():
    masterList = []
    res_time = 0
    if(request.method == 'POST'):#if searched
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
        tag = request.form['tag']
        vote_url = f'https://stackoverflow.com/search?tab=Votes&pagesize=15&q=%5b{tag}%5d%20created%3a7d..1d' #gets info from past week
        new_url = f'https://stackoverflow.com/questions/tagged/{tag}?tab=newest&pagesize=15'
        
        start = time.process_time() #start processing timer
        vote = requests.get(vote_url, headers=headers)
        new = requests.get(new_url, headers=headers)

        voteSoup = BeautifulSoup(vote.text, 'html.parser')
        newSoup  = BeautifulSoup(new.text, 'html.parser')
        v_questions = voteSoup.find_all('div', {'class': 'question-summary'})[:10] #10 highest vote
        n_questions = newSoup.find_all('div', {'class': 'question-summary'})[:10] #10 newest

        #for newest posts
        for item in n_questions:
            title = item.find('a', {'class': 'question-hyperlink'}).text
            votes = int(item.find('span', {'class': 'vote-count-post'}).text)
            
            postLink = item.find('a', {'class': 'question-hyperlink'})['href']

            dictionaryList = get_post_dictionary_list(postLink)
            
            dictionary = {
                "title": title,
                "votes": votes,
                "created": dictionaryList[0]["dates"],
                "body": dictionaryList[0]["body"],
                "answers": dictionaryList,
                "comments": dictionaryList[0]["comments"]
            }
            masterList.append(dictionary)
        
        #for highest voted questions
        for item in v_questions:
            title = item.find('a', {'class': 'question-hyperlink'}).text
            votes = int(item.find('span', {'class': 'vote-count-post'}).text)
            
            postLink = item.find('a', {'class': 'question-hyperlink'})['href']

            dictionaryList = get_post_dictionary_list(postLink)
            
            dictionary = {
                "title": title,
                "votes": votes,
                "created": dictionaryList[0]["dates"],
                "body": dictionaryList[0]["body"],
                "answers": dictionaryList,
                "comments": dictionaryList[0]["comments"]
            }
            masterList.append(dictionary)

        end = time.process_time()
        res_time = end-start #end processing timer
        return render_template('index.html', masterList = masterList, res_time = res_time)
    else:#if not POST
        return render_template('index.html', masterList = masterList, res_time = res_time)

#for debugging
if __name__ == "__main__":
    app.run(debug=True)