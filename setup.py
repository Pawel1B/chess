from chess_package.game import game
import yaml
import os


def load_configs():
    dirs=os.listdir("configs")
    configs={}
    for dir in dirs:
        with open(f'configs/{dir}',"r") as f:
            data=yaml.safe_load(f)
        configs[dir]=data
    return configs
configs=load_configs()


def main():
    our_game=game(configs["config.yml"])
    our_game.run()


if __name__ == "__main__":
    main()
