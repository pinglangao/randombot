# import praw
# import spotify
#
#
# alexabot = praw.Reddit(user_agent = 'alexa_play_bot_2',
#                   client_id = 'obgVOv3lTA0JbQ',
#                   client_secret = 'sKCI6fZm9pHLy6WVUBNNuOIwV_8',
#                   username = 'alexa_play_bot',
#                   password = '990610Alexa')
#
# subreddit = alexabot.subreddit('testingground4bots')
#
# comments = subreddit.stream.comments()
#
# for comment in comments:
#     text = comment.body
#     author = comment.author
#     if ('alexa play' in text.lower()) & (len(text) > 11):
#         print (text)
#         print (text.index('alexa play') + len('alexa play '))
#         songtitle = text[text.index('al exa play ') + len('alexa play '):-1].split('.')[0]
#         # songtitle = text[0:3]
#         message = spotify.search_track(songtitle).format(author)
#         comment.reply(message)

import praw
from youtube2 import youtube_search

alexabot = praw.Reddit(user_agent = '_owl_bot_',
                  client_id = '-aS31v8n1AiB0A',
                  client_secret = 'Gb2b9IoMyM0h-JMz7yv0dZra19k',
                  username = '_owl_bot_',
                  password = 'hackrice')

subreddit = alexabot.subreddit('testingground4bots')

comments = subreddit.stream.comments()

for comment in comments:
    f = open('comments.txt', 'r+')
    commentIDs = f.read()
    f.close()
    if len(commentIDs) > 100:
        open('comments.txt', 'w')
    text = comment.body
    author = comment.author
    text = text.lower()
    if commentIDs.find(comment.id) == -1:
        if 'owlbot play ' in text:
            search = text[text.index('owlbot play ') + len('owlbot play '):]
            video = youtube_search(search)
            message = ("Now Playing: [%s](https://youtube.com/watch?v=%s)." % (video["snippet"]["title"], video["id"]["videoId"])).format(author)
            comment.reply(message)
            f1 = open('comments.txt', 'a+')
            f1.write(comment.id + " ")
            f1.close()
