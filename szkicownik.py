dict = {"I":"you", "me":"you", "my": "your", "you": "I"}
list = ["I", "me", "my", "you"]
text = "Do you think that it is true?"


for elem in list:
    if (text.__contains__(elem)):
        person = (dict.get(elem))

# <li>Yes, it is.</li><li>You think so?></li>