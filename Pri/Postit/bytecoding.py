import os
from datetime import datetime

def prompt_post():
    title = input('Post Title: ')
    content = input('Post Content (Markdown or plain text): ')
    date = datetime.now().strftime('%Y-%m-%d')
    filename = f"{date}-{title.lower().replace(' ', '-').replace('.', '')}.md"
    post_path = os.path.join(os.path.dirname(__file__), 'Posts', filename)
    with open(post_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n{content}\n")
    print(f"Post saved to {post_path}")
    # Optionally, call the HTML adder here

if __name__ == '__main__':
    prompt_post()
