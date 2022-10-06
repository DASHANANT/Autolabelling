import sys
from src.config.parser import parse_arguments
from src.apps.show_point_cloud import show_point_cloud
from src.apps.show_image import show_image
from src.tools.util import get_path


def main():
    config = parse_arguments()
    if config['dp'] is None:
        if config['rd']:
            config['dp'] = get_path(root_dir=config['rd'], idx=config['i'])
        elif config['dd']:
            config['dp'] = get_path(root_dir=config['dd'], idx=config['i'])
        else:
            print("Error: no path found")

    if config['vwp']:
        show_point_cloud(pc_path=config['dp'], bev=config['bv'], rmg=config['rmg'],
                         ev=config['ev'], azimuth=config['azim'], elevation=config['eva'])
    if config['vwc']:
        show_image(root=config['rd'], dp=config['dp'], cam=config['vwc'])


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            sys.exit(0)
