from omegaconf import DictConfig, OmegaConf, MissingMandatoryValue, open_dict
from pytest import raises
import hydra
import os 
import logging 
from hydra.core.hydra_config import HydraConfig

log = logging.getLogger(__name__) # Tạo logger cho file hiện tại 
@hydra.main()
def my_app(cfg: DictConfig) -> None:
    log.info("Info level message")
    log.debug("Debug level message")
if __name__== "__main__":
    my_app()