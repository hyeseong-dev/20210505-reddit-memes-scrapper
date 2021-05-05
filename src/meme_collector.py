import requests as _requests
from tqdm import tqdm as _tqdm
import os as _os
import dotenv as _dotenv
import praw as _praw
import urllib.parse as _parse
import shutil as _shutil

_dotenv.load_dotenv()

def _create_reddit_client():
    client = _praw.Reddit(
        client_id=_os.environ["CLIENT_ID"],
        client_secret=_os.environ["CLIENT_SECRET"],
        user_agent=_os.environ["USER_AGENT"],
    )
    return client

def _is_image(post):
    try:
        return post.post_hint == 'image'
    except AttributeError:
        return False

def _get_image_urls(client: _praw.Reddit, subreddit_name: str, limit: int):
    hot_memes = client.subreddit(subreddit_name).hot(limit=limit)    
    image_urls = list()
    for post in hot_memes:
        if _is_image(post):
            image_urls.append(post.url)
    return image_urls

def _get_image_name(image_url: str) -> str:
    image_name = _parse.urlparse(image_url) 
    basename = _os.path.basename(image_name.path)
    return basename                                  # '/Users/Desktop/temp/test.txt' 경우 'text.txt'만 반환 됨
    
def _create_folder(folder_name: str): 
    """
    If the folder does not exist then create the 
    foler using the given name
    """
    try:
        _os.makedirs(folder_name, exist_ok=True)
    except OSError:
        print('something happened while making folder')
    else:
        print('Downloading...')

def _download_image(folder_name: str, raw_response, image_name: str):
    with open(f'{folder_name}/{image_name}', 'wb') as image_file:
        _shutil.copyfileobj(raw_response, image_file)

def _collect_memes(subreddit_name: str, limit: int=20):
    '''
    Collects the images from the urls and stores
    the folders named after their subreddits
    '''
    _create_folder(subreddit_name)
    client = _create_reddit_client()
    images_urls = _get_image_urls(client=client, subreddit_name=subreddit_name, limit=limit)
    
    for image_url in images_urls:
        image_name = _get_image_name(image_url)
        response = _requests.get(image_url, stream=True)

        if response.status_code == 200:
            response.raw.decode_content = True
            _download_image(subreddit_name, response.raw, image_name)
    print('Done!')

if __name__ == '__main__':
    _collect_memes(subreddit_name='ProgrammerHumor')
