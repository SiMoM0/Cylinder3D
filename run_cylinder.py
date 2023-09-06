# Run Cylinder3D
# Usage: python3 run_cylinder <dataset path>

import os
import sys

# path to dataset/sequences
dataset_path = sys.argv[1]
output_path = sys.argv[2]

for seq in sorted(os.listdir(dataset_path)):

    #print(os.path.join(dataset_path, seq))

    demo_folder = os.path.join(dataset_path, seq, 'lidar/')
    save_folder = os.path.join(output_path, seq)
    label_folder = os.path.join(dataset_path, seq, 'annotations', 'semseg')

    command = f'python3 demo_folder.py --demo-folder {demo_folder} --save-folder {save_folder} --demo-label-folder {label_folder}'

    os.mkdir(save_folder)

    # execute command
    #os.system(command)

    print(command)