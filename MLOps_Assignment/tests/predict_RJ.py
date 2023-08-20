import hydra
from omegaconf import DictConfig


#this i not sure
@hydra.main(config_path="../config/predict", config_name="predict_RJ", version_base=None) # will access main.yaml in config folder
def train_model(config: DictConfig):
    """Function to predict label"""

    # print(f"Train modeling using {config.data.proc}")
    # print(f"Model used: {config.modelparam.name}")
    # print(f"Save the output to {config.data.fpath}")
    # model = create_model(f'{config.modelparam.model}', n_estimators = {config.modelparam.n_estimators})
    # # finalize the model
    # final_best = finalize_model(model)

    # # save model to disk
    # save_model(final_best, 'hdb_pipeline')

    X_test = #all new inputs
    model = mlflow.sklearn.load_model(f'{config.mlflow.model}')
    pred = model.predict(X_test)

    print(f'Predicted Resale Price is: {}'.format(pred))


if __name__ == "__main__":
    train_model()