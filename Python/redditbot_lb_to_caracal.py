import praw


reddit = praw.Reddit(
    client_id = "",
    client_secret = "",
    username = "",
    password = "",
    user_agent = "<>"
)
subreddit = reddit.subreddit("[Sub of your choice]")

print("still running")

hot_posts = subreddit.hot(limit = 5)
new_posts = subreddit.new(limit = 5)
print("running")

for submission in new_posts:
    print("moving on to next submission")
    title = submission.title
    if "lbs" in title:
        title_list = title.split()
        for title in title_list:
            if "lbs" in title:
                split_lb_part = title.split("l")
                split_lb_part.pop(1)
                lb_amount = split_lb_part[0]
                print(lb_amount)
                weight_in_floppa = lb_amount / 35, 5
                submission.reply(f"{lb_amount} lbs is around {weight_in_floppa}. I am a bot and I hope this conversion could help you visualize {lb_amount} lbs")