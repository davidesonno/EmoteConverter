from PIL import Image, ImageSequence
from io import BytesIO

def save_webp_to_jpg(webp_data, output_file):
    import os
    try:
        folder_path = os.path.dirname(output_file)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        img = Image.open(BytesIO(webp_data))
        is_animated = img.is_animated if hasattr(img, 'is_animated') else False
        
        if is_animated:
            frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
            frames[0].save(output_file + '.gif', save_all=True, append_images=frames[1:], loop=0)
        else:
            img.convert("RGBA").save(output_file + '.png', "PNG")
    except Exception as e:
        raise e
