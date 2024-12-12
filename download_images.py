import os
import requests
from urllib.parse import urlparse
import concurrent.futures

# Create images directory if it doesn't exist
IMAGES_DIR = os.path.join('static', 'images')
os.makedirs(IMAGES_DIR, exist_ok=True)

# List of images to download with their target filenames
IMAGES = {
    # Hero images
    'https://images.unsplash.com/photo-1504384308090-c894fdcc538d': 'hero-bg.jpg',  # Tech background
    'https://images.unsplash.com/photo-1460925895917-afdab827c52f': 'about-hero.jpg',  # Meeting room
    'https://images.unsplash.com/photo-1522071820081-009f0129c71c': 'team-hero.jpg',  # Team collaboration
    
    # Service related images
    'https://images.unsplash.com/photo-1498050108023-c5249f4df085': 'software-dev.jpg',  # Code on screen
    'https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a': 'seo.jpg',  # SEO visualization
    'https://images.unsplash.com/photo-1451187580459-43490279c0fa': 'data.jpg',  # Data visualization
    
    # Feature images
    'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40': 'expertise.jpg',  # Professional at work
    'https://images.unsplash.com/photo-1553877522-43269d4ea984': 'support.jpg',  # Customer support
    'https://images.unsplash.com/photo-1551434678-e076c223a692': 'technology.jpg',  # Modern office
    
    # Abstract backgrounds
    'https://images.unsplash.com/photo-1557683316-973673baf926': 'pattern1.jpg',  # Abstract pattern
    'https://images.unsplash.com/photo-1579546929518-9e396f3cc809': 'gradient1.jpg',  # Gradient
    'https://images.unsplash.com/photo-1558591710-4b4a1ae0f04d': 'pattern2.jpg',  # Tech pattern
}

def download_image(url_filename):
    url, filename = url_filename
    try:
        response = requests.get(url)
        if response.status_code == 200:
            filepath = os.path.join(IMAGES_DIR, filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f'Successfully downloaded {filename}')
            return True
        else:
            print(f'Failed to download {filename}: Status code {response.status_code}')
            return False
    except Exception as e:
        print(f'Error downloading {filename}: {str(e)}')
        return False

def main():
    print('Starting image downloads...')
    
    # Use ThreadPoolExecutor for concurrent downloads
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(download_image, IMAGES.items()))
    
    success_count = sum(1 for result in results if result)
    print(f'\nDownload complete. Successfully downloaded {success_count} of {len(IMAGES)} images.')

if __name__ == '__main__':
    main()
