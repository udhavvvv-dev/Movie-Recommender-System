# Movie Recommender System // Content Based Movie Recommender System

Movie Recommender System is the python Based Project To Create Content Based Recommender System using TMDB 5000 movie dataset from kaggle

Link: https://u-rex13-movie-recommender-system-app-2ap1dd.streamlit.app/

* * *

### Steps To Run This Project:

1) Fisrt Downlod the zip folder of project and unzip the folder 

2) Install Python and Visual Studio code using below given link
   - Python Desktop Application: "https://www.python.org/downloads/"
   - Visual Studion Code IDE: "https://code.visualstudio.com/download"

3) Open the project folder inside the visual studio code

3) Install the below given libery in command prompt or visual studio code terminal

![image](https://user-images.githubusercontent.com/109918405/192830267-8050f9cb-bfa1-4834-b55f-744d34b4f870.png)

Below are python libery command before run this project you make sure to run all command in terminal 

```
pip install streamlit
```
```
pip install pickle-mixin
```
```
pip install pandas
```
```
pip install requests 
```
  
  4)Afte installing the project required python libery we return use termianl to run our project using simple command.
  ```
  streamlit run app.py
  ``` 
  (meaning of the line is "streamlit" is package name that we are used to create this web app and run meaning to "run" this project using streamlit and "app.py" is the python file that i create the frontend of this project if in any other situation it can different if you create by own using other name so it is differnet name python extension file) 
 
 5) after you run this line the streamlit create a localhost in your machine and run this web application using browser

  - This is the localhost that streamlit is host our web application
![image](https://user-images.githubusercontent.com/109918405/192834944-1e2d0332-d2b3-4fc0-a347-35cd7349b8c3.png)

  - This is user interface that you see after it launch in browser
![image](https://user-images.githubusercontent.com/109918405/192835386-36aee8e5-c6e7-4e37-b241-04c4adc0b9c2.png)
  
  - You can search the movie from list or you can just type the movie name
![image](https://user-images.githubusercontent.com/109918405/192835852-e81e98d3-b00d-41c2-9259-acb7f974901f.png)

  - The Result Screen you get after you search movie and get suggested by movie recommendation model
![image](https://user-images.githubusercontent.com/109918405/192836167-4f05161b-1e46-4c52-b1b3-48a57bf94ece.png)

* * *

### what is role of each file in this or what it contain

![image](https://user-images.githubusercontent.com/109918405/193418292-261579f4-3b6e-4801-83d3-b8d0d9aeebea.png)

- **".git"** file it automatically created when we initiative or init github repository to over local project folder.
- **"git attributes"** file contain some command that help while hosting the project on any web services and in my case ill also use "Git LFS" to uplod some big size data file in same repositery so it also contain that lfs code to track that files.
- **"git ignore"** file tells Git which files to ignore when committing your project to the GitHub repository.
- **"app.py"** this file contain the frontend and backend recommendation model implemenation to present in web application using python libery "streamlit"
- **"movie_dict.pkl"** this pickle file we generated using movie-recommender-system in jupyter system this file contain the dataset that we use in project but in dictonary format but some checking and error solving purposes.
- **"movie-recommender-system.ipynb"** this this jupyter notebook file in this we created the movie recommendation model and in this we filer the movie dataset that we use for recommendation
- **"movies.pkl"** it filter data we created to use but strealit doesnt support pandas file so use and refilter this file with other name.
- **"Procfile"** A Procfile is a mechanism for declaring what commands are run by your application's containers on the Deis platform. It follows the process model. You can use a Procfile to declare various process types, such as multiple types of workers, a singleton process like a clock, or a consumer of the Twitter streaming API
- **"readme"** it file contain information about our project it didnt use for deployment purpose.
- **"requirements"** it file we have to generate in terminal using command to get requirements file to know deployment mechnism what we requirement we want and we have 
- **"setup.sh"** defines Bourne or Korn shell environment variables necessary to build an InfoCrafter database from the command line using the icft command. The setup.sh file sets the TOOLSDIR and TOPLEVEL_BUILDDIR variables. it is use for deployement
- **"similarity.pkl"** it is file that we convert from pandas to pickle so streamlit can support
- **"tmdb_5000_credits.csv"** it is movie credits dataset that we have using in this project
- **"tmdb_5000_movies.csv"** it is also a dataset that contain of movie id,tag,cast,crew,gener etc
   - we have both dataset file but stil you want to explore other dataset you can checkout kaggle website and i gave you this dataset site also
      - Kaggle to find other dataset likes or other things also (https://www.kaggle.com/datasets)
      - TMDB 5000 Movie Dataset that we are using (https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)


* * *

### what is content based recommendation system:

- Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback.
- For Example Suppose User1 Like a "Iran Man" movie and rate the movie 4.5 out 5 and similarly the User2 like the same "Iran Man" and give the rating similarily to User1 so they both have equal choice in Sci-Fi movie Genre so basically the machine learning model observe the patent and next time the model suggest the movie or anything other thing according to what we want him to suggest, the model suggest the iteam according the tag system of iteam
- if you want to know more about content based recommendation system here are some blog that you can read
   - https://developers.google.com/machine-learning/recommendation/content-based/basics#:~:text=Content%2Dbased%20filtering%20uses%20item,previous%20actions%20or%20explicit%20feedback.
   - https://www.kdnuggets.com/2020/07/building-content-based-book-recommendation-engine.html

* * *
