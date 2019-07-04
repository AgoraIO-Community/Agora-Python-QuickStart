import os
import tarfile
import argparse

def extract_graph(args):
    MODEL_NAME = args.model
    MODEL_FILE = MODEL_NAME + '.tar'
    tar_file = tarfile.open(MODEL_FILE)
    for file in tar_file.getmembers():
        file_name = os.path.basename(file.name)
        if 'frozen_inference_graph.pb' in file_name:
            tar_file.extract(file, os.getcwd())

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('--model', default='ssdlite_mobilenet_v2_coco_2018_05_09',
                       type=str, help='model name')
    args = parse.parse_args()
    extract_graph(args)