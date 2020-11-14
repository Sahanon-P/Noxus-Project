# Noxus-Project
## League’s Insights

![Noxus](darius-god-king.jpg)

   -- ***By my hand will NOXUS rise*** --

## Description 
             
   - A web-application providing analytical insights of the game “League of Legends” such as win rates, most played builds and most used characters presented in a way of data visualization to make users be able easily understand the complex in-game data and utilize the information they gained to make somewhat beneficial decisions in their gameplays whether they be pro-players or beginners.
Signing in is not necessary to view our website, unless the user wants to subscribe and receive news about our latest updates. If so, they can sign up or subscribe with their email to help us grow our lovely league of legends community.

## Development Plan

<details>
  <summary> ITERATION 1 </summary>
  <p> 

#### PRIORITY
1. Proposal [Single mode + Review]
2. Wiki [Single player]
3. Project Task board [Single player]
4. index.html [1-2 player]
	- Contact us [Single mode]
	- Blank champion page [Single mode]
5. CSS stylesheet[Co-op]
6. Server[Deploy]

#### GOAL
1. Create Homepage and Contact us.
2. Manage Wiki and Readme.

#### FEATURES
1. Home page.
2. Contact Us page.

#### ACCEPTANCE CRITERIA
1. Home page working and stable.
2. Wiki look good and easy to read.

</p>
  </details>

<details>
  <summary> ITERATION 2 </summary>
  <p> 

#### PRIORITY
1. Find data sources
2. Mine data
3. Search bar function
4. Github page availability
5. Improves Home page

#### GOAL
1. Readable champions data.
2. Search bar.
3. Improved Home page.

#### FEATURES
1. json data.
2. Search function

#### ACCEPTANCE CRITERIA
1. Available data for next iteration.

</p>
  </details>

<details>
  <summary> ITERATION 3 </summary>
  <p> 

#### PRIORITY
1. Models Planning
2. Champion Class
3. Contact us Page
4. User experience report.
5. GUI improvement according to UX.

#### GOAL
1. Contact us Page.
2. Improves designs of GUI.
3. Viable Models for database.

#### FEATURES
1. Contact_us.html

#### ACCEPTANCE CRITERIA
1. Working Contact us Page.
2. Possibly improved GUI.
3. Finished Models class.

</p>
  </details>
  
  <details>
  <summary> ITERATION 4 </summary>
  <p> 

#### PRIORITY
1. Viable Models for database.
2. Web app model.

#### GOAL
1. Contact us Page.
2. Home page.
3. Viable Models for database.

#### FEATURES
1. Index.html.
2. Contact_us.html.

#### ACCEPTANCE CRITERIA
1. Working contact us and home page.
2. Working Model data base for web app.

</p>
  </details>

<details>
  <summary> ITERATION 5 </summary>
  <p> 

#### PRIORITY
1. Continue database models.
2. Merging all page together. 
3. Admin logging.

#### GOAL
1. Merging all page.
2. Viable Models for database.

#### FEATURES
1. Admin login

#### ACCEPTANCE CRITERIA
1. Working Web application.
2. Working admin page.
3. Working admin logging
4. Finished Models class.

  </p>
</details>
  
**Code Review Checklist** --> [here](../../wiki/Checklist)

**Code Review Procedure** --> [here](../..wiki/Procedure)

## Installation Guide for local running server
1. Clone this repository
In your directory type this command.    
`git clone https://github.com/Sahanon-P/Noxus-Project.git`    
2. After you clone the repository, In the project directory please type this command    
` python manage.py migrate `    
in order to migrate all the module that use in this webapp.    
3. Our webapp use external data from website so in order to make the webapp run correctly you need to read and save data from our sources.    
	- In the project directory please type this command.    

	   `python manage.py shell`    
	   For database saving.    

	- After you get into the shell please type this commands. 

	   `exec(open("update.py").read())`    
	   This will take you a few minutes depends on your internet connection.  

	- Then please type these 3 commands as order.    

	   ```
	   exec(open("items_update.py").read())  
	   exec(open("rune_update.py").read()) 
	   exec(open("update_summonner_spell.py").read())    
	   ```

	- Then you can type `python manage.py runserver` to see our webapp.    
	  You can type the port number as you like after the `runserver` command.    
	  For example.  
	  `python manage.py runserver 9000 `
