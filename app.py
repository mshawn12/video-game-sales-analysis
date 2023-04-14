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
    query = "SELECT * FROM completedata"
    df = pd.read_sql(query, conn)
    # print(df)
    return df.to_json(orient= "records")



# Test Route
@app.route("/test")
def test():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
    name = "test"
    return render_template("test.html", games=data,name=name)





# Main Routes

@app.route("/")
def home():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
    name = "test"
    return render_template("dashboard.html", games=data,name=name)

@app.route("/dashboard")
def dashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
    conn= engine.connect()
    query = "SELECT * FROM completedata"
    df = pd.read_sql(query, conn)

    return render_template("dashboard.html",games=df.to_json(orient= "records"))

# Action Dashboard
@app.route("/actiondashboard")
def actiondashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
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





# Adventure Dashboard
@app.route("/adventuredashboard")
def adventuredashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
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

# Puzzle Dashboard
@app.route("/puzzledashboard")
def puzzledashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
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

# Strategy Dashboard
@app.route("/strategydashboard")
def strategydashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
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

# Role-Playing Dashboard
@app.route("/roleplayingdashboard")
def roleplayingdashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
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

# Simulation Dashboard
@app.route("/simulationdashboard")
def simulationdashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
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

# Misc Dashboard
@app.route("/miscdashboard")
def miscdashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
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

# Fighting Dashboard
@app.route("/fightingdashboard")
def fightingdashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
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

# Sports Dashboard
@app.route("/sportsdashboard")
def sportsdashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
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

# Racing Dashboard
@app.route("/racingdashboard")
def racingdashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
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


# FPS Dashboard
@app.route("/fpsdashboard")
def fpsdashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
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

# Platform Dashboard
@app.route("/platformdashboard")
def platformdashboard():
    data = "http://127.0.0.1:5000/api/v1.0/completedata"
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