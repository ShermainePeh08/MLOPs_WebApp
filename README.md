# MLOps WebApp
View our web application here!: https://srj-mlops.streamlit.app/ 

Objective: Build an end to end Maching Learning system using Pycaret and Deploy it.

Tasks:
1. Train, Validate & Develop Machine Learning Pipeline using Pycaret
    - HDB Resale Price
    - Medical Cardiovascular Health
2. Build & Deploy a front-end web application with real-time prediction
    - Using Streamlit
3. Set up development & deployment environment according to MLOPs Lifecycle

## Tools Used
- Poetry: Dependency Management
- Hydra: Manage Config Files
- DVC: Data Version Control 

## Cookiecutter Setup
pip install cookiecutter
```bash
cookiecutter {link} --checkout dvc-poetry
```
## MLOPs Lifecycle
### DVC
- Data Version Control was used on the data folder to manage and version data.
    - To initialize dvc run
        ```bash 
        dvc init
        ```
    - To track data folder run
        ```bash 
        dvc add data/ 
        ```
- The above commands will create a .gitignore and data.dvc file that tracks the changes in the data folder

### Hydra
- Hydra helps streamline experiment processes by providing a consistent and organized way to manage configurations
- Before hydra implementation
    - All parameters were hard-coded into the python notebooks like hdb_RJ.ipynb and medical.ipynb
- After hydra implementation
    - All configurations such as pycaret setup parameters are configured in config/process/ folder .yaml files
- This allows easy changes in configurations instead of having to scroll throught entire notebook

## Streamlit Web Application
```bash
pip install streamlit
```
- pycaret model saved within models folder
	- Regression model for HDB Resale Price
	- Classification model on predicting Cardiovascular Issues 
- load pycaret model into system 
- setup pages folders for multipage 
- page split into 2 to display forms and prediction
	- prediction is updated live as input is being edited 
streamlit run {python file}

## Deployment
https://streamlit.io/cloud
- Deployment created on streamlit cloud 
- Create new App and link to GitHub's Streamlit WebApp
- Create requirements.txt file 
	```bash
    pip freeze > requirements.txt
    ```
## Folder Structure
```
MLOPS_WEBAPP:
    .dvcignore
    .gitignore
    README.md
    MLOps_Assignment
    │   .gitignore
    │   .pre-commit-config.yaml
    │   data.dvc
    │   Makefile
    │   poetry.lock
    │   pyproject.toml
    │   README.md
    │
    ├───.dvc
    │       .gitignore
    │       config
    │
    ├───streamlit_deploy
    │   │   Homepage.py
    │   │   requirements.txt
    │   │
    │   ├───pages
    │          HDB_Prediction.py
    │          Medical_Prediction.py
    |
    ├───config
    │   │   main.yaml
    │   │
    │   ├───model
    │   │       model1.yaml
    │   │       model2.yaml
    │   │
    │   └───process
    │           process_RJ.yaml
    │           process_Shermaine.yaml
    │
    ├───data
    │   │   
    │   │
    │   ├───final
    │   │       .gitkeep
    │   │
    │   ├───processed
    │   │       .gitkeep
    |   |       hdb_processed.csv
    |   |       medical_processed.csv
    │   │
    │   └───raw
    │           .gitkeep
    │           01_hdb_resale_transactions.csv
    │           02_medical_records.csv
    │
    ├───docs
    │       .gitkeep
    │
    ├───models
    │       .gitkeep
    │       best_gbr__pipeline.pkl
    │       cv_issue-pipeline.pkl
    │       cv_issue-pipeline_testing.pkl
    │       resale_price_pipeline_zx.pkl
    │
    ├───notebooks
    │   │   .gitkeep
    │   │
    │   ├───RuiJie
    │   │       hdb_Hydra.ipynb
    │   │       hdb_RJ.ipynb
    |   |       mlruns
    |   |       logs.log
    │   │
    │   └───Shermaine
    │           logs.log
    │           medical-hydra.ipynb
    │           medical.ipynb
    │
    ├───src
    │       process.py
    │       train_model.py
    │       __init__.py
    │
    └───tests
            test_process.py
            test_train_model.py
            __init__.py
```
## Roles:
- Shermaine: Medical Cardiovascular Health
- RuiJie: HDB Resale Price