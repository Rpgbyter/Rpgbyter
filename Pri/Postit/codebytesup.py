import os
from datetime import datetime
from html_updater import add_post_to_html

def create_post(section_id):
    title = input("Enter the title of the post: ")
    content = []
    print("Enter the content of the post. Type 'END' on a new line to finish.")
    while True:
        line = input()
        if line == 'END':
            break
        content.append(line)

    post_content_raw = "\n".join(content)
    # Replace newlines with <br> for HTML display
    post_content_html = post_content_raw.replace('\n', '<br>')

    date = datetime.now().strftime("%Y-%m-%d")

    html_block = f"""
<div class="blog-post-container">
    <details class="blog-post-details">
        <summary class="blog-post-summary">
            <span class="post-title">{title}</span>
            <span class="post-date">{date}</span>
        </summary>
        <div class="post-content">
            {post_content_html}
        </div>
    </details>
</div>
"""

    html_file_path = os.path.join(os.path.dirname(__file__), '..', 'No', 'byterFlash.html')
    html_file_path = os.path.abspath(html_file_path)

    if add_post_to_html(html_file_path, section_id, html_block):
        print(f"Successfully added post to {section_id} in {html_file_path}")
    else:
        print(f"Failed to add post to {section_id}.")

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        section_id = sys.argv[1]
        create_post(section_id)
    else:
        print("Usage: python3 codebytesup.py <section_id>")
        print("Available sections: byteblogging, bytecoding-tutorials, codebytes")