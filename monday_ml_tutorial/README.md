# Example DVC Pipeline

This folder demonstrates how to set up a DVC pipeline with existing code.

1. Copy your code out of notebooks etc. and into scripts.
2. Execute each stage with `dvc run -n {name} -d {dependency} -o {output} {command}`
3. Check the pipeline with `dvc dag`
4. Run the pipeline with `dvc repro`
5. Commit all `.dvc` files to git

I've helped out with Step 1, converting to scripts, by script-ifying the HelloUniverse / Ciprianovic "DeepMerge" notebook Michelle introduced in Part 1.

## Running the Scripts

Install the Python requirements

    pip install -r requirements.txt

Download the data (images and labels, as a single FITS file)

    python deepmerge/download_data.py deepmerge/latest_data.fits

Preprocess the data and save to deepmerge/prepared_data/*.npy

    python deepmerge/preprocess_data.py

Train a CNN on the preprocessed data, save to deepmerge/models/latest

    python deepmerge/train_cnn.py

## Setting up DVC Pipeline

This bit is your job! Remember: describe the scripts as a series of steps, each with a name, dependencies, and outputs.

    # TODO for you