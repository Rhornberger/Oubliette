## Oubliette
​
## Project Overview
​
- Random character generator
- Quick-reference for spells, feats and skills
- Organizational platform for info DM's need to track in any given game
- Separate pages for each party member, including character sheets for each and other pertinent info
​
The goal is reduce the volume of reference materials necessary when playing tabletop RPG
​
- What libraries or frameworks will you use?
    -I need to do some research into what libraries might be of use to me.
    -I want to use django restframework for the account functionality.
    -I want to use Ajax for the DOM manipulation.
​
## Features
​
​
### User stories
​
"As a DM, I want to reference information (spells, feats, skills, classes, creatures, and race) easily and quickly."
​
- Create search field for each category
- Render results to page.
"As a DM, I want on-the-spot access to specific player information."
- Create player profiles and store in DB
- Include all character sheet info with all relevant stats.
"As a player, I want quick access to information pertinent only to my character."
- Initiate permissions giving:
  DM full read/write.
  players full read with partial write access.
"As a player or DM, I want quick access to game mechanic information."
- Create search for (eg) Combat rules regarding player/NPC interaction.
"As a DM, I need the ability to generate a character on demand during gameplay."
- Create DB table of character names
- Access table of races/classes and retrieve relevant information
- Outline base stats
​
#### Questions to ask yourself about functionalities
​
What will the user see on each page? What can they input and click and see? How will their actions correspond to events on the back-end?
-The user will see a homepage that prompts them to either sign into an existing user account or to create a new user account.
-Once a user account is initiated the user will have to option to start a party group, this will set them as the Dungeon Master and come with additional permissions.
-Once in the party group the user will be able invite friends into the party group. And from there be able to keep track of the info of the players in their party.
-Every user will have access to the quick reference functionality of the program, The DM will have the permissions similar to that of a super User in that the DM can change anything on any players charactersheet.
-Every player will be able to see basic info on other players in the party such as name, class, race however only the player conected to the character will be able to see all the info on that character. Only the user designated as DM will be able to make changes to anything on the character sheet. The users that are party members only will need to get a one time permission from the DM to make most changes to the character info. The exception to this will be dropping items from inventory.

​
## Data Model
​
'User'
'Player'
'DungeonMaster'
'Party'
'Spells'
'Classes'
'Races'
'Weapons'
'Armour'
'Equipment'
'Skills'
'Feats'
'Gameplay'
'Creatures'
'RandomGeneration'
​
## Schedule
​
Here you'll want to come up with some (very rough) estimates of the timeframe for each section, as well as milestones. State specifically which steps you'll take in the implementation. This section should also include work you're planning to do after the capstone is finished.

    **tentative schedule**
        -Days 1-3: Create my API for the Base informtion of Game play. This to include all info required for the quick reference functionality. Start on the base sketches for how I want my pages to present. (This is for the Pathfinder RPG and there is no publicly available API so I need to create my own with the necessary information)
        -Days 4-6: Create the functionality for the quick refernce. Be able to pull up the info based on input values.
        -Days 7-9: Create functionality for accounts and allow users to sign in and out and send invites to friends and initiate a new Party as DM.
        -Days 10-11: Create a form that acts as a charactersheet and saves all player info. This will allow read and write to the appropriate users based on previous stipulations.
        -Days 12-15: Use this time to finish and polish all css and fine tune any functionality that is not working as I would like.

    -What I want to accomplish after the capstone presentation: 
        -I want to add in a Partial Random character genterator so that NPC's can easily be created and so that if visitors are in from out of town and want to play with the paty during a game they can just decide what kind of character they want to play and the program will develop a character that will meet minimum requirements to match the rest of the party.
