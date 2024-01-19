from flask import Flask, render_template, request, Markup, session
import json
from plotly.offline import plot
from plotly.graph_objs import Scatter
from py2neo import Graph
import plotly
import pandas as pd
import math
from datetime import datetime,timedelta
import datetime
app = Flask(__name__) 
app.secret_key = "abc"  

def cumulative_list_community( first_day_str , time_list , sentiment_list ) :
    
    first_day_obj = datetime.datetime.strptime(first_day_str, '%Y-%m-%dT%H:%M:%S')
    #print(first_day_obj)
    
    cumulative_sentiments = []
    numerator = 0
    denominator = 0
    for i in range(len(time_list)) :
        time_obj = datetime.datetime.strptime(time_list[i], '%Y-%m-%dT%H:%M:%S')
        priority = (math.ceil( (time_obj-first_day_obj).total_seconds()/86400 ) + 1)
        #print(priority)
        numerator = numerator + (priority*float(sentiment_list[i]))
        denominator = denominator + priority
        cumulative_sentiments.append(numerator/denominator)
    
    return cumulative_sentiments


def community(xoxo) :
    graph = Graph(password="123")
    dataset = graph.run("match (t:Tweet) return t.text, t.time, t.sentiment_value, t.category").to_data_frame()
    dataset.columns = ['tweet','time','sentiment_value','category']
    dataset = dataset.sort_values(by='time')
    dataset = dataset.dropna()
    
    tweets = dataset.tweet.tolist()
    sentiments = dataset.sentiment_value.tolist()
    time = dataset.time.tolist()
    category = dataset.category.tolist()
    
    tweets_categorical = [[],[],[],[],[]]
    sentiments_categorical = [[],[],[],[],[]]
    cumulative_sentiments_categorical = [[],[],[],[],[]]
    time_categorical = [[],[],[],[],[]]
    
    for_days_tweets_categorical = [[],[],[],[],[]]
    for_days_sentiments_categorical = [[],[],[],[],[]]
    for_days_cumulative_sentiments_categorical = [[],[],[],[],[]]
    for_days_time_categorical = [[],[],[],[],[]]
    
    for_days_tweets = []
    for_days_sentiments = []
    for_days_time = []
    for_days_category = []
    
    days = 14
    
    category_list = ['education','business','politics','sports','entertainment']
    
    cur_time_str = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    cur_time_obj = datetime.datetime.strptime(cur_time_str, '%Y-%m-%dT%H:%M:%S')
    
    for i in range(len(tweets)) :
        tweet_time_obj = datetime.datetime.strptime(time[i] , '%Y-%m-%dT%H:%M:%S')
        diff = (cur_time_obj - tweet_time_obj).total_seconds()/86400
        category_index = category_list.index(category[i].lower())
        if(diff <= days) :
            for_days_tweets.append(tweets[i])
            for_days_sentiments.append(sentiments[i])
            for_days_time.append(time[i])
            for_days_category.append(category[i])
            
            for_days_tweets_categorical[category_index].append(tweets[i])
            for_days_sentiments_categorical[category_index].append(sentiments[i])
            for_days_time_categorical[category_index].append(time[i])
            
        tweets_categorical[category_index].append(tweets[i])
        sentiments_categorical[category_index].append(sentiments[i])
        time_categorical[category_index].append(time[i])
        
    cumulative_sentiments = cumulative_list_community(time[0],time,sentiments)
    date_14days_ago = datetime.datetime.now() - timedelta(days=14)
    date_14days_ago_str = date_14days_ago.strftime('%Y-%m-%dT%H:%M:%S')
    for_days_cumulative_sentiments = cumulative_list_community(date_14days_ago_str,for_days_time,for_days_sentiments)
    
    for i in range(5) :
        if(len(time_categorical[i]) > 0) :
            cumulative_sentiments_categorical[i] = cumulative_list_community(time_categorical[i][0],time_categorical[i],sentiments_categorical[i])
        if(len(for_days_time_categorical[i]) > 0) :
            for_days_cumulative_sentiments_categorical[i] = cumulative_list_community(date_14days_ago_str,for_days_time_categorical[i],for_days_sentiments_categorical[i])
    if(xoxo == 1):
    	return tweets_categorical, time_categorical, cumulative_sentiments_categorical
    else:
    	return for_days_tweets_categorical, for_days_time_categorical, for_days_cumulative_sentiments_categorical



def cumulative_list( first_day_str , time_list , sentiment_list ) :
    
    first_day_obj = datetime.datetime.strptime(first_day_str, '%Y-%m-%dT%H:%M:%S')
    #print(first_day_obj)
    
    cumulative_sentiments = []
    numerator = 0
    denominator = 0
    for i in range(len(time_list)) :
        time_obj = datetime.datetime.strptime(time_list[i], '%Y-%m-%dT%H:%M:%S')
        priority = (math.ceil( (time_obj-first_day_obj).total_seconds()/86400 ) + 1)
        #print(priority)
        #priority=priority*priority
        numerator = numerator + (priority*float(sentiment_list[i]))
        denominator = denominator + priority
        cumulative_sentiments.append(numerator/denominator)
    
    return cumulative_sentiments


#for perticular user 
def user_info( user_name, xox) :
    graph = Graph(password="123")
    query = 'match (p:User {name : "' + user_name + '"}) -[:TWEETS]-> (t:Tweet) return t.text,t.time,t.sentiment_value,t.category'
    user_data = graph.run(query).to_data_frame()
    user_data.columns = ['text','time','sentiment_value','category']
    user_data = user_data.sort_values(by="time",ascending=False)
    
    category_list = ['education','business','politics','sports','entertainment']
    
    #sentiment for 'days' days
    days = 14
    
    #sentiment over all time 
    tweets = user_data.text.tolist()
    sentiments = user_data.sentiment_value.tolist()
    time = user_data.time.tolist()
    category = user_data.category.tolist()
    
    tweets_categorical = [[],[],[],[],[]]
    sentiments_categorical = [[],[],[],[],[]]
    cumulative_sentiments_categorical = [[],[],[],[],[]]
    time_categorical = [[],[],[],[],[]]

    cur_time_str = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    cur_time_obj = datetime.datetime.strptime(cur_time_str, '%Y-%m-%dT%H:%M:%S')
    
    #data for max(14,days) days
    for_days_tweets = []
    for_days_sentiments = []
    for_days_time = []
    for_days_category = []
    
    #categorical data for max(14,days) days
    for_days_tweets_categorical = [[],[],[],[],[]]
    for_days_sentiments_categorical = [[],[],[],[],[]]
    for_days_cumulative_sentiments_categorical = [[],[],[],[],[]]
    for_days_time_categorical = [[],[],[],[],[]]
    
    for j in range(len(tweets)) :
        i = len(tweets) - j - 1
        tweet_time_obj = datetime.datetime.strptime(time[i] , '%Y-%m-%dT%H:%M:%S')
        diff = (cur_time_obj - tweet_time_obj).total_seconds()/86400
        category_index = category_list.index(category[i].lower())
        if(diff <= days) :
            for_days_tweets.append(tweets[i])
            for_days_sentiments.append(sentiments[i])
            for_days_time.append(time[i])
            for_days_category.append(category[i])
            
            for_days_tweets_categorical[category_index].append(tweets[i])
            for_days_sentiments_categorical[category_index].append(sentiments[i])
            for_days_time_categorical[category_index].append(time[i])
            
        tweets_categorical[category_index].append(tweets[i])
        sentiments_categorical[category_index].append(sentiments[i])
        time_categorical[category_index].append(time[i])
        
    tweets.reverse()
    sentiments.reverse()
    time.reverse()
    category.reverse() 
    cumulative_sentiments = cumulative_list(time[0],time,sentiments)
    
    date_14days_ago = datetime.datetime.now() - timedelta(days=14)
    date_14days_ago_str = date_14days_ago.strftime('%Y-%m-%dT%H:%M:%S')
    
    for_days_cumulative_sentiments = cumulative_list(date_14days_ago_str,for_days_time,for_days_sentiments)
    
    for i in range(5) :
        if(len(time_categorical[i]) > 0) :
            cumulative_sentiments_categorical[i] = cumulative_list(time_categorical[i][0],time_categorical[i],sentiments_categorical[i])
        if(len(for_days_time_categorical[i]) > 0) :
            for_days_cumulative_sentiments_categorical[i] = cumulative_list(date_14days_ago_str,for_days_time_categorical[i],for_days_sentiments_categorical[i])

    if (xox == 1):
        return tweets_categorical, cumulative_sentiments_categorical, time_categorical
    else :
        return for_days_tweets_categorical, for_days_cumulative_sentiments_categorical, for_days_time_categorical



@app.route('/') 
def show_whole_list():
	#code to fetch all the name along with its priority in json file
	f = open('dictionary.txt',mode='r', encoding="utf8")
	dic = f.read()
	f.close()
	x=json.loads(dic)
	y = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
	return render_template('result.html', result= y)


@app.route('/user_details',methods=["GET","POST"])
def user_details():
	if (request.method == "POST"):
		username=request.form['username']
		last_days=request.form['last_days']
		session['username'] = username
		session['last_days'] = last_days
	else:
		username=session['username']
		last_days=session['last_days']


	tweets_categorical, sentiments_categorical, time_categorical=user_info( username, 1 ) 
	
	import plotly.graph_objects as go
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=time_categorical[0], y=sentiments_categorical[0],hovertext=tweets_categorical[0], name='Education Sentiments',line=dict(color='blue', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=time_categorical[1], y=sentiments_categorical[1],hovertext=tweets_categorical[1], name='Business Sentiments',line=dict(color='yellow', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=time_categorical[2], y=sentiments_categorical[2],hovertext=tweets_categorical[2], name='Politics Sentiments',line=dict(color='green', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=time_categorical[3], y=sentiments_categorical[3],hovertext=tweets_categorical[3], name='Sports Sentiments',line=dict(color='red', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=time_categorical[4], y=sentiments_categorical[4],hovertext=tweets_categorical[4], name='Entertainment Sentiments',line=dict(color='black', width=1, dash='dot')))
	fig.update_layout(title=""+username+"'s Sentiments",xaxis_title='Time',yaxis_title='Sentiment Values')
	#my_plot_div = plot([Scatter(x=, y=)], output_type='div')
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return render_template('user_detail.html',to_check=1,user_val=username,days=last_days,plot = graphJSON)


@app.route('/user_details_days',methods=["GET","POST"])
def see_something():
	username = session['username']
	last_days = session['last_days']
	for_days_tweets_categorical, for_days_sentiments_categorical, for_days_time_categorical=user_info( username, 0 )
	import plotly.graph_objects as go
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=for_days_time_categorical[0], y=for_days_sentiments_categorical[0],hovertext=for_days_tweets_categorical[0], name='Education Sentiments',line=dict(color='blue', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=for_days_time_categorical[1], y=for_days_sentiments_categorical[1],hovertext=for_days_tweets_categorical[1], name='Business Sentiments',line=dict(color='yellow', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=for_days_time_categorical[2], y=for_days_sentiments_categorical[2],hovertext=for_days_tweets_categorical[2], name='Politics Sentiments',line=dict(color='green', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=for_days_time_categorical[3], y=for_days_sentiments_categorical[3],hovertext=for_days_tweets_categorical[3], name='Sports Sentiments',line=dict(color='red', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=for_days_time_categorical[4], y=for_days_sentiments_categorical[4],hovertext=for_days_tweets_categorical[4], name='Entertainment Sentiments',line=dict(color='black', width=1, dash='dot')))
	fig.update_layout(title=""+username+"'s Sentiments",xaxis_title='Time',yaxis_title='Sentiment Values')
	#my_plot_div = plot([Scatter(x=, y=)], output_type='div')
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return render_template('user_detail.html',to_check=0,user_val=username,days=last_days,plot = graphJSON)

@app.route('/community',methods=["GET","POST"])
def community_page():
	tweets_categorical, time_categorical, cumulative_sentiments_categorical = community(1)
	import plotly.graph_objects as go
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=time_categorical[0], y=cumulative_sentiments_categorical[0],hovertext=tweets_categorical[0], name='Education Sentiments',line=dict(color='blue', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=time_categorical[1], y=cumulative_sentiments_categorical[1],hovertext=tweets_categorical[1], name='Business Sentiments',line=dict(color='yellow', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=time_categorical[2], y=cumulative_sentiments_categorical[2],hovertext=tweets_categorical[2], name='Politics Sentiments',line=dict(color='green', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=time_categorical[3], y=cumulative_sentiments_categorical[3],hovertext=tweets_categorical[3], name='Sports Sentiments',line=dict(color='red', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=time_categorical[4], y=cumulative_sentiments_categorical[4],hovertext=tweets_categorical[4], name='Entertainment Sentiments',line=dict(color='black', width=1, dash='dot')))
	fig.update_layout(title="Community Overall Sentiments",xaxis_title='Time',yaxis_title='Sentiment Values')
	#my_plot_div = plot([Scatter(x=, y=)], output_type='div')
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return render_template('community_tab.html',to_do_check=1,plot=graphJSON)

@app.route('/community_by_days',methods=["GET","POST"])
def community_page1():
	tweets_categorical, time_categorical, cumulative_sentiments_categorical = community(0)
	import plotly.graph_objects as go
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=time_categorical[0], y=cumulative_sentiments_categorical[0],hovertext=tweets_categorical[0], name='Education Sentiments',line=dict(color='blue', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=time_categorical[1], y=cumulative_sentiments_categorical[1],hovertext=tweets_categorical[1], name='Business Sentiments',line=dict(color='yellow', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=time_categorical[2], y=cumulative_sentiments_categorical[2],hovertext=tweets_categorical[2], name='Politics Sentiments',line=dict(color='green', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=time_categorical[3], y=cumulative_sentiments_categorical[3],hovertext=tweets_categorical[3], name='Sports Sentiments',line=dict(color='red', width=1, dash='dot')))
	fig.add_trace(go.Scatter(x=time_categorical[4], y=cumulative_sentiments_categorical[4],hovertext=tweets_categorical[4], name='Entertainment Sentiments',line=dict(color='black', width=1, dash='dot')))
	fig.update_layout(title="Community last 14 days Sentiments",xaxis_title='Time',yaxis_title='Sentiment Values')
	#my_plot_div = plot([Scatter(x=, y=)], output_type='div')
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return render_template('community_tab.html',to_do_check=0,plot=graphJSON)


if __name__ == '__main__': 
   app.run(debug = True) 


