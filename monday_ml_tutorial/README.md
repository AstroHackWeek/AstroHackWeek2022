# Example DVC Pipeline

This folder demonstrates how to set up a [DVC pipeline](https://dvc.org/doc/start/data-management/data-versioning) with existing code.

1. Copy your code out of notebooks etc. and into scripts.
2. Execute each stage with `dvc run -n {name} -d {dependency} -o {output} {command}`
3. Check the pipeline with `dvc dag`
4. Commit `dvc.yaml` and `dvc.lock` files to git

Then you can make edits to your code or data and re-run the pipeline with `dvc repro`. DVC will automatically re-run only the stages that need re-running.

I've helped out with Step 1, converting to scripts, by script-ifying the HelloUniverse / Ciprianovic "DeepMerge" notebook Michelle introduced in Part 1.

## Running the Scripts

Install the Python requirements

    pip install -r requirements.txt

Download the data (images and labels, as a single FITS file)

    python deepmerge/download_data.py deepmerge/latest_data.fits

Preprocess the data and save to deepmerge/prepared_data/*.npy

    python deepmerge/prepare_data.py

Train a CNN on the preprocessed data, save to deepmerge/models/latest

    python deepmerge/train_cnn.py

## Setting up DVC Pipeline

This bit is your job! Remember: describe the scripts as a series of steps, each with a name, dependencies, and outputs.

    dvc init --subdir

    # TODO for you

I recommend the `dvc run` [docs](https://dvc.org/doc/command-reference/run#run) and the versioning [tutorial](https://dvc.org/doc/use-cases/versioning-data-and-models/tutorial).

For extra bonus points, add Weights and Biases tracking in train_cnn.py. See the [TensorFlow guide](https://docs.wandb.ai/guides/integrations/tensorflow)
