This projects is used to track your habit, for example workout activity,... using Google Sheet

* type in what you did
* the api will automatically update your data in google sheet(date,time,excercise, duration of the workout, how many calories you used for this workout)

***
USAGE TUTORIAL
* Go to the Nutritionix API website: https://www.nutritionix.com/business/api and select "Get Your API Key" to sign up for a free account.
* go to this link and create a copy of the My Workouts Spreadsheet. You may need to login/register.
"https://docs.google.com/spreadsheets/d/1E5LwCfkizAxpBmzvF6jcjsASSVShR7DtFHi37EYrQXc/edit#gid=0"
* Set up your google sheet with sheety used this link:"https://sheety.co/. Login with your google sheet acount and make sure you give sheety permission to access and edit google sheet by click in "See, edit,create and delete all your google spread sheets".
* Under your Google Account Security settings, you should see that Sheety has access. Double-check that you see Sheety listed as an authorized app.
* In your project page, click on "New Project" and create a new project in Sheety with the name "Workout Tracking" and paste in the URL of your own "My Workouts" Google Sheet.
* In your sheety acount, click on "API"-> "workouts" and enabled "GET", "POST","PUT", "DELETE"
* copy your "POST"API link and change in row 11 i main.py for sheety_post_endpoint
* Sheety expect your record to be nested in a root property.
  (for exp, if your sheety_post_endpoint is "https://api.sheety.co/9d464d54e93643d616111bc10cf215f6/myWorkouts/workouts" ends with "workouts" then nested you workout record with "workout" like in main.py rows 46
