from dataclasses import dataclass
import hydra
from hydra.core.config_store import ConfigStore
@dataclass
class MySQLconfig:
    host: str = "localhost"
    port: int = 3306

cs = ConfigStore.instance()

cs.store(name="config", node = MySQLconfig)

@hydra.main(config_name="config")
def my_app(cfg: MySQLconfig) -> None:
    print(f"Host: {cfg.host}, port: {cfg.port}")

if __name__ == "__main__":
    my_app()