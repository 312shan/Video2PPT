# _*_ coding: utf-8 _*_
import cv2
from skimage.measure import compare_ssim as ssim
import numpy as np
import argparse
import os

# Create ArgumentParser() object
parser = argparse.ArgumentParser()

# Add argument
parser.add_argument('--videos_path', required=True, help='path to video')
parser.add_argument('--sim_benchmark', type=float, help='image similarity benchmark', default=0.95)
parser.add_argument('--images_output_path', help='path to images output folder', default='./')
parser.add_argument('--frame_per_step', type=int, help='how many frame per step', default=100)

# Print usage
parser.print_help()

# Parse argument
args = parser.parse_args()

vc = cv2.VideoCapture()
vc.open(args.videos_path)
fps = vc.get(cv2.CAP_PROP_FPS)
frames = vc.get(cv2.CAP_PROP_FRAME_COUNT)
print(fps, frames)
pre = None
for i in range(int(frames)):
    ret, frame = vc.read()
    if pre is None:
        pre = np.zeros_like(frame)
    if frame is None:
        continue
    if i % args.frame_per_step == 0 and ssim(pre, frame, multichannel=True) < args.sim_benchmark:
        cv2.imwrite(os.path.join(args.images_output_path, '{}.png'.format(i)), frame)
        pre = frame

