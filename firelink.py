import webbrowser
favourite_websites={
    "facebook":"https://www.facebook.com/",
    "youtube":"https://www.youtube.com/",
    "google":"https://www.google.com/"
}
def open_website(name):
    if name in favourite_websites.keys():
        link=favourite_websites[name]
        webbrowser.get('firefox').open(link)
    else:
        print("invalid choice")
    
        