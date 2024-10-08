"""
Script for displaying an image with the OCR model predictions.
"""

import logging
import pathlib
from contextlib import nullcontext

import click
import cv2
import keras
import numpy as np

import fast_plate_ocr.common.utils
from fast_plate_ocr.train.model.config import load_config_from_yaml
from fast_plate_ocr.train.utilities import utils

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)


@click.command(context_settings={"max_content_width": 120})
@click.option(
    "-m",
    "--model",
    "model_path",
    required=True,
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=pathlib.Path),
    help="Path to the saved .keras model.",
)
@click.option(
    "--config-file",
    required=True,
    type=click.Path(exists=True, file_okay=True, path_type=pathlib.Path),
    help="Path pointing to the model license plate OCR config.",
)
@click.option(
    "-d",
    "--img-dir",
    required=True,
    type=click.Path(exists=True, dir_okay=True, file_okay=False, path_type=pathlib.Path),
    help="Directory containing the images to make predictions from.",
)
@click.option(
    "-t",
    "--time",
    default=True,
    is_flag=True,
    help="Log time taken to run predictions.",
)
@click.option(
    "-l",
    "--low-conf-thresh",
    type=float,
    default=0.2,
    show_default=True,
    help="Threshold for displaying low confidence characters.",
)
def visualize_predictions(
    model_path: pathlib.Path,
    config_file: pathlib.Path,
    img_dir: pathlib.Path,
    low_conf_thresh: float,
    time: bool,
):
    """
    Visualize OCR model predictions on unlabeled data.
    """
    config = load_config_from_yaml(config_file)
    model = utils.load_keras_model(
        model_path, vocab_size=config.vocabulary_size, max_plate_slots=config.max_plate_slots
    )
    images = utils.load_images_from_folder(
        img_dir, width=config.img_width, height=config.img_height
    )
    for image in images:
        with (
            fast_plate_ocr.common.utils.log_time_taken("Prediction time") if time else nullcontext()
        ):
            x = np.expand_dims(image, 0)
            prediction = model(x, training=False)
            prediction = keras.ops.stop_gradient(prediction).numpy()
        utils.display_predictions(
            image=image,
            prediction=prediction,
            alphabet=config.alphabet,
            plate_slots=config.max_plate_slots,
            vocab_size=config.vocabulary_size,
            low_conf_thresh=low_conf_thresh,
        )
    cv2.destroyAllWindows()


if __name__ == "__main__":
    visualize_predictions()
