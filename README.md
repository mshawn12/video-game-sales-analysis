# Video Game Analysis
<strong><i>Overview</i></strong>: Using a Python Flask-powered API, HTML/CSS, Javascript and SQL to test hypotheses about video game sales
<br/><br/>
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/main/images/video_game_header.png?raw=true">
<br/><br/>
<strong><i>Team Members</i></strong>: Alvaro Aquino, Dozie Kingsley, Emmanuel Garcia, Frantzy Francois, Jonathan Pokorny, & Mickey Young

## Background Information
The team will leverage a Global Video Game Sales & Ratings dataset from <a href="https://www.kaggle.com/datasets/thedevastator/global-video-game-sales-ratings">Kaggle</a> in order to test various hypotheses about video game genres.


## Process
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/process.png?raw=true" alt="project process"><br/><br/>
- <strong><i>Step 1</i></strong>: Creating Jupyter Notebook to load, clean, and export Excel files as CSVs as well as setting up sqlalchemy, config.py, .gitignore, pip install, etc.
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/main/images/jupyter_notebook.png?raw=true" alt="Jupyter Notebook preview"><br/>
<br/>

- <strong><i>Step 2</i></strong>: Creating an ERD Diagram using https://app.quickdatabasediagrams.com/ to develop SQL schema and assign the correct data types to all of our columns
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/main/images/ERD_Process.png?raw=true" alt="ERD Diagram via quickdatabasediagrams.com"><br/>
<br/>

- <strong><i>Step 3</i></strong>: Leveraging pgAdmin 4 to clean our data, create tables, and merge datasets. In order to have a single database for our Flask APIs, we joined the (3) datasets on "uniqueid" and selected the appropriate columns to avoid duplicate values
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/main/images/postgres_sql_steps.png?raw=true" alt="SQL steps">

- SQL Queries
```
    CREATE TABLE video_game_info (
        uniqueid INT,
        name VARCHAR,
        yearreleased INT,
        genre VARCHAR,
        publisher VARCHAR,
        developer VARCHAR,
        rating VARCHAR,
        CONSTRAINT pk_video_game_info PRIMARY KEY (
        uniqueid
     )
);

    CREATE TABLE video_game_sales (
        uniqueid INT,
        name VARCHAR,
        nasales FLOAT,
        eusales FLOAT,
        jpsales FLOAT,
        othersales FLOAT,
        globalsales FLOAT,
        CONSTRAINT pk_video_game_sales PRIMARY KEY (
        uniqueid
     )
);

    CREATE TABLE video_game_scores (
        uniqueid INT,
        name VARCHAR,
        criticscore INT,
        criticcount INT,
        userscore FLOAT,
        usercount INT,
        CONSTRAINT pk_video_game_scores PRIMARY KEY (
        uniqueid
     )
);

    ALTER TABLE video_game_sales ADD CONSTRAINT fk_video_game_sales_uniqueid FOREIGN KEY("uniqueid")
    REFERENCES video_game_info ("uniqueid");

    ALTER TABLE video_game_scores ADD CONSTRAINT fk_video_game_scores_uniqueid FOREIGN KEY("uniqueid")
    REFERENCES video_game_info ("uniqueid");


    CREATE TABLE completedata AS
        SELECT vgi.uniqueid,vgi.name, vgi.yearreleased, vgi.genre, vgi.publisher, vgi.developer, vgi.rating,
        vgs.nasales, vgs.eusales, vgs.jpsales, vgs.othersales, vgs.globalsales,vgsc.criticscore, vgsc.criticcount, vgsc.userscore, vgsc.usercount
        FROM video_game_sales AS vgs JOIN video_game_info AS vgi
        ON vgs.uniqueid = vgi.uniqueid
        JOIN video_game_scores AS vgsc
        ON vgsc.uniqueid= vgi.uniqueid
```
<br/>

- <strong><i>Step 4</i></strong>: Once our database was created, we developed a barebone HTML file with corresponding CSS & Javascript to test if our data was being pulled properly. In order to connect our files to the database, we first imported the create_engine function from sqlalchemy as well as a number of other dependencies. In addition, we created a config.py file to store our individual database credentials, stored them / imported them as variables, and used them in our create_engine function f string.
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/app_py_file.png?raw=true" alt="Preview of app.py file"><br/>
<br/>

- <strong><i>Step 5</i></strong>: Once our database was connected, we leveraged Google Slides to mock up what our potential dashboard could look like. This allowed us to quickly move things around, plan what specific metrics / visualizations we wanted to develop, and identify the proper next steps to achieve our goal. This served as our starting point and helped us understand the details of what needed to be done and what questions we hoped to answer.
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/dashboard_mockup.png?raw=true" alt="Preliminary dashboard mockup"><br/><br/>

- <strong><i>Step 6</i></strong>: Once we had a general idea of what our dashboard could look like, we began developing a list of potential questions that our dashboard could answer. Building off our story from <a href="https://github.com/mshawn12/group1-ticketmaster">Project 1</a>, where we assessed ticket prices & events for Music & Sports genres, our goal was to do an in-depth assessment to glean various insights on video game genres. Our goal as a group is to continue developing insights for producers, developers, and consumers alike in order to make data-driven decisions about the entertainment industry. Whether you’re a consumer looking for what new game to buy or a developer looking for what genres make the most sense to invest in, our interactive experiences are for you. List of potential questions:
    - What genre generates the most sales?
    - What genre gets the best reviews?
    - What country generates the most sales?
    - What publishers are the most successful in each genre?
    - What publishers generate the most revenue?
    - Are certain genres more popular in certain countries?
    - Do certain genres generate more revenue?
    - What are the most popular games in each genre (based on sales or user/critic review)?
    - What years had the most sales?
    - What years had the most popular games (based on user/critic review)?
    - Gross sales overall by Genre, Publisher, Country?
    - Do certain Ratings get better reviews (Mature, Everyone, Teen, etc.)?
    - Top Developers by Genre?
<br/><br/>

- <strong><i>Step 7</i></strong>: After establishing a set of core questions that we hoped to address, we then created a series of Flask App routes that mapped to specific URLs in order to pull various types of data. We started off with broad queries just to ensure that the data came through properly and that we were able to properly map them to various visualizations.
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/app_route_apis.png?raw=true" alt="app.route functions"><br/>
<br/>


- <strong><i>Step 8</i></strong>: We then created a series of d3.json functions that pulled the data for the corresponding charts. Using loops, lists, and variables, we were able to pull, store, and reference the desired metrics. Due to roadblocks with our data format and visualization decisions made earlier in the project, Javascipt code needed to be added to each HTML page directly, rather than being called from a separate js file. Although we hope to fix as a future enhancement, this was the path of least resistance at the time of writing this README.md
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/d3_json_completedata_function.png?raw=true" alt="Snapshot of d3.json function"><br/>
<br/>

- <strong><i>Step 9</i></strong>: We then used <a href="https://plotly.com/javascript/">Plotly</a> to create a variety of visualizations, including bar charts, bubble charts, and gauge charts. The color schemes of each of these visualizations were adjusted to match the designs initially set out in our bare bone HTML files.<br/>
<br/>

- <strong><i>Step 10</i></strong>: Rinse and repeat of Steps 8 & 9 in order to generate the functions and charts that we agreed upon in our mockup <br/>
<br/>

- <strong><i>Step 11</i></strong>: Identified an additional Javascript library, Google Charts, to leverage in our visuals per Project Requirements. We chose to use the <a href="https://developers.google.com/chart/interactive/docs/gallery/geochart">GeoChart</a> visualization as it easily integrated with our existing infrastructure and allowed us to adjust the look and feel, which we would later use to match the color scheme of our CSS
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/google_geochart.png?raw=true" alt="Google GeoCharts example">
<i>via Google </i><br/><br/>

- <strong><i>Step 12</i></strong>: We then created a PANEL variable that leveraged the d3.select function to select the div where we would enter text-based data for each genre. This includes Total Games, Total Sales, Top Game, Top Publisher, and Top Developer, each of which has their own SQL queries and APIs in order to pull the top performer for each genre and category
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/panel_html.png?raw=true" alt="PANEL.html function"><br/><br/>

- <strong><i>Step 13</i></strong>: Once all our visualizations and data points were finalized, we then focused on the HTML & CSS components to enhance the look & feel of our dashboard. By leveraging a combination of CSS from a <a href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"> previous assignment</a>, templates from <a href="https://www.free-css.com/free-css-templates/page290/digimedia">free-css.com</a>, and custom CSS, we were able to develop a base design for all our pages. Each page would be filtered to only show data for a specific genre and also include a global navigation with links to the dashboard, our data set, resources used, about us section, and our GitHub repo as well as a sub-navigation on dashboard pages that allows users to flip between All Genres or a specific Genre.
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/dashboard_view.png?raw=true" alt="dashboard preview"><br/>
<br/>

- <strong><i>Step 14</i></strong>: After tinkering with the design to meet our standards, the primary dashboard.html file was then duplicated and filtered for each genre, and then linked in the sub-navigation. As noted above, each genre had its own dedicated html file (see below)
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/html_files.png?raw=true" alt="html files"><br/>
<br/>

- <strong><i>Step 15</i></strong>: Once our dashboard was complete, we used the interactive visualizations to begin answering some of the questions we asked at the outset of this project
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/key_findings.png?raw=true" alt="key findings">

 - Key findings
    - The Action genre had more games than any other genre in the dataset
    - Games in the Action genre received the highest overall reviews from both Critics and Users
    - Games in the Action genre generated the most sales in North America & Europe
        - However, games from the Role-Playing genre generated more sales in Japan
    - The Action genre comprised of ~23% of all Global Sales
    - Wii Sports, a game belonging to the Sports genre, generated by far the most Global Sales out of any game in the dataset
    - Electronic Arts (EA) is the Publisher with the best overall Critic Score
    - Games Rated "E" generated the most Global Sales
        - Games Rated "M" had the second highest Global Sales. It was interesting to see both sides of the spectrum be top performers
    - North America was the biggest market in terms of Sales
    - Sports games made up the majority of sales out of the Top 10 Games in Global Sales
    - While games in the Puzzle & Strategy genres generated the least Global Sales, they ranked amonst the highest in terms of Critic & User scores
<br/>

- <strong><i>Step 16</i></strong>: Using the template we selected from <a href="https://pptmon.com/">PPTMON</a>, we then began crafting our presentation. To create a consistent look and feel, these visuals were repurposed throughout all areas of our project deliverables<br/><br/>

- <strong><i>Obstacles faced</i></strong>:
    - Our data was not compatible with the templates provided in class. For this reason, the majority of our project needed to be created from scratch
    - Similar to the above, our Javascript could have been executed more efficiently, if our dataset was formatted properly
    - Since our dataset used a combination of regions and countries, it made it difficult to plot data on maps as you can typically only choose one or the other, not both. For this reason, we were only able to create a GeoChart for countries and could not include Europe
    - Learning curve with multiple team members using GitHub pulls, pushes, etc. <br/><br/>

### Final Dashboard Screenshots
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/dashboard_view.png?raw=true" alt="dashboard preview">
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/bar_bubble_charts.png?raw=true" alt ="Bar graph & Bubble Chart">
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/bar_geo.png?raw=true" alt="Bar graph & geo chart">
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/top_10_all_games.png?raw=true" alt="Top 10 and all games - bar charts">
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/ratings_criticscores.png?raw=true" alt="Ratings and Critic Scores">
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/criticscores_footer.png?raw=true" alt="Critic Scores & Footer">
<br/>

### Other Site Areas
<strong><i>About Page</i></strong>
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/homepage.png?raw=true" alt="About page">

<strong><i>Resources Page</i></strong>
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/resources_page.png?raw=true" alt="Resources page">

<strong><i>About Us Page</i></strong>
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/about_us_page.png?raw=true" alt="About us page">

## Presentation
- View presentation <a href="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/resources/group1_video_game_analysis.pdf">here</a>

## How to Run
1. Download the project files & review the requirements.txt file
2. Run the initial SQL queries and upload the provided CSVs to the corresponding tables
```sql
    CREATE TABLE video_game_info (
        uniqueid INT,
        name VARCHAR,
        yearreleased INT,
        genre VARCHAR,
        publisher VARCHAR,
        developer VARCHAR,
        rating VARCHAR,
        CONSTRAINT pk_video_game_info PRIMARY KEY (
        uniqueid
     )
);

    CREATE TABLE video_game_sales (
        uniqueid INT,
        name VARCHAR,
        nasales FLOAT,
        eusales FLOAT,
        jpsales FLOAT,
        othersales FLOAT,
        globalsales FLOAT,
        CONSTRAINT pk_video_game_sales PRIMARY KEY (
        uniqueid
     )
);

    CREATE TABLE video_game_scores (
        uniqueid INT,
        name VARCHAR,
        criticscore INT,
        criticcount INT,
        userscore FLOAT,
        usercount INT,
        CONSTRAINT pk_video_game_scores PRIMARY KEY (
        uniqueid
     )
);

    ALTER TABLE video_game_sales ADD CONSTRAINT fk_video_game_sales_uniqueid FOREIGN KEY("uniqueid")
    REFERENCES video_game_info ("uniqueid");

    ALTER TABLE video_game_scores ADD CONSTRAINT fk_video_game_scores_uniqueid FOREIGN KEY("uniqueid")
    REFERENCES video_game_info ("uniqueid");
```
3. Run the second set of SQL queries to create the completedata table. This will be the primary table used in the Flask API
```sql
    CREATE TABLE completedata AS
        SELECT vgi.uniqueid,vgi.name, vgi.yearreleased, vgi.genre, vgi.publisher, vgi.developer, vgi.rating,
        vgs.nasales, vgs.eusales, vgs.jpsales, vgs.othersales, vgs.globalsales,vgsc.criticscore, vgsc.criticcount, vgsc.userscore, vgsc.usercount
        FROM video_game_sales AS vgs JOIN video_game_info AS vgi
        ON vgs.uniqueid = vgi.uniqueid
        JOIN video_game_scores AS vgsc
        ON vgsc.uniqueid= vgi.uniqueid
```
4. Create a config.py file and enter your pgAdmin credentials. Ensure to add this in the main folder
```python
username = ""
password = ""
hostname = ""
port = ""
db = "videogamesales"
```

5. Install psycopg2, if necessary
```bash
!pip install psycopg2
```

6. Open Anaconda Prompt/Terminal depending on your device and cd to your folder location and run
```bash
python app.py
```
7. Copy your development server into your browser and enjoy!

-------------------------
## Requirements
For Project 3, you will work with your group to tell a story using data visualizations. Here are the specific requirements:
- Your visualization must include a Python Flask-powered API, HTML/CSS, JavaScript, and at least one database (SQL, MongoDB, SQLite, etc.).
- Your project should fall into one of the following three tracks:
    - A combination of web scraping and Leaflet or Plotly
    - A dashboard page with multiple charts that update from the same data
    - A server that performs multiple manipulations on data in a database prior to visualization (must be approved)
- Your project should include at least one JS library that we did not cover.
- Your project must be powered by a dataset with at least 100 records.
- Your project must include some level of user-driven interaction (e.g., menus, dropdowns, textboxes).
- Your final visualization should ideally include at least three views.

### Data Cleanup and Analysis
Now that you’ve picked your data, it’s time to tackle development and analysis. This is where the fun starts!

The analysis process can be broken into two broad phases: (1) exploration and cleanup, and (2) analysis.

As you’ve learned, you’ll need to explore, clean, and reformat your data before you can begin answering your research questions. We recommend keeping track of these exploration and cleanup steps in a dedicated Jupyter notebook to keep you organized and make it easier to present your work later.

After you’ve cleaned your data and are ready to start crunching numbers, you should track your work in a Jupyter notebook dedicated specifically to analysis. We recommend focusing your analysis on multiple techniques, such as aggregation, correlation, comparison, summary statistics, sentiment analysis, and time-series analysis. Don’t forget to include plots during both the exploration and analysis phases. Creating plots along the way can reveal insights and interesting trends in the data that you might not notice if you wait until you’re preparing for your presentation. Presentation requirements will be further explained in the next module.
<center><img src="https://media1.giphy.com/media/fAD9SMlNWp0k84Ra1G/giphy.gif?cid=ecf05e47ymo4d66y72dp78ty0vvfrzyls5equ8i5rchv0ln4&rid=giphy.gif&ct=g" alt="video game GIF via GIPHY.com"</center>