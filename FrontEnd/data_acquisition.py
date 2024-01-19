from py2neo import Graph
import pandas as pd
import math
import datetime

graph = Graph(password="123")

print('reading dataset...')
dataset = graph.run("match (p:User)-[:TWEETS]->(t:Tweet) return p.name, p.screen_name, t.text, t.time, t.sentiment_value").to_data_frame()  
dataset.columns = ['name','screen_name','text','time','sentiment_value']
dataset = dataset.sort_values(by='time')
print('dataset read complete')


dataset = dataset.dropna()

users = dataset.name.unique().tolist()
#screen_name = dataset.screen_name.unique().tolist()

tweets = []
time = []
sentiment = []

for i in range(len(users)) :
    tweets.append([])
    time.append([])
    sentiment.append([])
    
for ind in dataset.index :
    tweets[users.index(dataset['name'][ind])].append(dataset['text'][ind])
    time[users.index(dataset['name'][ind])].append(dataset['time'][ind])
    sentiment[users.index(dataset['name'][ind])].append(dataset['sentiment_value'][ind])
	
data = pd.DataFrame({ 'user':users , 'tweets':tweets , 'time':time , 'sentiment':sentiment })

print('processing each user...')
#data to show

first_day = dataset['time'].iloc[0]
first_day_obj = datetime.datetime.strptime(first_day, '%Y-%m-%dT%H:%M:%S')
dictionary = {}

for ind in data.index :
    name = data['user'][ind]
    #screen_name = data['screen_name'][ind]
    tweets = data['tweets'][ind]
    time = data['time'][ind]
    sentiment = data['sentiment'][ind]
    numerator = 0
    denominator = 0

    if(len(tweets) > 15 ):
    
        for i in range(len(tweets)) :
            tweet_time_obj = datetime.datetime.strptime(time[i], '%Y-%m-%dT%H:%M:%S')
            priority = math.ceil( (tweet_time_obj-first_day_obj).total_seconds()/86400 )
            numerator = numerator + (priority*float(sentiment[i]))
            denominator = denominator + priority
        
        cumulative_sentiment = numerator/denominator
        dictionary[name] = cumulative_sentiment
print('process complete...')
print(dictionary)
with open('dictionary1.txt', 'w', encoding='utf-8') as f:
    print(dictionary, file=f)
final_file = open('dictionary.txt','w', encoding="utf8") 
with open('dictionary1.txt', encoding="utf8") as f:
  while True:
    c = f.read(1)
    if not c:
        break
    if(c=="'"):
        final_file.write('"')
    else:
        final_file.write(c)
final_file.close()