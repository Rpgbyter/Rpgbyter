import requests
import argparse
import os

def download_image(prompt, filename, output_dir):
    url = f"https://pollinations.ai/p/{prompt}?width=1024&height=768&nologo=true"
    filepath = os.path.join(output_dir, filename)
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f'Image downloaded to {filepath}')
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {filename}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Download images from Pollinations.ai.")
    parser.add_argument('--output_dir', type=str, default='./', help='Directory to save the downloaded images.')
    parser.add_argument('--prompt', type=str, help='Single prompt to generate an image. If not provided, all default prompts will be used.')
    parser.add_argument('--filename', type=str, help='Filename for the single image. Required if --prompt is used.')

    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    if args.prompt and args.filename:
        download_image(args.prompt, args.filename, args.output_dir)
    elif not args.prompt and not args.filename:
        prompts = [
            ("Gemini%20CLI%20installation%20process", "gemini_cli_image_1.png"),
            ("Gemini%20CLI%20authentication%20and%20setup", "gemini_cli_image_2.png"),
            ("Gemini%20CLI%20basic%20commands%20and%20usage", "gemini_cli_image_3.png"),
            ("Gemini%20CLI%20advanced%20features%20and%20integrations", "gemini_cli_image_4.png"),
            ("Gemini%20CLI%20code%20generation%20example", "gemini_cli_image_5.png"),
            ("Gemini%20CLI%20shell%20command%20execution", "gemini_cli_image_6.png"),
            ("Gemini%20CLI%20codebase%20analysis", "gemini_cli_image_7.png"),
            ("Gemini%20CLI%20reviewing%20changes", "gemini_cli_image_8.png"),
            ("Gemini%20CLI%20troubleshooting%20common%20issues", "gemini_cli_image_9.png"),
            ("Gemini%20CLI%20future%20vision%20and%20development", "gemini_cli_image_10.png")
        ]
        for prompt, filename in prompts:
            download_image(prompt, filename, args.output_dir)
    else:
        parser.error("Both --prompt and --filename must be provided together, or neither.")

if __name__ == "__main__":
    main()