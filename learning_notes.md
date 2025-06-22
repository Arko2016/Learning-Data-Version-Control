### DVC
- Stands for Data Version Control tool
- Used to manage and version images, audio, video, and text files in storage and organize your ML modeling process into a reproducible workflow
- **Note:** DVC works on data version control in conjunction with code control using Git

### Stages in Machine Learning(ML) project:
- Data Ingestion
- Data Preprocessing
- Feature Engineering
- Feature Selection
- Model Training
- Model Evaluation
- Deployment

### Why can't Git be used for DVC?
- **Data limitations:** Git is primarily optimized for text-based files and has repository limitations for strong large data files and repositories
- **Performance Issues:** Git has performance issues with large files and Inefficient storage of binary data

### Git and DVC Integrated Workflow:
- **Git tracks DVC metafiles** : Git is used to version and manage the code and small metadata files (like .dvc files and dvc.yaml) that describe the DVC-tracked data and its versions
- **DVC manages large data**: DVC handles the actual large data files and models, storing them in a DVC cache (local or shared) and synchronizing them with configured DVC remotes (e.g., cloud storage like S3, Google Cloud Storage, or local shared volumes)
- **Always do git pull first** : When collaborating or moving between machines, you typically run git pull first to update your local repository with the latest .dvc files and dvc.yaml from the Git remote. This brings down the metadata about the data versions
    - Alternatively, if you want to revert back to an older version of the data, you can track back using the git hashid
- **Follow by dvc pull**: this will then bring back/download the respective version data from DVC remote based on .dvc files
