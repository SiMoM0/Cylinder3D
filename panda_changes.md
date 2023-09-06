# Changes performed to run Cylinder3D on Pandaset

#### Requirements

Same as Cylinder3D plus:
* json
* gzip
* numpy-quaternion
* pandas

### Usage

    python3 run_demo.py <pandaset_path> <prediction_path>

### Dataloader

* pc_dataset.py
    * add Pandaset class
    * add label map from pandaset to kitti
    * add getPoses function
    * modified absoluteFilePaths function
    * add packages json, gzip, pickle, quaternion (from numpy)

* pandaset.yaml: yaml configuration file for pandaset, same as semantickitti

### Inference

* demo_folder.py: set Pandaset dataset class instead of SemKitti

* run_cylinder.py: simple script to run demo_folder.py for each sequence in pandaset (input pandaset path)

* run_demo.py: script to perform inference for all the sequences in pandaset and compute miou/acc (based on demo_folder.py). Saves predicitons on specified path

### Others

* labels_ex.txt: confuion matrix example for evaluation

* dataset_nuscenes.py: changed np.int to np.int64

* dataset_semantickitti.py: changed np.int to np.int64
