import os
import cv2
import numpy as np
from pathlib import Path
import yaml

def load_yaml_config(yaml_path):
    """Load YAML configuration file."""
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)

def create_mask_from_segments(image_shape, segments):
    """Create a binary mask from YOLO format segments."""
    mask = np.zeros(image_shape[:2], dtype=np.uint8)
    for segment in segments:
        points = np.array(segment).reshape(-1, 2)
        points[:, 0] *= image_shape[1]  # width
        points[:, 1] *= image_shape[0]  # height
        points = points.astype(np.int32)
        cv2.fillPoly(mask, [points], 1)
    return mask

def process_label_file(label_path):
    """Process a single YOLO format label file and return segments."""
    segments = []
    if os.path.exists(label_path):
        with open(label_path, 'r') as f:
            for line in f:
                data = line.strip().split()
                if len(data) > 8:  # YOLO segmentation format
                    polygon = list(map(float, data[1:]))
                    polygon = np.array(polygon).reshape(-1, 2)
                    segments.append(polygon)
    return segments

def verify_masks(dataset_dir, output_dir):
    """Main function to verify masks and save visualization."""
    dataset_dir = Path(dataset_dir)
    output_dir = Path(output_dir)
    yaml_path = dataset_dir / 'data.yaml'
    config = load_yaml_config(yaml_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    image_dir = dataset_dir / 'images' / 'train'
    label_dir = dataset_dir / 'labels' / 'train'
    image_files = list(image_dir.glob('*.jpg')) + list(image_dir.glob('*.png'))
    total_images = len(image_files)
    print(f"Found {total_images} images to process")
    for idx, image_path in enumerate(image_files, 1):
        print(f"Processing image {idx}/{total_images}: {image_path.name}")
        image = cv2.imread(str(image_path))
        if image is None:
            print(f"Warning: Could not read image {image_path}")
            continue
        label_path = label_dir / f"{image_path.stem}.txt"
        segments = process_label_file(label_path)
        mask = create_mask_from_segments(image.shape, segments)
        result = image.copy()
        result[mask == 0] = 0
        output_path = output_dir / f"masked_{image_path.name}"
        cv2.imwrite(str(output_path), result)
    print("Processing complete!")

if __name__ == "__main__":
    # Change this path to your dataset folder
    dataset_dir = r"C:\Users\Soumya\Documents\cvat_mask_verify\StiQy_perspective_template-main"
    output_dir = r"C:\Users\Soumya\Documents\cvat_mask_verify\masked_verification"
    verify_masks(dataset_dir, output_dir)
