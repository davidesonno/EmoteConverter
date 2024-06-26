from PIL import Image, ImageSequence
from io import BytesIO

def save_webp_to_jpg(webp_data, output_file):
    try:
        img = Image.open(BytesIO(webp_data))
        is_animated = img.is_animated if hasattr(img, 'is_animated') else False
        
        if is_animated:
            frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
            frames[0].save(output_file + '.gif', save_all=True, append_images=frames[1:], loop=0)
            # print(f"Animated image saved as {output_file}.gif")
        else:
            img.convert("RGB").save(output_file + '.jpg', "JPEG")
            # print(f"Static image saved as {output_file}.jpg")
            
    except Exception as e:
        raise e
