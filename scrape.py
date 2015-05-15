import praw
import csv
import logging

logging.basicConfig(level=logging.DEBUG)

user_agent = "osx:comment-grabber:0.0.1 (by /u/bjlange)"
reddit = praw.Reddit(user_agent=user_agent)

rpolitics = reddit.get_subreddit('politics')
top = rpolitics.get_top_from_week()

story = reddit.get_submission(submission_id='3470iu')

story.replace_more_comments(limit=None)

comments = praw.helpers.flatten_tree(story.comments)

# print len(comments)
# print dir(comments[0])
# import pdb; pdb.set_trace()


with open('bernie-sanders-announces.csv', 'w') as outfile:
    header = ['author', 'score', 'submission', 'body']
    writer = csv.DictWriter(outfile, fieldnames=header)

    writer.writeheader()

    for comment in comments:
        comment_dict = {}
        author = comment.author

        # if the user has deleted their account, author is == None
        if author:
            comment_dict['author'] = comment.author.name
        else:
            comment_dict['author'] = None

        comment_dict['submission'] = comment.submission.title.encode('utf-8')
        comment_dict['score'] = comment.score
        comment_dict['body'] = comment.body.encode('utf-8')

        writer.writerow(comment_dict)

