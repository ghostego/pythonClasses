import webbrowser

# webbrowser.open("https://www.python.org")

# help(webbrowser)

# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep="; ", end="\t")

chrome = webbrowser.get(using='chrome') # if this doesnt work use webbrowswer.get('chrome $s').open("https://www.python.org")
chrome.open_new("https://www.python.org")

safari = webbrowser.get(using="safari")
safari.open_new("http://www.witchesandbling.com")