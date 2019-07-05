import os
import tarfile
import argparse

def extract_graph(args):
    MODEL_FILE = args.model
    tar_file = tarfile.open(MODEL_FILE)
    for file in tar_file.getmembers():
        file_name = os.path.basename(file.name)
        if 'frozen_inference_graph.pb' in file_name:
            tar_file.extract(file, os.getcwd())

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('--model_file', default='ssdlite_mobilenet_v2_coco_2018_05_09.tar',
                       type=str, help='file name of model')
    args = parse.parse_args()
    extract_graph(args)