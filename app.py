# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, jsonify, request
from pprint import pprint
from sklearn.linear_model._base import _preprocess_data
import json
import plotly.graph_objects as go
import pickle
import csv
import nltk
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from IPython.display import HTML
from jinja2 import Template



# Import credentials
from config import username, password, hostname, port, db

# Create Flask
app = Flask(__name__)

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db}')

# Load the model
# model = pickle.load(open('./model.pkl','rb'))



# Game Recommender Input

game_query = {}


# Main Routes

# Recommender
@app.route("/recommender")
def recommender():
    return render_template('recommender.html')



@app.route('/recommender',methods=['GET','POST'])
def gamepassthrough():
    if request.method=='POST':
        game = request.form['gameinput']
        # return game
        # print(game)
        index = len(game_query) + 1
        game_query[index] = request.form.get('gameinput')
        # Preprocessing functions
        def remove_stopwords(tokens):
            stop_words = set(stopwords.words('english'))
            filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
            return filtered_tokens

        def lemmatize_tokens(tokens):
            lemmatizer = WordNetLemmatizer()
            lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
            return lemmatized_tokens

        # User input
        user_input = request.form['gameinput']

        # Preprocess user input
        input_tokens = word_tokenize(user_input)
        input_tokens = remove_stopwords(input_tokens)
        input_tokens = lemmatize_tokens(input_tokens)

        # Load CSV data
        csv_file = 'video_game_cleaned_v2.csv'  # Replace with your CSV file path
        rows = []
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                rows.append(row)

        # Preprocess and tokenize CSV data
        documents = [' '.join(row) for row in rows]
        corpus_tokens = [word_tokenize(doc) for doc in documents]
        corpus_tokens = [remove_stopwords(tokens) for tokens in corpus_tokens]
        corpus_tokens = [lemmatize_tokens(tokens) for tokens in corpus_tokens]

        # Convert tokens back to strings for vectorization
        corpus_texts = [' '.join(tokens) for tokens in corpus_tokens]

        # Vectorize input and corpus texts
        vectorizer = TfidfVectorizer()
        vectorized_input = vectorizer.fit_transform([user_input])
        vectorized_corpus = vectorizer.transform(corpus_texts)

        # Compute cosine similarity between input and corpus
        cosine_similarities = cosine_similarity(vectorized_input, vectorized_corpus).flatten()

        # Find indices of rows with the highest cosine similarity
        top_similar_indices = cosine_similarities.argsort()[::-1]

        # Define the number of top matches you want to retrieve
        top_matches_count = 1

        # Get the top matching rows
        top_matching_rows = [rows[i] for i in top_similar_indices[:top_matches_count]]

        # Print the top matching rows
        print(f"Top {top_matches_count} matching rows:")
        for row in top_matching_rows:
            input_video_game = row[1].lower()
    
        print(input_video_game)
        game_match=input_video_game
        df = pd.read_csv('https://raw.githubusercontent.com/mshawn12/video-game-sales-analysis/main/resources/video_game_cleaned.csv')
        df = df.drop_duplicates(subset='name')
        sample_size = 4420
        df = df.sample(n=sample_size, replace=False, random_state=390)

        df = df.reset_index()
        df = df.drop('index',axis=1)
        def clean_text_pub(publisher):
            result = str(publisher).lower()
            return(result.replace(' ',''))
        df['publisher'] = df['publisher'].apply(clean_text_pub)
        def clean_text_dev(developer):
            result = str(developer).lower()
            return(result.replace(' ',''))
        df['developer'] = df['developer'].apply(clean_text_dev)
        df['name'] = df['name'].str.lower()
        df['publisher'] = df['publisher'].str.lower()
        df['genre'] = df['genre'].str.lower()
        df['developer'] = df['developer'].str.lower()
        df2 = df.drop(['nasales', 'eusales', 'jpsales', 'othersales', 'globalsales',
       'criticscore', 'criticcount', 'userscore', 'usercount'],axis=1)

        df2['data'] = df2[df2.columns[1:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        vectorizer = CountVectorizer()
        vectorized = vectorizer.fit_transform(df2['data'])
        similarities = cosine_similarity(vectorized)
        df = pd.DataFrame(similarities, columns=df['name'], index=df['name']).reset_index()
        recommendations = pd.DataFrame(df.nlargest(21,input_video_game)['name'])
        recommendations = recommendations[recommendations['name']!=input_video_game]
        recommendations_list = recommendations['name'].values.tolist()
        rec_1 = recommendations_list[0]
        rec_2 = recommendations_list[1]
        rec_3 = recommendations_list[2]
        rec_4 = recommendations_list[3]
        rec_5 = recommendations_list[4]
        rec_6 = recommendations_list[5]
        rec_7 = recommendations_list[6]
        rec_8 = recommendations_list[7]
        rec_9 = recommendations_list[8]
        rec_10 = recommendations_list[9]
        rec_11 = recommendations_list[10]
        rec_12 = recommendations_list[11]
        rec_13 = recommendations_list[12]
        rec_14 = recommendations_list[13]
        rec_15 = recommendations_list[14]
        rec_16 = recommendations_list[15]
        rec_17 = recommendations_list[16]
        rec_18 = recommendations_list[17]
        rec_19 = recommendations_list[18]
        rec_20 = recommendations_list[19]
        # list_template = Template("""
        # <table>
        #     <tr>
        #         <th>Game</th>
        #     </tr>
        #     <tr>
        #     {% for row in table %}
        #         <tr>
        #             <td>{{ row[0] }}</td>
        #         </tr>
        #     {% endfor %}
        # </table>
        # """)
        # recommendations_template = list_template.render(table=recommendations_list)

        # recommendations_html = recommendations.to_html(index=False)
        # recommendations_df = recommendations(index=False)
        # recommendations_df = open('results.html','w')
        # recommendations_df = write(recommendations_html)
        # recommendations_df.close()
        # HTML(recommendations.to_html(classes='table table-stripped'))


        # recommendations_df
        print('Here are some recommended video games for you from Group 1')
        print(recommendations)


    # return render_template('pass.html',game=game,game_match=game_match,game_recommendations=recommendations_html)
    # return render_template('pass.html',game=game,game_match=game_match,game_recommendations=recommendations)
    return render_template('pass.html',game=game,game_match=game_match,rec_1 = rec_1,rec_2 = rec_2,rec_3 = rec_3,rec_4 = rec_4,rec_5 = rec_5,rec_6 = rec_6,rec_7 = rec_7,rec_8 = rec_8
        ,rec_9 = rec_9,rec_10 = rec_10,rec_11 = rec_11,rec_12 = rec_12,rec_13 = rec_13,rec_14 = rec_14,rec_15 = rec_15,rec_16 = rec_16
        ,rec_17 = rec_17,rec_18 = rec_18,rec_19 = rec_19,rec_20 = rec_20)
    # return render_template('pass.html',game=game,game_match=game_match,game_recommendations=recommendations_template)
    


# --------------------------------------------


@app.route("/results")
def results():
    return render_template('results.html')


# @app.route('/predict',methods=['POST'])
# def predict():
#     # Get the data from the POST request.
#     if request.method == "POST":
#         #data = request.get_json(force=True)
#         print(request.form['exp'])
#         data = float(request.form['exp'])
#         print("Data", model.predict([[data]]))
#         # Make prediction using model loaded from disk as per the data.
#         prediction = model.predict([[data]])

#         # Take the first value of prediction
#         output = prediction[0]

#         return render_template("results.html", output=output, exp=data)


# Original 

# Map routes
@app.route("/api/v1.0/videogameinfo")
def videogameinfo():
    conn= engine.connect()
    query = "SELECT * FROM video_game_info"
    df = pd.read_sql(query, conn)
    return df.to_json(orient= "records")

@app.route("/api/v1.0/videogamesales")
def videogamesales():
    conn= engine.connect()
    query = "SELECT * FROM video_game_sales"
    df = pd.read_sql(query, conn)
    return df.to_json(orient= "records")

@app.route("/api/v1.0/videogamescores")
def videogamescores():
    conn= engine.connect()
    query = "SELECT * FROM video_game_scores"
    df = pd.read_sql(query, conn)
    return df.to_json(orient= "records")





# Test Route
@app.route("/test")
def test():
    data = "/api/v1.0/completedata"
    name = "test"
    return render_template("test.html", games=data,name=name)


@app.route("/home")
def home():
    data = "/api/v1.0/completedata"
    name = "Home"
    return render_template("index.html", games=data,name=name)

@app.route("/")
def dashboard():
    data = "/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completedata"
    df = pd.read_sql(query, conn)

    return render_template("dashboard.html",games=df.to_json(orient= "records"))


@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")


# Action Dashboard
@app.route("/actiondashboard")
def actiondashboard():
    data = "/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Action'"
    df = pd.read_sql(query, conn)

    return render_template("actiondashboard.html",games=df.to_json(orient= "records"))


@app.route("/api/v1.0/actiondashboard")
def actiondashboardapi():
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Action'"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")


# Average Critic Score for Genres - Action
@app.route("/api/v1.0/avggamecriticscoreaction")
def avggamecriticscoreaction():
    conn = engine.connect()
    query = "SELECT AVG(criticscore) FROM completedata WHERE genre='Action'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Genres - Action
@app.route("/api/v1.0/avggameuserscoreaction")
def avggameuserscoreaction():
    conn = engine.connect()
    query = "SELECT AVG(userscore) FROM completedata WHERE genre='Action'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")


# Total Sales by Game - All Genres - Action
@app.route("/api/v1.0/gamesalesaction")
def gamesalesaction():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Action' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")      


# Global Sales by Publisher - Action
@app.route("/api/v1.0/publishersalesaction")
def publishersalesaction():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), publisher FROM completedata WHERE genre='Action' GROUP BY publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 



# Global Sales by Developer - Action 
@app.route("/api/v1.0/developersalesaction")
def developersalesaction():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), developer FROM completedata WHERE genre='Action' GROUP BY developer, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 

# Sum of Global Sales - Action
@app.route("/api/v1.0/sumglobalsalesaction")
def sumglobalsalesaction():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), genre FROM completedata WHERE genre='Action' GROUP BY genre"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")



# Total Sales by Region - Action
@app.route("/api/v1.0/totalsalesaction")
def totalsalesaction():
    conn = engine.connect()
    query = "SELECT SUM(nasales) AS nasales,SUM(eusales) AS eusales,SUM(jpsales) AS jpsales FROM completedata WHERE genre ='Action'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - Top 10 - Action
@app.route("/api/v1.0/gamesalestop10action")
def gamesalestop10action():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Action' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC LIMIT 10"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  





# Adventure Dashboard
@app.route("/adventuredashboard")
def adventuredashboard():
    data = "/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Adventure'"
    df = pd.read_sql(query, conn)

    return render_template("adventuredashboard.html",games=df.to_json(orient= "records"))


@app.route("/api/v1.0/adventuredashboard")
def adventuredashboardapi():
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Adventure'"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")


# Average Critic Score for Genres - Adventure
@app.route("/api/v1.0/avggamecriticscoreadventure")
def avggamecriticscoreadventure():
    conn = engine.connect()
    query = "SELECT AVG(criticscore) FROM completedata WHERE genre='Adventure'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Genres - Adventure
@app.route("/api/v1.0/avggameuserscoreadventure")
def avggameuserscoreadventure():
    conn = engine.connect()
    query = "SELECT AVG(userscore) FROM completedata WHERE genre='Adventure'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - All Genres - Adventure
@app.route("/api/v1.0/gamesalesadventure")
def gamesalesadventure():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Adventure' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")      

# Global Sales by Publisher - Adventure
@app.route("/api/v1.0/publishersalesadventure")
def publishersalesadventure():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), publisher FROM completedata WHERE genre='Adventure' GROUP BY publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 


# Global Sales by Developer - Adventure 
@app.route("/api/v1.0/developersalesadventure")
def developersalesadventure():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), developer FROM completedata WHERE genre='Adventure' GROUP BY developer, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 

# Sum of Global Sales - Adventure
@app.route("/api/v1.0/sumglobalsalesadventure")
def sumglobalsalesadventure():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), genre FROM completedata WHERE genre='Adventure' GROUP BY genre"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Total Sales by Region - Adventure
@app.route("/api/v1.0/totalsalesadventure")
def totalsalesadventure():
    conn = engine.connect()
    query = "SELECT SUM(nasales) AS nasales,SUM(eusales) AS eusales,SUM(jpsales) AS jpsales FROM completedata WHERE genre ='Adventure'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - Top 10 - Adventure
@app.route("/api/v1.0/gamesalestop10adventure")
def gamesalestop10adventure():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Adventure' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC LIMIT 10"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  




# Puzzle Dashboard
@app.route("/puzzledashboard")
def puzzledashboard():
    data = "/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Puzzle'"
    df = pd.read_sql(query, conn)

    return render_template("puzzledashboard.html",games=df.to_json(orient= "records"))


@app.route("/api/v1.0/puzzledashboard")
def puzzledashboardapi():
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Puzzle'"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")


# Average Critic Score for Genres - Puzzle
@app.route("/api/v1.0/avggamecriticscorepuzzle")
def avggamecriticscorepuzzle():
    conn = engine.connect()
    query = "SELECT AVG(criticscore) FROM completedata WHERE genre='Puzzle'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Genres - Puzzle
@app.route("/api/v1.0/avggameuserscorepuzzle")
def avggameuserscorepuzzle():
    conn = engine.connect()
    query = "SELECT AVG(userscore) FROM completedata WHERE genre='Puzzle'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - All Genres - Puzzle
@app.route("/api/v1.0/gamesalespuzzle")
def gamesalespuzzle():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Puzzle' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")      

# Global Sales by Publisher - Puzzle
@app.route("/api/v1.0/publishersalespuzzle")
def publishersalespuzzle():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), publisher FROM completedata WHERE genre='Puzzle' GROUP BY publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 


# Global Sales by Developer - Puzzle 
@app.route("/api/v1.0/developersalespuzzle")
def developersalespuzzle():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), developer FROM completedata WHERE genre='Puzzle' GROUP BY developer, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 

# Sum of Global Sales - Puzzle
@app.route("/api/v1.0/sumglobalsalespuzzle")
def sumglobalsalespuzzle():
    conn = engine.connect()
    query = "SELECT CAST(SUM(globalsales) AS DECIMAL(10,2)), genre FROM completedata WHERE genre='Puzzle' GROUP BY genre"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Total Sales by Region - Puzzle
@app.route("/api/v1.0/totalsalespuzzle")
def totalsalespuzzle():
    conn = engine.connect()
    query = "SELECT SUM(nasales) AS nasales,SUM(eusales) AS eusales,SUM(jpsales) AS jpsales FROM completedata WHERE genre ='Puzzle'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - Top 10 - Puzzle
@app.route("/api/v1.0/gamesalestop10puzzle")
def gamesalestop10puzzle():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Puzzle' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC LIMIT 10"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  



# Strategy Dashboard
@app.route("/strategydashboard")
def strategydashboard():
    data = "/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Strategy'"
    df = pd.read_sql(query, conn)

    return render_template("strategydashboard.html",games=df.to_json(orient= "records"))


@app.route("/api/v1.0/strategydashboard")
def strategydashboardapi():
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Strategy'"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")


# Average Critic Score for Genres - Strategy
@app.route("/api/v1.0/avggamecriticscorestrategy")
def avggamecriticscorestrategy():
    conn = engine.connect()
    query = "SELECT AVG(criticscore) FROM completedata WHERE genre='Strategy'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Genres - Strategy
@app.route("/api/v1.0/avggameuserscorestrategy")
def avggameuserscorestrategy():
    conn = engine.connect()
    query = "SELECT AVG(userscore) FROM completedata WHERE genre='Strategy'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")


# Total Sales by Game - All Genres - Strategy
@app.route("/api/v1.0/gamesalesstrategy")
def gamesalesstrategy():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Strategy' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")      

# Global Sales by Publisher - Strategy
@app.route("/api/v1.0/publishersalesstrategy")
def publishersalesstrategy():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), publisher FROM completedata WHERE genre='Strategy' GROUP BY publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 


# Global Sales by Developer - Strategy 
@app.route("/api/v1.0/developersalesstrategy")
def developersalesstrategy():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), developer FROM completedata WHERE genre='Strategy' GROUP BY developer, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 

# Sum of Global Sales - Strategy
@app.route("/api/v1.0/sumglobalsalesstrategy")
def sumglobalsalesstrategy():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), genre FROM completedata WHERE genre='Strategy' GROUP BY genre"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Total Sales by Region - Strategy
@app.route("/api/v1.0/totalsalesstrategy")
def totalsalesstrategy():
    conn = engine.connect()
    query = "SELECT SUM(nasales) AS nasales,SUM(eusales) AS eusales,SUM(jpsales) AS jpsales FROM completedata WHERE genre ='Strategy'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - Top 10 - Strategy
@app.route("/api/v1.0/gamesalestop10strategy")
def gamesalestop10strategy():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Strategy' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC LIMIT 10"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  




# Role-Playing Dashboard
@app.route("/roleplayingdashboard")
def roleplayingdashboard():
    data = "/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Role-Playing'"
    df = pd.read_sql(query, conn)

    return render_template("roleplayingdashboard.html",games=df.to_json(orient= "records"))


@app.route("/api/v1.0/roleplayingdashboard")
def roleplayingdashboardapi():
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Role-Playing'"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Average Critic Score for Genres - Role Playing
@app.route("/api/v1.0/avggamecriticscoreroleplaying")
def avggamecriticscoreroleplaying():
    conn = engine.connect()
    query = "SELECT AVG(criticscore) FROM completedata WHERE genre='Role-Playing'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Genres - Role Playing
@app.route("/api/v1.0/avggameuserscoreroleplaying")
def avggameuserscoreroleplaying():
    conn = engine.connect()
    query = "SELECT AVG(userscore) FROM completedata WHERE genre='Role-Playing'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - All Genres - Role-Playing
@app.route("/api/v1.0/gamesalesroleplaying")
def gamesalesroleplaying():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Role-Playing' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")      

# Global Sales by Publisher - Role-Playing
@app.route("/api/v1.0/publishersalesroleplaying")
def publishersalesroleplaying():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), publisher FROM completedata WHERE genre='Role-Playing' GROUP BY publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 


# Global Sales by Developer - Role-Playing 
@app.route("/api/v1.0/developersalesroleplaying")
def developersalesroleplaying():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), developer FROM completedata WHERE genre='Role-Playing' GROUP BY developer, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 

# Sum of Global Sales - Role-Playing
@app.route("/api/v1.0/sumglobalsalesroleplaying")
def sumglobalsalesroleplaying():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), genre FROM completedata WHERE genre='Role-Playing' GROUP BY genre"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Total Sales by Region - Role-Playing
@app.route("/api/v1.0/totalsalesroleplaying")
def totalsalesroleplaying():
    conn = engine.connect()
    query = "SELECT SUM(nasales) AS nasales,SUM(eusales) AS eusales,SUM(jpsales) AS jpsales FROM completedata WHERE genre ='Role-Playing'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - Top 10 - Role-Playing
@app.route("/api/v1.0/gamesalestop10roleplaying")
def gamesalestop10roleplaying():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Role-Playing' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC LIMIT 10"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  



# Simulation Dashboard
@app.route("/simulationdashboard")
def simulationdashboard():
    data = "/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Simulation'"
    df = pd.read_sql(query, conn)

    return render_template("simulationdashboard.html",games=df.to_json(orient= "records"))


@app.route("/api/v1.0/simulationdashboard")
def simulationdashboardapi():
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Simulation'"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")


# Average Critic Score for Genres - Simulation
@app.route("/api/v1.0/avggamecriticscoresimulation")
def avggamecriticscoresimulation():
    conn = engine.connect()
    query = "SELECT AVG(criticscore) FROM completedata WHERE genre='Simulation'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Genres - Simulation
@app.route("/api/v1.0/avggameuserscoresimulation")
def avggameuserscoresimulation():
    conn = engine.connect()
    query = "SELECT AVG(userscore) FROM completedata WHERE genre='Simulation'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - All Genres - Simulation
@app.route("/api/v1.0/gamesalessimulation")
def gamesalessimulation():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Simulation' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")      

# Global Sales by Publisher - Simulation
@app.route("/api/v1.0/publishersalessimulation")
def publishersalessimulation():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), publisher FROM completedata WHERE genre='Simulation' GROUP BY publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 


# Global Sales by Developer - Simulation 
@app.route("/api/v1.0/developersalessimulation")
def developersalessimulation():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), developer FROM completedata WHERE genre='Simulation' GROUP BY developer, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 

# Sum of Global Sales - Simulation
@app.route("/api/v1.0/sumglobalsalessimulation")
def sumglobalsalessimulation():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), genre FROM completedata WHERE genre='Simulation' GROUP BY genre"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Total Sales by Region - Simulation
@app.route("/api/v1.0/totalsalessimulation")
def totalsalessimulation():
    conn = engine.connect()
    query = "SELECT SUM(nasales) AS nasales,SUM(eusales) AS eusales,SUM(jpsales) AS jpsales FROM completedata WHERE genre ='Simulation'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - Top 10 - Simulation
@app.route("/api/v1.0/gamesalestop10simulation")
def gamesalestop10simulation():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Simulation' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC LIMIT 10"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  






# Misc Dashboard
@app.route("/miscdashboard")
def miscdashboard():
    data = "/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Misc'"
    df = pd.read_sql(query, conn)

    return render_template("miscdashboard.html",games=df.to_json(orient= "records"))


@app.route("/api/v1.0/miscdashboard")
def miscdashboardapi():
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Misc'"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Average Critic Score for Genres - Misc
@app.route("/api/v1.0/avggamecriticscoremisc")
def avggamecriticscoremisc():
    conn = engine.connect()
    query = "SELECT AVG(criticscore) FROM completedata WHERE genre='Misc'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Genres - Misc
@app.route("/api/v1.0/avggameuserscoremisc")
def avggameuserscoremisc():
    conn = engine.connect()
    query = "SELECT AVG(userscore) FROM completedata WHERE genre='Misc'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")


# Total Sales by Game - All Genres - Misc
@app.route("/api/v1.0/gamesalesmisc")
def gamesalesmisc():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Misc' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")      

# Global Sales by Publisher - Misc
@app.route("/api/v1.0/publishersalesmisc")
def publishersalesmisc():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), publisher FROM completedata WHERE genre='Misc' GROUP BY publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 


# Global Sales by Developer - Misc 
@app.route("/api/v1.0/developersalesmisc")
def developersalesmisc():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), developer FROM completedata WHERE genre='Misc' GROUP BY developer, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 

# Sum of Global Sales - Misc
@app.route("/api/v1.0/sumglobalsalesmisc")
def sumglobalsalesmisc():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), genre FROM completedata WHERE genre='Misc' GROUP BY genre"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Total Sales by Region - Misc
@app.route("/api/v1.0/totalsalesmisc")
def totalsalesmisc():
    conn = engine.connect()
    query = "SELECT SUM(nasales) AS nasales,SUM(eusales) AS eusales,SUM(jpsales) AS jpsales FROM completedata WHERE genre ='Misc'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - Top 10 - Misc
@app.route("/api/v1.0/gamesalestop10misc")
def gamesalestop10misc():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Misc' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC LIMIT 10"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  





# Fighting Dashboard
@app.route("/fightingdashboard")
def fightingdashboard():
    data = "/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Fighting'"
    df = pd.read_sql(query, conn)

    return render_template("fightingdashboard.html",games=df.to_json(orient= "records"))


@app.route("/api/v1.0/fightingdashboard")
def fightingdashboardapi():
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Fighting'"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Average Critic Score for Genres - Fighting
@app.route("/api/v1.0/avggamecriticscorefighting")
def avggamecriticscorefighting():
    conn = engine.connect()
    query = "SELECT AVG(criticscore) FROM completedata WHERE genre='Fighting'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Genres - Fighting
@app.route("/api/v1.0/avggameuserscorefighting")
def avggameuserscorefighting():
    conn = engine.connect()
    query = "SELECT AVG(userscore) FROM completedata WHERE genre='Fighting'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - All Genres - Fighting
@app.route("/api/v1.0/gamesalesfighting")
def gamesalesfighting():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Fighting' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")      

# Global Sales by Publisher - Fighting
@app.route("/api/v1.0/publishersalesfighting")
def publishersalesfighting():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), publisher FROM completedata WHERE genre='Fighting' GROUP BY publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 


# Global Sales by Developer - Fighting 
@app.route("/api/v1.0/developersalesfighting")
def developersalesfighting():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), developer FROM completedata WHERE genre='Fighting' GROUP BY developer, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 

# Sum of Global Sales - Fighting
@app.route("/api/v1.0/sumglobalsalesfighting")
def sumglobalsalesfighting():
    conn = engine.connect()
    query = "SELECT CAST(SUM(globalsales) AS DECIMAL(10,2)), genre FROM completedata WHERE genre='Fighting' GROUP BY genre"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Total Sales by Region - Fighting
@app.route("/api/v1.0/totalsalesfighting")
def totalsalesfighting():
    conn = engine.connect()
    query = "SELECT SUM(nasales) AS nasales,SUM(eusales) AS eusales,SUM(jpsales) AS jpsales FROM completedata WHERE genre ='Fighting'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - Top 10 - Fighting
@app.route("/api/v1.0/gamesalestop10fighting")
def gamesalestop10fighting():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Fighting' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC LIMIT 10"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  



# Sports Dashboard
@app.route("/sportsdashboard")
def sportsdashboard():
    data = "/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Sports'"
    df = pd.read_sql(query, conn)

    return render_template("sportsdashboard.html",games=df.to_json(orient= "records"))


@app.route("/api/v1.0/sportsdashboard")
def sportsdashboardapi():
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Sports'"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Average Critic Score for Genres - Sports
@app.route("/api/v1.0/avggamecriticscoresports")
def avggamecriticscoresports():
    conn = engine.connect()
    query = "SELECT AVG(criticscore) FROM completedata WHERE genre='Sports'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Genres - Sports
@app.route("/api/v1.0/avggameuserscoresports")
def avggameuserscoresports():
    conn = engine.connect()
    query = "SELECT AVG(userscore) FROM completedata WHERE genre='Sports'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - All Genres - Sports
@app.route("/api/v1.0/gamesalessports")
def gamesalessports():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Sports' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")      

# Global Sales by Publisher - Sports
@app.route("/api/v1.0/publishersalessports")
def publishersalessports():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), publisher FROM completedata WHERE genre='Sports' GROUP BY publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 


# Global Sales by Developer - Sports 
@app.route("/api/v1.0/developersalessports")
def developersalessports():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), developer FROM completedata WHERE genre='Sports' GROUP BY developer, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 

# Sum of Global Sales - Sports
@app.route("/api/v1.0/sumglobalsalessports")
def sumglobalsalessports():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), genre FROM completedata WHERE genre='Sports' GROUP BY genre"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Total Sales by Region - Sports
@app.route("/api/v1.0/totalsalessports")
def totalsalessports():
    conn = engine.connect()
    query = "SELECT SUM(nasales) AS nasales,SUM(eusales) AS eusales,SUM(jpsales) AS jpsales FROM completedata WHERE genre ='Sports'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - Top 10 - Sports
@app.route("/api/v1.0/gamesalestop10sports")
def gamesalestop10sports():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Sports' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC LIMIT 10"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  



# Racing Dashboard
@app.route("/racingdashboard")
def racingdashboard():
    data = "/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Racing'"
    df = pd.read_sql(query, conn)

    return render_template("racingdashboard.html",games=df.to_json(orient= "records"))


@app.route("/api/v1.0/racingdashboard")
def racingdashboardapi():
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Racing'"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")


# Average Critic Score for Genres - Racing
@app.route("/api/v1.0/avggamecriticscoreracing")
def avggamecriticscoreracing():
    conn = engine.connect()
    query = "SELECT AVG(criticscore) FROM completedata WHERE genre='Racing'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Genres - Racing
@app.route("/api/v1.0/avggameuserscoreracing")
def avggameuserscoreracing():
    conn = engine.connect()
    query = "SELECT AVG(userscore) FROM completedata WHERE genre='Racing'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - All Genres - Racing
@app.route("/api/v1.0/gamesalesracing")
def gamesalesracing():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Racing' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")      

# Global Sales by Publisher - Racing
@app.route("/api/v1.0/publishersalesracing")
def publishersalesracing():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), publisher FROM completedata WHERE genre='Racing' GROUP BY publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 


# Global Sales by Developer - Racing 
@app.route("/api/v1.0/developersalesracing")
def developersalesracing():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), developer FROM completedata WHERE genre='Racing' GROUP BY developer, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 

# Sum of Global Sales - Racing
@app.route("/api/v1.0/sumglobalsalesracing")
def sumglobalsalesracing():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), genre FROM completedata WHERE genre='Racing' GROUP BY genre"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Total Sales by Region - Racing
@app.route("/api/v1.0/totalsalesracing")
def totalsalesracing():
    conn = engine.connect()
    query = "SELECT SUM(nasales) AS nasales,SUM(eusales) AS eusales,SUM(jpsales) AS jpsales FROM completedata WHERE genre ='Racing'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - Top 10 - Racing
@app.route("/api/v1.0/gamesalestop10racing")
def gamesalestop10racing():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Racing' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC LIMIT 10"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  



# FPS Dashboard
@app.route("/fpsdashboard")
def fpsdashboard():
    data = "/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Shooter'"
    df = pd.read_sql(query, conn)

    return render_template("fpsdashboard.html",games=df.to_json(orient= "records"))


@app.route("/api/v1.0/fpsdashboard")
def fpsdashboardapi():
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Shooter'"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")


# Average Critic Score for Genres - FPS
@app.route("/api/v1.0/avggamecriticscorefps")
def avggamecriticscorefps():
    conn = engine.connect()
    query = "SELECT AVG(criticscore) FROM completedata WHERE genre='Shooter'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Genres - FPS
@app.route("/api/v1.0/avggameuserscorefps")
def avggameuserscorefps():
    conn = engine.connect()
    query = "SELECT AVG(userscore) FROM completedata WHERE genre='Shooter'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - All Genres - Shooter
@app.route("/api/v1.0/gamesalesfps")
def gamesalesfps():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Shooter' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")      

# Global Sales by Publisher - Shooter
@app.route("/api/v1.0/publishersalesfps")
def publishersalesfps():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), publisher FROM completedata WHERE genre='Shooter' GROUP BY publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 


# Global Sales by Developer - Shooter 
@app.route("/api/v1.0/developersalesfps")
def developersalesfps():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), developer FROM completedata WHERE genre='Shooter' GROUP BY developer, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 

# Sum of Global Sales - Shooter
@app.route("/api/v1.0/sumglobalsalesfps")
def sumglobalsalesfps():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), genre FROM completedata WHERE genre='Shooter' GROUP BY genre"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Total Sales by Region - FPS
@app.route("/api/v1.0/totalsalesfps")
def totalsalesfps():
    conn = engine.connect()
    query = "SELECT SUM(nasales) AS nasales,SUM(eusales) AS eusales,SUM(jpsales) AS jpsales FROM completedata WHERE genre ='Shooter'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")


# Total Sales by Game - Top 10 - FPS
@app.route("/api/v1.0/gamesalestop10fps")
def gamesalestop10fps():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Shooter' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC LIMIT 10"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  



# Platform Dashboard
@app.route("/platformdashboard")
def platformdashboard():
    data = "/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Platform'"
    df = pd.read_sql(query, conn)

    return render_template("platformdashboard.html",games=df.to_json(orient= "records"))


@app.route("/api/v1.0/platformdashboard")
def platformdashboardapi():
    conn= engine.connect()
    query = "SELECT * FROM completedata WHERE genre='Platform'"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")


# Average Critic Score for Genres - Platform
@app.route("/api/v1.0/avggamecriticscoreplatform")
def avggamecriticscoreplatform():
    conn = engine.connect()
    query = "SELECT AVG(criticscore) FROM completedata WHERE genre='Platform'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Genres - Platform
@app.route("/api/v1.0/avggameuserscoreplatform")
def avggameuserscoreplatform():
    conn = engine.connect()
    query = "SELECT AVG(userscore) FROM completedata WHERE genre='Platform'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")


# Total Sales by Game - All Genres - Platform
@app.route("/api/v1.0/gamesalesplatform")
def gamesalesplatform():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Platform' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")      

# Global Sales by Publisher - Platform
@app.route("/api/v1.0/publishersalesplatform")
def publishersalesplatform():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), publisher FROM completedata WHERE genre='Platform' GROUP BY publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 


# Global Sales by Developer - Platform 
@app.route("/api/v1.0/developersalesplatform")
def developersalesplatform():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), developer FROM completedata WHERE genre='Platform' GROUP BY developer, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 

# Sum of Global Sales - Platform
@app.route("/api/v1.0/sumglobalsalesplatform")
def sumglobalsalesplatform():
    conn = engine.connect()
    query = "SELECT CAST(SUM(globalsales) AS DECIMAL(10,2)), genre FROM completedata WHERE genre='Platform' GROUP BY genre"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# Total Sales by Region - Platform
@app.route("/api/v1.0/totalsalesplatform")
def totalsalesplatform():
    conn = engine.connect()
    query = "SELECT SUM(nasales) AS nasales,SUM(eusales) AS eusales,SUM(jpsales) AS jpsales FROM completedata WHERE genre ='Platform'"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total Sales by Game - Top 10 - Platform
@app.route("/api/v1.0/gamesalestop10platform")
def gamesalestop10platform():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata WHERE genre='Platform' GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC LIMIT 10"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  




# Custom Paths / Queries


@app.route("/api/v1.0/completedata")
def completedata():
    conn = engine.connect()
    query = "SELECT * FROM completedata"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")



@app.route("/api/v1.0/genres")
def genres():
    conn = engine.connect()
    query = "SELECT DISTINCT genre FROM completedata"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")



# Total Global Sales by Genre
@app.route("/api/v1.0/genressales")
def genressales():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), genre FROM completedata GROUP BY genre"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  

# Average Global Sales by Genre
@app.route("/api/v1.0/avggenressales")
def avggenressales():
    conn = engine.connect()
    query = "SELECT AVG(globalsales), genre FROM completedata GROUP BY genre"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  

#
#
# 



# Total North America Sales
@app.route("/api/v1.0/totalsales")
def totalsales():
    conn = engine.connect()
    query = "SELECT SUM(nasales) AS nasales,SUM(eusales) AS eusales,SUM(jpsales) AS jpsales FROM completedata"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")








# Total North America Sales
@app.route("/api/v1.0/nasales")
def nasales():
    conn = engine.connect()
    query = "SELECT SUM(nasales) FROM completedata"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# North America Sales by Genre
@app.route("/api/v1.0/nasalesgenre")
def nasalesgenre():
    conn = engine.connect()
    query = "SELECT SUM(nasales), genre FROM completedata GROUP BY genre ORDER BY SUM(nasales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total EU Sales
@app.route("/api/v1.0/eusales")
def eusales():
    conn = engine.connect()
    query = "SELECT SUM(eusales) FROM completedata"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# EU Sales by Genre
@app.route("/api/v1.0/eusalesgenre")
def eusalesgenre():
    conn = engine.connect()
    query = "SELECT SUM(eusales), genre FROM completedata GROUP BY genre ORDER BY SUM(eusales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Total JP Sales
@app.route("/api/v1.0/jpsales")
def jpsales():
    conn = engine.connect()
    query = "SELECT SUM(jpsales) FROM completedata"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# JP Sales by Genre
@app.route("/api/v1.0/jpsalesgenre")
def jpsalesgenre():
    conn = engine.connect()
    query = "SELECT SUM(jpsales), genre FROM completedata GROUP BY genre ORDER BY SUM(jpsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")


# Sales Data

# Total Sales by Game - All Genres
@app.route("/api/v1.0/gamesales")
def gamesales():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")      

# Total Sales by Game - All Genres - Top 10
@app.route("/api/v1.0/gamesalestop10")
def gamesalestop10():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name, developer, publisher, genre FROM completedata GROUP BY name, developer, publisher, genre ORDER BY SUM(globalsales) DESC LIMIT 10"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")  


# Global Sales by Publisher
@app.route("/api/v1.0/publishersales")
def publishersales():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), publisher FROM completedata GROUP BY publisher ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 



# Global Sales by Developer
@app.route("/api/v1.0/developersales")
def developersales():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), developer FROM completedata GROUP BY developer ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 

# Sum of Global Sales
@app.route("/api/v1.0/sumglobalsales")
def sumglobalsales():
    conn = engine.connect()
    query = "SELECT CAST(SUM(globalsales) AS DECIMAL(10,2)) FROM completedata"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")





# Average Critic Score for Games
@app.route("/api/v1.0/avggamecriticscore")
def avggamecriticscore():
    conn = engine.connect()
    query = "SELECT AVG(criticscore) FROM completedata"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Games
@app.route("/api/v1.0/avggameuserscore")
def avggameuserscore():
    conn = engine.connect()
    query = "SELECT AVG(userscore) FROM completedata"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")





# Average Critic Score for Games
@app.route("/api/v1.0/gamecriticscore")
def gamecriticscore():
    conn = engine.connect()
    query = "SELECT AVG(criticscore), name, genre FROM completedata GROUP BY name, genre"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Games
@app.route("/api/v1.0/gameusercriticscore")
def gameusercriticscore():
    conn = engine.connect()
    query = "SELECT AVG(userscore), name, genre FROM completedata GROUP BY name, genre ORDER BY AVG(userscore) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average Critic Score for Genres
@app.route("/api/v1.0/genrecriticscore")
def genrecriticscore():
    conn = engine.connect()
    query = "SELECT AVG(criticscore), genre FROM completedata GROUP BY genre ORDER BY AVG(criticscore) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

# Average User Score for Genres
@app.route("/api/v1.0/genreusercriticscore")
def genreusercriticscore():
    conn = engine.connect()
    query = "SELECT AVG(userscore), genre FROM completedata GROUP BY genre"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")


@app.route("/api/v1.0/testdata")
def testdata():
    json_data = pd.read_json("/api/v1.0/completedata")
    return json_data.to_json(orient= "records")


# Run Flask
if __name__ == "__main__":
    app.run(debug= True)