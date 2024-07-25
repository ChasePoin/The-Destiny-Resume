# The Destiny Resume #
## Summary ##
This is a tool to create a resume based on various destiny 2 stats, such as raids, dungeons, and titles. It was made as a fun side project.
The tool leverages the bungie API to get information about the player, translates and formats it, then sends it to gemini to create a summary.

## Necessities ##
For now, this is solely a private tool. Hence, you will have to get an API Key from bungie in order to make requests. To do this:
1. Go to Bungie.net and sign in.
2. Scroll down and go to the developer portal.
3. Press "Create New App"
4. Set the OAuth Client Type to "Confidential" and click the first box for scope ("Read your Destiny 2 Information...")
5. Set the following environmental variables (left is environmental variable name, right is what you should set it to from the page):
* bungie_client_id=your OAuth client_id
* bungie_client_secrert=your OAuth client_secret
* bungie_token=your API Key
Next, you will need to also get an API Key for gemini.
1. Follow this link: https://ai.google.dev/gemini-api/docs/api-key.
2. Press "Get an API Key."
3. Set the following environmental variable: 
* GOOGLE_API_KEY=your api key
This assumes you have the knowledge to create a python environment using the included environment.yml file and use it to run the program.
4. Finally, set the redirect URL. The redirect URL in grabbers.py is set as google.com. If you want to use that, just set the redirect URL in your application page to google.com.
5. If you want to use a different one you will also have to change the "placeholder_redirect" variable in grabbers.py to match.

## Using the Tool ##
Once you have all of the environmental variables set, simply run main.py; it will produce a link for you to follow. Follow this link and copy+paste the url back into where the program says to. This is to authenticate the tool to allow it to read your destiny 2 profile information. 
After a bit of time, a file named resume.txt should be produced. There is an example "resume.txt" included in the repo. Since the summary is AI, the formatting is not exactly the same for every single resume.
If an undesired result is produced (the AI is crazy sometimes) just delete resume.txt and try again.

## Misc ##
The code isn't perfect; the translator.py file function is very rough. There are a few adjustments and additions I would like to make and will try to make in the future. I currently want to add:
* A function to generate endpoint urls instead of just calling the url specifically in each grabber function.
* An argparser and function to allow for only certain parts of the three main categories (general, raid, dungeon) to be included in the resume.
* Cleaner code...
* Eventually, I want to create a public version of this and a front-end for the code.
