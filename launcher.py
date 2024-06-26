import sys
from _7tv import main as main7tv
from utils import *


def main(argv):
    check_args(argv)
    # print(argv)
    emotes_list_path=argv[1]
    output_folder=argv[2]
    emotes=get_links_dict(emotes_list_path)
    # print(emotes)
    main7tv.save_emotes(emotes['7tv_emotes'],output_folder)    


if __name__=='__main__':
    main(sys.argv)