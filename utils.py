def read_file(filepath):
    try:
        # print(f'Emotes file: {filepath}')
        with open(filepath, 'r') as file:
            content = file.readlines()
            content=[url.rstrip('\n') for url in content]
            return content
    except: pass

def get_links_dict(filepath):
    content=read_file(filepath)
    # print(content,type(content))
    return create_links_dict(content)

def create_links_dict(urls):
    from urllib.parse import urlparse
    allowed_paths = {
        'https://7tv.app/emotes/':'7tv_emotes',
        'https://cdn.7tv.app/emote/':'7tv_emotes',
    }
    path_dict = {allowed_paths[path]: [] for path in allowed_paths}
    
    for url in urls:
        parsed_url = urlparse(url)
        url_prefix = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
        for allowed_path in allowed_paths:
            if url_prefix.startswith(allowed_path):
                path_dict[allowed_paths[allowed_path]].append(url)
                break

    return path_dict

def check_args(argv):
    DEV_MODE=True
    l=len(argv)
    if l==1 and DEV_MODE: #if executed from vscode gui
        argv[:]=['','./emotes','./out']
        return
    # check if there are argv
    if l<=1:
        raise KeyError('Insufficient arguments')
    # check if the emotes list file exists
    import os
    if not os.path.exists(argv[1]):
        raise KeyError('Emotes list file does not exist')
    # check if the output folder is specified/correct
    if l!=3 or not check_foldername(argv[2]):
        raise KeyError('Output folder invalid or not provided')

def check_foldername(folder_name):
    import re
    if re.search(r'[\\/:\*\?"<>\|]', folder_name) is not None:
        return False
    if folder_name in {'.', '..'}:
        return False
    if len(folder_name) > 255:
        return False
    return True
