## Overview of Project Structure and Contents:

    The project is organized into several folders, each serving a specific purpose:



    ### Results and Visualizations Overview:

        1. info.md: This file contains essential information about the project, including its objectives, methodologies, and any relevant background information. It serves as a guide for understanding the overall context of the work.

        2. plots: This folder includes various visualizations generated during the analysis. These plots help in understanding the data trends and patterns, providing a visual representation of the findings.

        3. map_screenshots: This folder contains screenshots of interactive maps created during the project. These maps visualize geographical data and can be useful for presentations or reports.

        4. tables.md: This file provides a summary of the tables generated throughout the project, detailing the structure and contents of the datasets used.



    ### Data Folders/Files Overview:

        - raw_data: This folder contains the original datasets collected for the project. These files are in their unprocessed form and serve as the foundation for all subsequent analyses.

        - processed_data: This folder holds the cleaned and processed datasets. The data has been refined to remove inconsistencies and prepare it for analysis.

        - combined_data.csv: This file contains the combined datasets from various sources, allowing for a comprehensive analysis of the variables of interest.

        - cleaned_data.csv: This file is a cleaned version of the raw data, ensuring that it is ready for modeling and analysis.



    ### Jupyter Notebooks Overview:

        1. raw_data_downloader.ipynb: This notebook is responsible for downloading the raw datasets from specified sources. It includes code to handle any potential errors during the download process and ensures that the data is stored in the appropriate format.

        2. raw_data_processor.ipynb: This notebook processes the raw data, converting it into a more usable format. It includes functions to read the raw data files and perform initial cleaning steps, such as handling missing values and formatting.

        3. data_processor.ipynb: This notebook reads the processed data files and merges them into a single DataFrame. It includes functions for reading multiple CSV files, merging dataframes based on specified columns, and sorting the final combined dataset.

        4. linear_interpreter.ipynb: This notebook focuses on interpreting the data using linear regression techniques. It includes code for defining features and targets, fitting the model, and evaluating its performance through various metrics.

        5. model_builder.ipynb: This notebook builds and evaluates machine learning models, including neural networks and random forests. It provides insights into model performance through metrics such as Mean Squared Error (MSE) and R-squared values.