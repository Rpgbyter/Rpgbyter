import requests
import os

def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded: {save_path}")
    else:
        print(f"Failed to download {url} (status code: {response.status_code})")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python download_image.py <image_url> <save_path>")
        sys.exit(1)
    url = sys.argv[1]
    save_path = sys.argv[2]
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    download_image(url, save_path)
