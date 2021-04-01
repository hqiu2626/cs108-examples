Navigating the Spoonacular+Firebase portion of the application:
1. Log in or create an account on the authentication page (connected to firebase)
	- Log in with already created account: 
		- username: henryqiu@gmail.com
		- password: 123456
	- Create an account (fields cannot be left empty and password must be longer than 6 characters)

2. Once the user logs in or creates an account, the user is directed to the main page that uses the Spoonacular API

3. User can type in any type of cuisine (i.e. italian) in the first field and press the "Submit1" button to retrieve a recipe relevant to the cuisine with an id number
	- currently, only one recipe is displayed for demonstration purposes

4. User can also type in any list of ingredients (i.e. eggs, spinach) in the second field and press the "Submit2" button to retrieve a recipe most relevant to the requested ingredients
	- user can write multiple ingredients but must be separated by a comma
	
5. User can type in an id number from the earlier requested recipes (i.e. 648271) in the third field and press the "Submit3" button to retrieve the recipe matched with the given id for a more detailed response (i.e. ingredients of the recipe)
	- currently, not all information is displayed for demonstration purposes 

6. The user can save the recipe in the database for future reference by pressing the "Save" button

7. The user can look at the saved recipes in the database by pressing the "Saved Recipes" button

8. To see the saved recipes, the user can press the "Display" button
	- currently, the app only shows the first created recipe stored in the database but will be implemented later to show all

9. The user can go back by pressing the "Back" button or logout by pressing the "Logout" button
