# Data-Mining

# Instructions to get Started With Project

Github Link: https://github.com/CIS400-Social-Media/Data-Mining

1. Insure python is installed by running `python3 –-version` in terminal. Insure pip is installed by running `pip3 –-version` in terminal.
2. Open up the terminal and change your directory to a place you would like to save the project. Using Git clone the repository `git clone git@github.com:CIS400-Social-Media/Data-Mining.git` Use the ls command to verify the newly made Data-Mining project folder is in the directory
3. cd into the Data-Mining directory
4. `brew install python` (if you do not have python) in the terminal.
5. creating a virtual environment with the name venv type in terminal: `python3 -m venv venv`
6. activate the virtual environemnt type in terminal: `source venv/bin/activate`
7. install the dependent libraries type in terminal: `pip3 install -r requirements.txt` 
8. NOTE: Put all the dependecies and any packages you are installing in the requirments.txt file therefore it is easier for all team members to download all the dependices.

# How to run the application

1. Run trending.py to get all the top 10 trending videos for each country on Youtube with the specific category for each video and the overall sentiment for each video, all the data is stored in data.json.
2. Run happiness_analysis.py to get the correlation between happiness score and sentiment for all categories. 
3. Run freedom_index_analysis.py to get the correlation between freedom index and sentiment for all categories. 
4. Run life_expectancy_analysis.py to get the correlation between life expectancy and sentiment for all categories.
5. The interim result of analysis is stored in the output directory.
6. The correlation results are stored in the following csv files
    * category_correlation_happiness.csv
    * category_freedom_correlation.csv
    * category_life_expectancy_correlation.csv

7.  Run graphs.py with numeric argument to produce correlation graph for categories
    * 1 Gaming and Life Expectancy. 
    * 2 News & Politics and Happiness Score. 
    * 3 Sports and Happiness Score.
    * 4 Pets & Animals and Freedom Index.  
    * 5 Entertainment and Happiness Score. 

    For example, `python3 graphs.py 1`

