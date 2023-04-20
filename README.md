# Video Game Analysis
Overview: Using a Python Flask-powered API, HTML/CSS, Javascript and SQL to test hypotheses about video game sales
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/main/images/video_game_header.png?raw=true">

## Background Information
The team will leverage a Global Video Game Sales & Ratings dataset from <a href="https://www.kaggle.com/datasets/thedevastator/global-video-game-sales-ratings">Kaggle,/a> in order to test various hypotheses about video game genres.


## Process
- Step 1: Creating Jupyter Notebook to load, clean, and export Excel files as CSVs as well as setting up sqlalchemy, config.py, .gitignore, pip install, etc.
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/main/images/jupyter_notebook.png?raw=true" alt="Jupyter Notebook preview">


- Step 2: Creating an ERD Diagram using https://app.quickdatabasediagrams.com/ to develop SQL schema and assign the correct data types to all of our columns
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/main/images/ERD_Process.png?raw=true" alt="ERD Diagram via quickdatabasediagrams.com">


- Step 3: Leveraging pgAdmin 4 to clean our data, create tables, and merge datasets. In order to have a single database for our Flask APIs, we joined the (3) datasets on "uniqueid" and selected the appropriate columns to avoid duplicate values
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/main/images/postgres_sql_steps.png?raw=true" alt="SQL steps">


- Step 4: Once our database was created, we developed a barebone HTML file with corresponding CSS & Javascript to test if our data was being pulled properly. In order to connect our files to the database, we first imported the create_engine function from sqlalchemy as well as a number of other dependencies. In addition, we created a config.py file to store our individual database credentials, stored them / imported them as variables, and used them in our create_engine function f string.
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/app_py_file.png?raw=true" alt="Preview of app.py file">


- Step 5: Once our database was connected, we leveraged Google Slides to mock up what our potential dashboard could look like. This allowed us to quickly move things around, plan what specific metrics / visualizations we wanted to develop, and identify the proper next steps to achieve our goal. This served as our starting point and helped us understand the details of what needed to be done and what questions we hoped to answer.
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/dashboard_mockup.png?raw=true" alt="Preliminary dashboard mockup">


- Step 6: Once we had a general idea of what our dashboard could look like, we began developing a list of potential questions that our dashboard could answer. Building off our story from Project 1, where we assessed ticket prices & events for Music & Sports genres, our goal was to do an in-depth assessment to glean various insights on video game genres. Our goal as a group is to continue developing insights for producers, developers, and consumers alike in order to make data-driven decisions about the entertainment industry. Whether you’re a consumer looking for what new game to buy or a developer looking for what genres make the most sense to invest in, our interactive experiences are for you. List of potential questions:
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


- Step 7: After establishing a set of core questions that we hoped to address, we then created a series of Flask App routes that mapped to specific URLs in order to pull various types of data. We started off with broad queries just to ensure that the data came through properly and that we were able to properly map them to various visualizations.
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/app_route_apis.png?raw=true" alt="app.route functions">



- Step 8: We then created a series of d3.json functions that pulled the data for the corresponding charts. Using loops, lists, and variables, we were able to pull, store, and reference the desired metrics. Due to roadblocks with our data format and visualization decisions made earlier in the project, Javascipt code needed to be added to each HTML page directly, rather than being called from a separate js file. Although we hope to fix as a future enhancement, this was the path of least resistance at the time of writing this README.md
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/d3_json_completedata_function.png?raw=true" alt="Snapshot of d3.json function">


- Step 9: We then used <a href="https://plotly.com/javascript/">Plotly</a> to create a variety of visualizations, including bar charts, bubble charts, and gauge charts. The color schemes of each of these visualizations were adjusted to match the designs initially set out in our bare bone HTML files.


- Step 10: Rinse and repeat of Steps 8 & 9 in order to generate the functions and charts that we agreed upon in our mockup 


- Step 11: Identified an additional Javascript library, Google Charts, to leverage in our visuals per Project Requirements. We chose to use the <a href="https://developers.google.com/chart/interactive/docs/gallery/geochart">GeoChart</a> visualization as it easily integrated with our existing infrastructure and allowed us to adjust the look and feel, which we would later use to match the color scheme of our CSS
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/google_geochart.png?raw=true" alt="Google GeoCharts example">
<i>via Google </i>


- Step 12: We then created a PANEL variable that leveraged the d3.select function to select the div where we would enter text-based data for each genre. This includes Total Games, Total Sales, Top Game, Top Publisher, and Top Developer, each of which has their own SQL queries and APIs in order to pull the top performer for each genre and category
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/panel_html.png?raw=true" alt="PANEL.html function">



- Step 13: Once all our visualizations and data points were finalized, we then focused on the HTML & CSS components to enhance the look & feel of our dashboard. By leveraging a combination of CSS from a <a href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"> previous assignment</a>, templates from <a href="https://www.free-css.com/free-css-templates/page290/digimedia">free-css.com</a>, and custom CSS, we were able to develop a base design for all our pages. Each page would be filtered to only show data for a specific genre and also include a global navigation with links to the dashboard, our data set, resources used, about us section, and our GitHub repo as well as a sub-navigation on dashboard pages that allows users to flip between All Genres or a specific Genre.
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/dashboard_view.png?raw=true" alt="dashboard preview">


- Step 14: After tinkering with the design to meet our standards, the primary dashboard.html file was then duplicated and filtered for each genre, and then linked in the sub-navigation. As noted above, each genre had its own dedicated html file (see below)
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/html_files.png?raw=true" alt="html files">

### Final Dashboard Screenshots
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/dashboard_view.png?raw=true" alt="dashboard preview">
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/bar_bubble_charts.png?raw=true" alt ="Bar graph & Bubble Chart">
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/bar_geo.png?raw=true" alt="Bar graph & geo chart">
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/top_10_all_games.png?raw=true" alt="Top 10 and all games - bar charts">
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/ratings_criticscores.png?raw=true" alt="Ratings and Critic Scores">
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/criticscores_footer.png?raw=true" alt="Critic Scores & Footer">


### Other Site Areas
About Page
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/homepage.png?raw=true" alt="About page">

Resources Page
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/resources_page.png?raw=true" alt="Resources page">

About Us Page
<img src="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/images/about_us_page.png?raw=true" alt="About us page">

## Presentation
View presentation <a href="https://github.com/mshawn12/video-game-sales-analysis/blob/mydashboard/resources/group1_video_game_analysis.pdf">here</a>


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