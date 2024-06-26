
def _download_emote(url, filename):
    import requests
    import converter
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        converter.save_webp_to_jpg(response.content,filename)
    else:
        print(f"Failed to retrieve the emote. Status code: {response.status_code}")
    response.close()

def save_emotes(urls,out_folder):
    import os
    for i,url in enumerate(urls,1):
        url=validate_url(url)
        print(f'Downloading {url}...')
        _download_emote(url,os.path.join(out_folder,str(i)))

        
def validate_url(url):
    import re
    ttv_emotes_formats = [
        '1x.webp',
        '2x.webp',
        '3x.webp',
        '4x.webp',
    ]
    default_format = '3x.webp'
    
    base_pattern = r"https://7tv.app/emotes/([a-zA-Z0-9]+)(/?)$"
    suffix_pattern = r"https://cdn.7tv.app/emote/([a-zA-Z0-9]+)/(" + '|'.join(ttv_emotes_formats).replace('.', r'\.') + r")$"
    
    match = re.match(suffix_pattern, url)
    if match:
        return url
    
    match = re.match(base_pattern, url)
    if match:
        base_id = match.group(1)
        
        if url.startswith(f"https://cdn.7tv.app/emote/{base_id}/"):
            return url + f"/{default_format}"
        else:
            return f"https://cdn.7tv.app/emote/{base_id}/{default_format}"
    
    raise ValueError(f"The URL provided is not a valid 7tv emote URL:\n{url}")