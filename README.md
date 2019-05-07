# places365-nets

## Requirements

### UNIX Packages

|  **Packages** |                           **Purpose**                          |
| :-----------: | :------------------------------------------------------------: |
| **wget, tar** | **Download** and **Extract** **Places365** Easy Format Dataset |

### Python Packages

| **Package** | **Version** |
| :---------: | :---------: |
|  **python** |     3.6     |

## Files

-   `download_places365` - Executable script to download and extract the Places365 dataset.
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
