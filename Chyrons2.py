import requests
import csv
import time


# This is the file location. You won't see this again until the very end of our program. If you're on windows you'll need to use \\ instead of / to define your filepath.
outputFile = open(r'C:\Users\jholzbau\Desktop\Misc\jholzbau\Chyrons.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

# requests acts like your browser. It opens a url, but rather than taking the tike to render it in a viewable display, it just returns the html of the page
response = requests.get('https://archive.org/services/third-eye.php?last=24')
# JRH: if response doesnt work for some crazy reason, you can try export? like you did in your download all folder.

# If for whatever reason the above request fails, raise_for_status() will throw an error (which is good since there's no point in proceeding further)
# Get = open up a page for me.
# Post = more for exchanging data back and forth securely, because it's encrypted.
# Put = change something. Cowdy uses rarely.
# Delete = delete.

#JRH: basically checking for Web status = 200 (bueno). If not 200, let's just quit early, cuz the rest of this isnt' going to work.
response.raise_for_status()

outputWriter(outputFile)
#Cowdy: there is where my new script fails.  I get this error: "TypeError: '_csv.writer' object is not callable"  How do i Fix?

# This will just slow our program down so we don't hammer the CBS site too quickly and get our ip limited / banned
time.sleep(.2)

# Don't forget to close your file otherwise you end up with fun locking issues
outputFile.close()
