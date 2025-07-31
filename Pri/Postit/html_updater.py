from bs4 import BeautifulSoup

def add_post_to_html(html_file_path, section_id, post_html):
    with open(html_file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    section_div = soup.find('section', id=section_id)
    if not section_div:
        print(f"Error: Section with ID '{section_id}' not found in {html_file_path}")
        return False

    category_content_div = section_div.find('div', class_='category-content')
    if not category_content_div:
        print(f"Error: 'category-content' div not found within section '{section_id}'")
        return False

    # Find the comment where new posts should be dynamically loaded
    # This assumes the comment is the last element before which new content should be added
    comment_tag = category_content_div.find(string=lambda text: isinstance(text, Comment) and 'Blog posts will be dynamically loaded here' in text)

    if comment_tag:
        # Insert the new post HTML before the comment
        new_post_soup = BeautifulSoup(post_html, 'html.parser')
        comment_tag.insert_before(new_post_soup)
    else:
        # If no comment, append to the end of category_content_div
        new_post_soup = BeautifulSoup(post_html, 'html.parser')
        category_content_div.append(new_post_soup)

    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    return True

# This is a placeholder for the Comment class, as it's not directly imported from bs4
# It's usually accessed via soup.new_tag(name, **kwargs) or directly from the element's contents
# For this script, we'll assume it's a string comparison for simplicity, but for robust parsing,
# it's better to use from bs4.element import Comment if available or handle it as a NavigableString.
from bs4.element import Comment