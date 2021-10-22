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
    if "[weight_unit]" in title:
        title_list = title.split()
        for title in title_list:
            if "[weight unit of your choice]" in title:
                split_[weight_unit]_part = title.split("[first letter of your weight unit]")
                split_[weight_unit]_part.pop(1)
                [weight_unit]_amount = split_[weight_unit]_part[0]
                print([weight_unit]_amount)
                weight_in_[weight_unit] = [weight_unit]_amount / [conversion_rate]
                submission.reply(f"{lb_amount} lbs is around {weight_in_[weight_unit]}. I am a bot and I hope this conversion could help you visualize {[weight_unit]_amount} [weight_unit]")