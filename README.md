# File utils

Small Python scripts that I use for making my life easier when needing to work with lots of files in Azure Blob storage with the [Books API](https://github.com/Project-Books/books-api).

This has been made specific to my use case, so it may need modifying to suit yours.

## High-level overview
- [create_dir.py](https://github.com/knjk04/file-utils/blob/main/src/create_dir.py) is used to create folders where the name of the folder is a number.
    - E.g. if you pass in 1 as the start and 50 as the end, it will create folders called 1, 2, 3, ..., 50
- [move_files.py](https://github.com/knjk04/file-utils/blob/main/src/move_files.py) uses create_dir.py to create new directories. It then moves files at the location the user wants to those new folders

![image](https://user-images.githubusercontent.com/11173328/132993638-77a83295-2f0f-4711-bf4b-9ffd39c6e110.png)

![image](https://user-images.githubusercontent.com/11173328/132993579-2f8c7e9e-46f9-462d-be84-cb5062a385ee.png)

The image above shows the numbered folders. Each folder contains a single image where the images were previously in the parent folder of the numbered folders (1st image)
