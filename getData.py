import praw
import json
import pandas as pd

reddit = praw.Reddit(client_id='lOJMrEgYuTKbHnTSbZ9MLg', client_secret='Uu_2r21osuQPGbpyd-FZwnmR53Iecg', user_agent='funnyadvice')
shitty_advice = reddit.subreddit('shittyadvice')
hot_posts = shitty_advice.top(limit=100)
data = {}
i = 0




with open("redditData.jsonl", "w") as outfile:
	outfile.truncate(0)
	posts = list(hot_posts)
	for post in posts[:6]:

		comments = list(post.comments)
		for comment in comments[:3]:
			dict = {"prompt": post.title, "completion": comment.body}
			json.dump(dict, outfile)
			outfile.write('\n')

		# data[post.title] = [comment.body for comment in comments[:3]]
		# print(data[post.title])
		print(i)
		i += 1


# df = pd.DataFrame(data,columns=['title', 'comments'])
# csv = df.to_csv('redditData.csv')

