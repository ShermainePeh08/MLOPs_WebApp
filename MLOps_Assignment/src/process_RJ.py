import hydra
from omegaconf import DictConfig


@hydra.main(config_path="../config/process", config_name="process_RJ", version_base=None)
def process_data(config: DictConfig):
    """Function to process the data"""

    print(f"Process data using {config.data.raw}")
    hdb = pd.read_csv(f"{config.data.raw}")
    hdb_nodup = hdb.drop_duplicates()
    hdb_nodup['month'] = pd.to_datetime(hdb_nodup['month'], format='%Y-%m')
    hdbsetup = setup(data=hdb_nodup, target=f'{config.setup.target}', train_size=f'{config.setup.trainsize}',transformation=f'{config.setup.transform}',
                normalize=f'{config.setup.norm}',session_id=f'{config.setup.session}', 
                log_experiment=f'{config.setup.logexp}',experiment_name=f'{config.setup.expname}', remove_outliers=f'{config.setup.rmoutlier}',
                fold=f'{config.setup.fold}', ignore_features=[f'{config.setup.ignore}'], bin_numeric_features = [f'{config.setup.bin}'],
                date_features=[f'{config.setup.date}']
                )

    print(f'Numeric features: {hdbsetup._fxs["Numeric"]}')
    print(f'Categorical features: {hdbsetup._fxs["Categorical"]}')
    print(f'Date features: {hdbsetup._fxs["Date"]}')

    df = hdbsetup.get_config('dataset_transformed')
    file_name = 'hdb_processed.csv'
    file_path = f'{config.data.ppath}
    full_file = file_path + file_name
    df.to_csv(full_file, index=False)

    print(f'Data was processed and written at {}.'.format(full_file))

if __name__ == "__main__":
    process_data()
