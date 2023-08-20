import hydra
from omegaconf import DictConfig


@hydra.main(config_path="../config/model", config_name="model_RJ", version_base=None) # will access main.yaml in config folder
def train_model(config: DictConfig):
    """Function to train the model"""

    print(f"Train modeling using {config.data.proc}")
    print(f"Model used: {config.modelparam.name}")
    print(f"Save the output to {config.data.fpath}")
    model = create_model(f'{config.modelparam.model}', n_estimators = {config.modelparam.n_estimators})
    # finalize the model
    final_best = finalize_model(model)

    # save model to disk
    save_model(final_best, 'hdb_pipeline')


if __name__ == "__main__":
    train_model()
