# ISRO Project Directory Index
    This document serves as an index to the entire project directory structure and its contents.

## Directory Structure

    ### Root Directory
        - `index.md` - This file, serving as the project index

        - `ISRO_Proposal.pdf` - Project proposal document
        - `Paper.pdf` and `Paper.docx` - Project paper/documentation

        - `.gitignore` - Git ignore configuration file

    ### trainer/
        Contains components for training machine learning models.

        #### Key Files:
        - `raw_data_downloader.ipynb` - Notebook for downloading raw data
        - `raw_data_processor.ipynb` - Notebook for processing raw data
        - `data_processor.ipynb` - Notebook for processing training data
        - `linear_interpreter.ipynb` - Notebook for linear model interpretation
        - `model_builder.ipynb` - Notebook for building models

        - `combined_data.csv` - Combined training dataset
        - `cleaned_data.csv` - Cleaned training dataset

        - `info.md` - Information about the training module
        - `tables.md` - Documentation of results

        #### Subdirectories:
        - `raw_data/` - Raw training data
        - `processed_data/` - Processed training data

        - `plots/` - Generated plots and visualizations
        - `map_screenshots/` - Contains map visualization screenshots

    ### prediction/
        Contains components related to making predictions using trained models.

        #### Key Files:
        - `data_importer.ipynb` - Notebook for importing data
        - `data_processor.ipynb` - Notebook for processing prediction data
        - `predictions.ipynb` - Notebook for making predictions

        - `combined_data.csv` - Combined dataset for predictions
        - `cleaned_data.csv` - Cleaned dataset for predictions

        - `info.md` - Information about the prediction module

        #### Subdirectories:
        - `raw_data/` - Raw data for predictions
        - `raw_data_processor/` - Scripts for processing raw data
        - `processed_data/` - Processed data for predictions
        
        - `imported_data/` - Contains preprocessed oceanographic data files (chl, fe, kd, no3, o2, ph, po4, si, spco2, so, thetao, uo, vo, wo) with projected dates from 2025-2030, used when CMIP6 data is not available

        - `plots/` - Generated plots and visualizations
        - `map_screenshots/` - Contains map visualization screenshots

    ### models/
        Contains trained machine learning models.

        #### Key Files:
        - `linear_regression_model.pkl` - Trained Linear Regression model
        - `robust_regression_model.pkl` - Trained Robust Regression model

        - `scaler.pkl` - Data scaler for model inputs
        - `neural_network.pkl` - Trained Neural Network model
        - `random_forest.pkl` - Trained Random Forest model

## Usage
1. For training new models, refer to the `trainer/` directory
2. Trained models are stored in the `models/` directory
3. For making predictions, use the components in the `prediction/` directory

## Documentation
- Each major component has its own `info.md` file with specific documentation
- The project paper and proposal provide high-level overview and methodology