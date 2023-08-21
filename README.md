# MLOPs_WebApp

Nanyang Polytechnic: Machine Learning Operations Assignment 2023.

Objective: Build an end to end Maching Learning system and Deploy it

Tasks:
1. Train, Validate & Develop Machine Learning Pipeline using Pycaret
- HDB Resale Price
- Medical Cardiovascular Health
2. Build & Deploy a front-end web application with real-time prediction
- Using Streamlit
3. Set up development & deployment environment according to MLOPs Lifecycle
- Poetry
- DVC
- Hydra
- Pdoc

## Streamlit Web Application


## Deployment


## MLOPs Lifecycle
### DVC
Data Version Control was used on the data folder to manage and version data.

To initialize dvc run:
dvc init

To track data folder run:
dvc add data/ 

The above commands will create a .gitignore and data.dvc file that tracks the changes in the data folder

### Hydra
Hydra helps streamline experiment processes by providing a consistent and organized way to manage configurations

Before hydra implementation:
All parameters were hard-coded into the python notebooks like hdb_RJ.ipynb and medical.ipynb

After hydra implementation:
All configurations such as pycaret setup parameters are configured in config/process/ folder yaml files

This allows easy changes in configurations instead of having to scroll throught entire notebook

## Roles:
Shermaine: Medical Cardiovascular Health

RuiJie: HDB Resale Price