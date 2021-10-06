"""
This script is a badly named Reddit scraper.
It checks the amount of posts inputed by users and downloads the images.
Currently only supports images.
"""

import praw
import prawcore
import urllib.request

def main():

	reddit = praw.Reddit(client_id="id",
						 client_secret="secret",
						 username="name",
						 password="password",
						 user_agent="url-grabber"
						)

	sub:str     =   input("Subreddit name: ")
	limit:int	= 	int(input("How many?: "))



	downloaded:int      =    0
	skipped:int         =    0
	bad:int             =    0
	error_list:list 	=	 []


	subreddit = reddit.subreddit(sub)

	hot = subreddit.hot(limit = limit)
	try:
		for submission in hot:
		    url = submission.url
		    try:
		        if url.endswith('.jpg') or url.endswith('.jpeg') or url.endswith('.png') or url.endswith('.gif'):
		            filename = url.split('/')[-1]
		            urllib.request.urlretrieve(url, filename)
		            print(f'\nFile saved as {filename}')
		            downloaded+=1

		        else:
		            print('\nFile not saved. Not an image.')
		            skipped+=1
		    except Exception as e:

		        print(f'\nError: {e}')
		        bad+=1
		        error_list.append(e)

	except Exception as e:
		# List of exceptions that can occur
		if isinstance(e,prawcore.exceptions.Redirect):
			print('An error occured.\033[1m Is the subreddit name correct?\033[0m')
			return 0
		
		elif isinstance(e,prawcore.exceptions.RequestException):
			print('An error occured.\033[1m Is the internet connected?\033[0m')
			return 0
		
		elif isinstance(e,prawcore.exceptions.Forbidden):
			print('An error occured.\033[1m Is the subreddit set to private or banned?\033[0m')
			return 0

		elif isinstance(e,prawcore.exceptions.ResponseException):
			print('An error occured.\033[1m Are the client ID & client secret correct?\033[0m')
			return 0
		
		elif isinstance(e,prawcore.exceptions.OAuthException):
			print('An error occured.\033[1m Are the username and password correct?\033[0m')
			return 0
		
		else:
			print(f'An error occured. Detailed:\n{e}')
			print(f'\033[1m{type(e)}\033[0m')
			return 0

	print(f"\nStats:\nSubreddit: r/{sub}\nTotal: {limit}\nDownloaded: {downloaded}\nSkipped: {skipped}")

	if bad>0:
		print(f"Errors: {bad}\nListed:")
		for i in error_list:
			print(i)
	return 0

if __name__ == '__main__':
	main()
