import re
import wikipedia
import time

def describing_chuck_norris_finder():
    """
    This function gets a random wikipedia page
    then scans that page to find if it has a sentence has a phrase describing things that Chuck Norris is/does/was/will be in the future using regex and prints the paragraph where the sentence occurs to the screen if it does, else keeps trying random pages until you find one that does have a match.
    """
    # get a random wikipedia page
    try:
        random_page = wikipedia.random(pages=1)
        # get the content of the page
        page_content = wikipedia.page(random_page).content
        # split the content into paragraphs
        paragraphs = page_content.split('\n')
        # compile the regex
        regex = re.compile(r'Chuck Norris (was|is|will be|has been) (a|an|the) (\w+)')
        # loop through the paragraphs
        for paragraph in paragraphs:
            # search for the regex
            match = regex.search(paragraph)
            # if there is a match
            if match:
                # print the paragraph
                print('\n')
                print(paragraph)
                # break out of the loop
                break
            # if there is no match
            else:
                # sleep for 1 second
                #time.sleep(1)
                # try again
                print('.',end='')
                describing_chuck_norris_finder()
    except Exception as e:
        # if there is an error sleep for 1 second
        time.sleep(1)
        # try again
        describing_chuck_norris_finder()

# call the function
describing_chuck_norris_finder()