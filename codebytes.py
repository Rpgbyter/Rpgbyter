import os
from datetime import datetime

def prompt_post():
    title = input('Post Title: ')
    content = input('Post Content (Markdown or plain text): ')
    date = datetime.now().strftime('%Y-%m-%d')
    filename = f"{date}-{title.lower().replace(' ', '-').replace('.', '')}.md"
    post_path = os.path.join(os.path.dirname(__file__), 'Posts', filename)
    with open(post_path, 'w', encoding='utf-8') as f:
        f.write(f'''<div class="card blog-post">
  <h3>{title}</h3>
  <div class="card-footer">{date}</div>
  <button class="read-more-btn" onclick="togglePostContent(this)">Read More</button>
  <div class="post-content" style="max-height:0;overflow:hidden;transition:max-height 0.4s cubic-bezier(.4,0,.2,1),padding 0.4s; text-align:left;">
    {content.replace(chr(10), '<br>')}
  </div>
</div>\n''')
    print(f"Post saved to {post_path}")
    # Optionally, call the HTML adder here

if __name__ == '__main__':
    prompt_post()
