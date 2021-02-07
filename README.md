# Project1
In order to deploy/run: Flask, requests, os, and random are all required. (Also, the actual files are on the master branch, not the main one)

  # Improvements
Ideally there would be a much larger variety of songs to display, as well as further classification of said songs based on genre, and other features from the Spotify  API such as "danceability", "energy", etc... to give the user more information about the song. It would also be nice (If possible) for the preview to be embedded into the page, so that users could hear a slice of the song in addition to the available information.

  # Problems
No problems have been encountered so far. Regardless, I'm keeping my fingers crossed.

# Technical Issues that were overcome
Actually getting the data from Spotify was quite easy. I had to research on their website how exactly I was supposed to set up the authentication requests, but it was all straightforward. The hard part was actually converting the data I was recieving into something I could use. Since Spotify returns data in the form of a JSON (and a very hard to read JSON at that), I had to research parsing JSON objects in python and use https://jsonformatter.curiousconcept.com/# in order to properly view what I was looking at. This is where the majority of my time was spent. 

The other major issue I encountered was an error running the application. Specifically, the error was "OSError: [Errno 98] Address already in use", which seemed to be an error regarding the availability of the port I was running my application on. After numerous stack overflow searches, what eventually saved me was closing everything in the Cloud9 IDE, logging out of my account, and then restarting my computer. I'm not sure why, but the sage advice of "turn it off and back on" has remained my "old reliable" for problem solving.

Other than these two problems (and the mental trauma suffered from being logged out of AWS constantly whilst researching the Spotify API), I encountered no other issues.
