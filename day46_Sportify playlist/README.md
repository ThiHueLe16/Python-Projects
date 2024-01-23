### Top 100 Billboard song in Spotify 
this is used to create automatically a top 100 song playlist from top100 Billboard on a past day in Spotify
* Create a top100song in billboard 
* Add to your playlist in Spotify
***

### Usage tutorial
Step 1:
*Sign up for free in Spotify,  **use this link** 
```
URL = "http://spotify.com/signup/"
```
Step 2:
Go to the **developer dashboard** and create a new Spotify App:

```
URL = "https://developer.spotify.com/dashboard/"
```
(redirect link in your sportify app: https://example.com)

Step3: After create Spotify app, copy **Client ID** and **Client Secret** into python code. Enter your Spotify user name into Python code(row 31, "sp = spotipy.Spotify(auth_manager=SpotifyOAuth(...user name="...")")

Step4:Run code and enter the date, in which you want to create the top 100 playlist from Billboard 
