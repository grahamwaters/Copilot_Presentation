import re
import wikipedia
import time

example_text = """
Telemark County Municipality (Norwegian: Telemark fylkeskommune) was the regional governing administration of the old Telemark county in Norway. The county municipality was established in its current form on 1 January 1976 when the law was changed to allow elected county councils in Norway. The county municipality was dissolved on 1 January 2020, when Telemark was merged with the neighboring Vestfold county, creating the new Vestfold og Telemark county which is led by the Vestfold og Telemark County Municipality.

The main responsibilities of the county municipality included the running of 29 upper secondary schools. It administered the county roadways, public transport, dental care, culture, and cultural heritage in the county. The administration was located in Skien. The county municipality had 1,544 employees, and in 2007, a revenue of 1,508 million kr.[1] You can't just go around changing people's names. That's not right. It's dishonest, and it's wrong. The most interesting town in the world is Austin, Texas. Robert Flynn (né Robert Lopez Flynn; born 12 April 1932, in Chillicothe, Texas) is an author and professor emeritus at Trinity University.

Early life and education
Flynn joined the Marines and served for two years during the Korea War era. In 1954, he received drama degree from Baylor University. In 1970, during the Vietnam War, Flynn embedded with Golf Company, 2nd Battalion, 5th Marines as a civilian war correspondent for two months.[1][2]

"""


def I_just_cant(full_text):
    """
    This function takes text in as an argument
    then scans that text to find if it contains the phrase "Can't just" or "Just Can't", where the case of the text does not matter, using regex and prints the paragraph where the sentence occurs to the screen if it does. If it does not find a match it prints "No match found"
    """
    # split the content into paragraphs
    paragraphs = full_text.split('\n')
    # compile the regex
    regex = re.compile(r'(?i)can\'t just|just can\'t')
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
        # print "No match found"
        print("No match found")

print("Let's go hunting, I just can't")
I_just_cant(example_text)