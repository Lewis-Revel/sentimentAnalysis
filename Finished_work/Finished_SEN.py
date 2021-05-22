
import praw
import csv
import itertools
from praw.models import MoreComments
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import PunktSentenceTokenizer
import math
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentIntensityAnalyzer
import time
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
from tkinter import *



with open ('Reddit_Data.csv', 'w', newline='',encoding="utf-8-sig") as f:
    fieldnames = ['submission_num','Submission_ID','Submission_Title','Submission_Comments','Submission_Sentiment','submission_link']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
                


    reddit = praw.Reddit(client_id = "bg9SK32k3dZUvA",
                         client_secret = "J4METC_ffoYyxOoLMmJoiBORtbBpFg",
                         username = "SentimentAnalysisUni",
                         password = "Brighton2021",
                         user_agent = "PythonPraw")
    



    root = Tk()
    sub_name = Entry(root)
    num = Entry(root)
    search_type = Entry(root)
    flair_name = Entry(root)
    comments = Entry(root)

    sub_name.insert(0,"Enter the name of a subreddit")
    num.insert(1,"Enter how many posts you want to check for a specific flair")
    search_type.insert(2,"Enter searech type (top - top posts of all time. hot - top posts in the last few days. new - the newest posts")
    flair_name.insert(3,"Enter Flair type")
    comments.insert(4,"Enter amount of comments you want to analysie per post")
    
    

    sub_name.pack()
    num.pack()
    search_type.pack()
    flair_name.pack()
    comments.pack()


    def click():
        global sub_name
        global num
        global search_type
        global flair_name
        global comments
        sub_name = sub_name.get()
        num = num.get()
        search_type = search_type.get()
        flair_name = flair_name.get()
        comments = comments.get()
        root.destroy()
                

    myButton = Button(root, text="Enter: ", command=click)
    myButton.pack()

    root.protocol(click)
    root.geometry("500x500")
    root.mainloop()

    sub_name = str(sub_name)
    num = int(num)
    search_type = str(search_type)
    flair_name = str(flair_name)
    comments = int(comments)
        

        


    subred = reddit.subreddit(str(sub_name))

    

    if search_type == "top": 
        hot_apex = subred.top(limit=num) 
    elif  search_type == "hot":
        hot_apex = subred.hot(limit=num)
    elif search_type == "new":
        hot_apex = subred.new(limit=num)
    User_subname = list(hot_apex)

    sub_title = []
    n = 0
    sub_link = []

    list_sub_title = list(sub_title)

    for submission in User_subname:
        if submission.link_flair_text == flair_name:
            i = str(submission) # makes i the string version of sub id 
            sub_title.append(submission.title)
            sub_id = reddit.submission(id=i) #sub_id holds the reddit submission id
            n = n + 1
            sub_link.append(submission.shortlink)
            writer.writerow({'submission_num':'S' + str(n),'Submission_ID' : submission.id,'Submission_Title' : submission.title,'submission_link' : submission.shortlink})
            count = 0
            for comment in sub_id.comments:
                if hasattr(comment, 'body'):
                    count = count + 1
                    if count < comments:
                        writer.writerow({'Submission_Comments' : comment.body})

    
   

    sia = SentimentIntensityAnalyzer()

    stop_words = set(stopwords.words("english"))

    words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]

    import pandas as pd
    import csv

    
    if len(sub_title) < 1: 
        print ("There was no results found with your search parameters")
        exit()



    df = pd.read_csv("Reddit_Data.csv")
    df = df.iloc[1:]
    
    Comments_column = df.Submission_Comments 
        
    comment_list = []
    for row in Comments_column:
        comment_list.append(row)
        
    comment_ = comments - 1

        
    # Splits all the comments in to seperate lists each new list holds the comments from one post. I need to fnd a way to automtize this so there isnt a cap on how many posts are analysised
    comment_1 = comment_list[:comment_]                   
    comment_2 = comment_list[comment_ : comment_+comments]
    comment_3 = comment_list[comment_+comments:comment_+comments*2] 
    comment_4 = comment_list[comment_+comments*2:comment_+comments*3]
    comment_5 = comment_list[comment_+comments*3:comment_+comments*4]
    comment_6 = comment_list[comment_+comments*4:comment_+comments*5]
    comment_7 = comment_list[comment_+comments*5:comment_+comments*6]
    comment_8 = comment_list[comment_+comments*6:comment_+comments*7]
    comment_9 = comment_list[comment_+comments*7:comment_+comments*8]
    comment_10 = comment_list[comment_+comments*8:comment_+comments*9]
    comment_11 = comment_list[comment_+comments*9:comment_+comments*10]
    comment_12 = comment_list[comment_+comments*10:comment_+comments*11]
    comment_13 = comment_list[comment_+comments*11:comment_+comments*12]
    comment_14 = comment_list[comment_+comments*12:comment_+comments*13]
    comment_15 = comment_list[comment_+comments*13:comment_+comments*14]
    comment_16 = comment_list[comment_+comments*14:comment_+comments*15]
    comment_17 = comment_list[comment_+comments*15:comment_+comments*16]
    comment_18 = comment_list[comment_+comments*16:comment_+comments*17]
    comment_19 = comment_list[comment_+comments*17:comment_+comments*18]
    comment_20 = comment_list[comment_+comments*18:comment_+comments*19]
    comment_21 = comment_list[comment_+comments*19:comment_+comments*20]
    comment_22 = comment_list[comment_+comments*20:comment_+comments*21]
    comment_23 = comment_list[comment_+comments*21:comment_+comments*22]
    comment_24 = comment_list[comment_+comments*22:comment_+comments*23]
    comment_25 = comment_list[comment_+comments*23:comment_+comments*24]
    comment_26 = comment_list[comment_+comments*24:comment_+comments*25]
    comment_27 = comment_list[comment_+comments*25:comment_+comments*26]
    comment_28 = comment_list[comment_+comments*26:comment_+comments*27]
    comment_29 = comment_list[comment_+comments*27:comment_+comments*28]
    comment_30 = comment_list[comment_+comments*28:comment_+comments*29]
   
    





    sen_score_1 = (sia.polarity_scores(str(comment_1)))
    sen_score_2 = (sia.polarity_scores(str(comment_2)))
    sen_score_3 = (sia.polarity_scores(str(comment_3)))
    sen_score_4 = (sia.polarity_scores(str(comment_4)))
    sen_score_5 = (sia.polarity_scores(str(comment_5)))
    sen_score_6 = (sia.polarity_scores(str(comment_6)))
    sen_score_7 = (sia.polarity_scores(str(comment_7)))
    sen_score_8 = (sia.polarity_scores(str(comment_8)))
    sen_score_9 = (sia.polarity_scores(str(comment_9)))
    sen_score_10 = (sia.polarity_scores(str(comment_10)))
    sen_score_11 = (sia.polarity_scores(str(comment_11)))
    sen_score_12 = (sia.polarity_scores(str(comment_12)))
    sen_score_13 = (sia.polarity_scores(str(comment_13)))
    sen_score_14 = (sia.polarity_scores(str(comment_14)))
    sen_score_15 = (sia.polarity_scores(str(comment_15)))
    sen_score_16 = (sia.polarity_scores(str(comment_16)))
    sen_score_17 = (sia.polarity_scores(str(comment_17)))
    sen_score_18 = (sia.polarity_scores(str(comment_18)))
    sen_score_19 = (sia.polarity_scores(str(comment_19)))
    sen_score_20 = (sia.polarity_scores(str(comment_10)))
    sen_score_21 = (sia.polarity_scores(str(comment_21)))
    sen_score_22 = (sia.polarity_scores(str(comment_22)))
    sen_score_23 = (sia.polarity_scores(str(comment_23)))
    sen_score_24 = (sia.polarity_scores(str(comment_24)))
    sen_score_25 = (sia.polarity_scores(str(comment_25)))
    sen_score_26 = (sia.polarity_scores(str(comment_26)))
    sen_score_27 = (sia.polarity_scores(str(comment_27)))
    sen_score_28 = (sia.polarity_scores(str(comment_28)))
    sen_score_29 = (sia.polarity_scores(str(comment_29)))
    sen_score_30 = (sia.polarity_scores(str(comment_30)))
    
    


    
                    
    list_of_T = [
    ('S1',sen_score_1,), 
    ('S2',sen_score_2,), 
    ('S3',sen_score_3,), 
    ('S4',sen_score_4,),
    ('S5',sen_score_5,), 
    ('S6',sen_score_6,), 
    ('S7',sen_score_7,), 
    ('S8',sen_score_8,), 
    ('S9',sen_score_9,), 
    ('S10',sen_score_10,), 
    ('S11',sen_score_11,), 
    ('S12',sen_score_12,), 
    ('S13',sen_score_13,), 
    ('S14',sen_score_14,),
    ('S15',sen_score_15,),
    ('S16',sen_score_16,), 
    ('S17',sen_score_17,), 
    ('S19',sen_score_18,), 
    ('S19',sen_score_19,),
    ('S20',sen_score_20,), 
    ('S21',sen_score_21,), 
    ('S22',sen_score_22,), 
    ('S23',sen_score_23,), 
    ('S24',sen_score_24,), 
    ('S25',sen_score_25,), 
    ('S26',sen_score_26,),
    ('S27',sen_score_27,),
    ('S28',sen_score_28,), 
    ('S29',sen_score_29,), 
    ('S30',sen_score_30,), 
    ]        

    
        
    list_of_tuple = []    

    i = 0
    for li in list_of_T:
        if (i < len(sub_title)):
            new_li = (sub_title[i],sub_link[i]) + li
            i = i + 1 
            list_of_tuple.append(new_li)
    
  
    new_dict = []
    for e in list_of_tuple:
        score = (e[3]['pos'] - e[3]['neg'])
        if score!= int:
            new_dict.append((e[0],e[1], e[2],  (e[3]['pos'] - e[3]['neg'])))

    
    
    def bubbleSort(nlist):
        for passnum in range(len(nlist)-1,0,-1):
            for i in range(passnum):
                if nlist[i][3]<nlist[i+1][3]:
                    temp = nlist[i]
                    nlist[i] = nlist[i+1]
                    nlist[i+1] = temp
    
                    
        
    bubbleSort(new_dict)
    
    print (new_dict[6])
    last_elem = len(sub_title)-1
    
    

    with open ('Sen_Results.csv', 'w', newline='',encoding="utf-8-sig") as f:
        fieldnames = ['submission_title','submission_type','Submission_Num','Submission_Sentiment', 'submission_link','info',]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in new_dict:
      
            
            writer.writerow({'submission_title': i[0],'submission_link': i[1],'submission_type':search_type, 'Submission_Num': i[2], 'Submission_Sentiment' : i[3]})   

        writer.writerow({'info': "The posts are ordered in what has recieved the most postive feedback in the comments and also shows what type of post it is"})

submission_title = list(zip(*new_dict))[2]
Submission_Sentiment = list(zip(*new_dict))[3]

x = np.arange(len(submission_title)) 

slope, intercept = np.polyfit(x, Submission_Sentiment, 1)
c = 'center'
plt.bar(x, Submission_Sentiment,align=c)
plt.xticks(x, submission_title) 
plt.ylabel('Sentiment score')
plt.xlabel('submissions 1 - ' + str(last_elem))
plt.show()

