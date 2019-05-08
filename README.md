# Places365-Nets

## Requirements

### UNIX Packages

| **Packages**  | **Purpose**                                                    |
| ------------- | -------------------------------------------------------------- |
| **wget, tar** | **Download** and **Extract** **Places365** Easy Format Dataset |

### Python Packages

| **Package**     | **Version** |
| --------------- | ----------- |
| **python**      | 3.6         |
| **numpy**       | 1.15.4      |
| **progressbar** | 2.5         |
| **imageio**     | 2.4.1       |

## Instructions to Train and Evaluate the Model

1.  `./download_places365` - Command to Download and Extract the Places365 Dataset.
2.  Clean the dataset and remove grayscale images.
    -   `python clean_places365.py train` - Clean the training dataset
    -   `python clean_places365.py val` - Clean the validation dataset

## Files

-   `download_places365` - Executable script to download and extract the Places365 dataset.
-   `clean_places365.py` - Script to clean the dataset. 
-   `classes.txt` - Sorted list of classes in Places365.

## Folders

-   `places365_standard` - Created by `download_places365`
    -   `train.txt` - List of path to files in training set
    -   `val.txt` - List of path to files in validation set
    -   `train` - Contains 365 scene category partitions, with 900 images per category
        -   `airfield`
        -   `airplane_cabin`
        -   `airport_terminal`
        -   ... 362 more folders
    -   `test` - Contains 365 scene category partitions, with 100 images per category
        -   `airfield`
        -   `airplane_cabin`
        -   `airport_terminal`
        -   ... 362 more folders
