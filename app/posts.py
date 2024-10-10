# Posts class is a collection of posts
# defined by the associated json file
import json
import uuid
from datetime import datetime

class Posts: 
    def __init__(self, posts_file):
        self.posts_file = posts_file
        with open(self.posts_file) as file:
            self.posts = json.load(file)
        
    def get_posts(self):
        return self.posts
    
    def add_post(self, author, title, html_content):
        self.posts[str(uuid.uuid4())] = {
            "author": author,
            "date": str(datetime.now().date().strftime("%m/%d/%Y")),
            "title": title,
            "html_content": html_content,
            "post_reactions": {
                "up": 0,
                "down": 0
            },
            "comments": {}
        }
        self.update_db()
    
    def update_db(self):
        with open(self.posts_file, "w") as file:
            json.dump(self.posts, file)

    def get_post(self, post_id):
        return self.get_posts()[post_id]
    

    #TODO: add methods:
    # add_comment(id)
    # add_reaction(id)
    # add_comment_reaction(id)
