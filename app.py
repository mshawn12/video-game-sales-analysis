# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, jsonify
from pprint import pprint
import json
import plotly.graph_objects as go

# Import credentials
from config import username, password, hostname, port, db

# Create Flask
app = Flask(__name__)

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db}')

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

@app.route("/api/v1.0/completevideogamedata")
def completevideogamedata():
    conn= engine.connect()
    query = "SELECT * FROM completevideogamedata"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

@app.route("/")
def home():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
    name = "test"
    return render_template("index.html", games=data,name=name)

@app.route("/dashboard")
def dashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completevideogamedata"
    df = pd.read_sql(query, conn)

    return render_template("dashboard.html",games=df.to_json(orient= "records"))

@app.route("/actiondashboard")
def actiondashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completevideogamedata WHERE genre='Action'"
    df = pd.read_sql(query, conn)

    return render_template("actiondashboard.html",games=df.to_json(orient= "records"))


@app.route("/api/v1.0/actiondashboard")
def actiondashboardapi():
    conn= engine.connect()
    query = "SELECT * FROM completevideogamedata WHERE genre='Action'"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")





# Custom Paths / Queries

@app.route("/api/v1.0/jsondata")
def jsondata():
    conn = engine.connect()
    query = "SELECT * FROM jsondata"
    df = pd.read_sql(query, conn)
    pprint(df)
    return df.to_json(orient="records")

@app.route("/api/v1.0/completedata")
def completedata():
    conn = engine.connect()
    query = "SELECT * FROM completedata"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records")

@app.route("/api/v1.0/sumglobalsales")
def sumglobalsales():
    conn = engine.connect()
    query = "SELECT SUM(globalsales) FROM completedata"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

@app.route("/api/v1.0/genres")
def genres():
    conn = engine.connect()
    query = "SELECT DISTINCT genre FROM completedata"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")

# @app.route("/api/v1.0/json3")
# def json3():
#     conn = engine.connect()
#     query = "SELECT json_agg(completedata) FROM completedata"
#     df = pd.read_sql(query, conn)
#     print(df)
#     return df.to_json(orient= "records")

# @app.route("/api/v1.0/json4")
# def json4():
#     conn = engine.connect()
#     query = "SELECT * FROM completedata"
#     df = pd.read_sql(query, conn)
#     # print(df)
#     return df.to_json(orient= "records")
#     # print(df)
#     # myjson = json.dumps(df)
#     # print("\nJSON format = ",myJSON);

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



# Total Sales by Game
@app.route("/api/v1.0/gamesales")
def gamesales():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), name FROM completedata GROUP BY name ORDER BY SUM(globalsales) DESC"
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

# Global Sales by Publisher
@app.route("/api/v1.0/publishersales")
def publishersales():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), publisher, genre FROM completedata GROUP BY publisher, genre ORDER BY SUM(globalsales) DESC"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient= "records") 

# Global Sales by Developer
@app.route("/api/v1.0/developersales")
def developersales():
    conn = engine.connect()
    query = "SELECT SUM(globalsales), developer, genre FROM completedata GROUP BY developer, genre ORDER BY SUM(globalsales) DESC"
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
    json_data = pd.read_json("http://127.0.0.1:5000/api/v1.0/completedata")
    return json_data.to_json(orient= "records")
    # fig = go.Figure(data=[go.Table(
    #     header=dict(values=list(json_data.columns),
    #                 fill_color='paleturquoise',
    #                 aligh='left'),
    #     cells=dict(values=[json_data.globalsales],
    #                fill_color='lavender',
    #                align='left')
    # )])

    # fig.show()



# @app.route("/api/v1.0/jsontest")
# def jsontest():
#     # conn = engine.connect()
#     # query = "SELECT SUM(globalsales) FROM completedata"
#     # df = pd.read_sql(query, conn)
#     # # print(df)
#     # return df.to_json(orient= "records")
#     url = "http://127.0.0.1:5000/api/v1.0/completedata"
#     response = requests.get(url).json()

#     genres = []
#     names = []

#     counter = 0
#     for game in response["genre"]:
#         try:
#             print(game["name"])
#             print(game["genre"])
#             genres.append(game["genre"])
#             names.append(game["name"])
#             counter = counter + 1

#             if counter == 100:
#                 break
        
#         except:
#             print("error")

#     raw_df = pd.DataFrame({
#         "Genres": genres,
#         "Names": names
#     })

#     print(raw_df)

# Run 
if __name__ == "__main__":
    app.run(debug= True)