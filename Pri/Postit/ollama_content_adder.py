import ollama
import requests
import os
from datetime import datetime
from html_updater import add_post_to_html

# Configuration for Ollama models
OLLAMA_MODELS = {
    "byteblogging": "llama3", # A general purpose model for blog posts
    "bytecoding-tutorials": "codellama", # A code-focused model for tutorials
    "codebytes": "llama3" # A general purpose model for code snippets/discussions
}

# Pollinosis API configuration (placeholder - replace with actual API endpoint and key if needed)
POLLINOSIS_API_URL = "http://localhost:8000/generate_image" # Example local URL
# POLLINOSIS_API_KEY = "YOUR_API_KEY" # If an API key is required

def generate_content_with_ollama(title, section_id):
    model = OLLAMA_MODELS.get(section_id, "llama3") # Default to llama3 if section not found
    prompt = f"Generate a detailed and engaging article for a blog post titled '{title}'. The article should be suitable for the '{section_id}' section of a personal website. Focus on providing valuable information and insights. Format the content using paragraphs and subheadings (e.g., '## Subheading')."

    if section_id == "bytecoding-tutorials":
        prompt = f"Generate a comprehensive coding tutorial for a blog post titled '{title}'. The tutorial should include code examples and explanations. Focus on practical steps and clear instructions. Format the content using paragraphs, subheadings (e.g., '## Subheading'), and code blocks (e.g., ```python\nprint(\"Hello\")\n```)."
    elif section_id == "codebytes":
        prompt = f"Generate a concise explanation or discussion for a code snippet/concept titled '{title}'. Include a small, illustrative code example. Format the content using paragraphs, and code blocks (e.g., ```python\n# code here\n```)."

    print(f"Generating content for '{title}' using Ollama model '{model}'...")
    try:
        response = ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']
    except Exception as e:
        print(f"Error generating content with Ollama: {e}")
        return ""

def generate_image_with_pollinosis(prompt):
    print(f"Generating image with Pollinosis API for prompt: '{prompt}'...")
    try:
        headers = {"Content-Type": "application/json"}
        # if POLLINOSIS_API_KEY: # Uncomment if API key is needed
        #     headers["Authorization"] = f"Bearer {POLLINOSIS_API_KEY}"

        data = {"prompt": prompt}
        response = requests.post(POLLINOSIS_API_URL, json=data, headers=headers)
        response.raise_for_status() # Raise an exception for HTTP errors
        image_data = response.json()
        # Assuming the API returns a URL or base64 encoded image
        # For now, we'll just return a placeholder or the URL if available
        if 'image_url' in image_data:
            return image_data['image_url']
        elif 'image_base64' in image_data:
            # In a real scenario, you'd save this base64 to a file and return the path
            print("Base64 image data received. Saving to placeholder.png...")
            # Example: save_base64_image(image_data['image_base64'], "placeholder.png")
            return "./Copi/placeholder.png" # Placeholder path
        else:
            return ""
    except requests.exceptions.RequestException as e:
        print(f"Error generating image with Pollinosis API: {e}")
        print("Please ensure the Pollinosis API server is running and accessible.")
        return ""

def create_ollama_post(section_id):
    title = input("Enter the title for the Ollama generated post: ")

    # Generate content using Ollama
    generated_content = generate_content_with_ollama(title, section_id)
    if not generated_content:
        print("Could not generate content. Aborting post creation.")
        return

    # Generate image using Pollinosis API
    image_prompt = f"A pixel art image representing the blog post: {title}"
    generated_image_url = generate_image_with_pollinosis(image_prompt)
    image_tag = f'<img src="{generated_image_url}" alt="{title}" style="max-width:100%; height:auto; margin-bottom: 15px;">' if generated_image_url else ""

    date = datetime.now().strftime("%Y-%m-%d")

    # Convert generated content to HTML-friendly format (basic markdown to HTML conversion)
    # This is a very basic conversion. For full markdown, a library like markdown2 or mistune would be better.
    html_content_parts = []
    for line in generated_content.split('\n'):
        if line.startswith('## '):
            html_content_parts.append(f'<h3>{line[3:].strip()}</h3>')
        elif line.strip(): # Only add non-empty lines as paragraphs
            html_content_parts.append(f'<p>{line.strip()}</p>')
    formatted_content = "\n".join(html_content_parts)

    html_block = f"""
<div class="blog-post-container">
    <details class="blog-post-details">
        <summary class="blog-post-summary">
            <span class="post-title">{title}</span>
            <span class="post-date">{date}</span>
        </summary>
        <div class="post-content">
            {image_tag}
            {formatted_content}
        </div>
    </details>
</div>
"""

    html_file_path = os.path.join(os.path.dirname(__file__), '..', 'No', 'byterFlash.html')
    html_file_path = os.path.abspath(html_file_path)

    if add_post_to_html(html_file_path, section_id, html_block):
        print(f"Successfully added Ollama-generated post to {section_id} in {html_file_path}")
    else:
        print(f"Failed to add Ollama-generated post to {section_id}.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        section_id = sys.argv[1]
        create_ollama_post(section_id)
    else:
        print("Usage: python3 ollama_content_adder.py <section_id>")
        print("Available sections: byteblogging, bytecoding-tutorials, codebytes")