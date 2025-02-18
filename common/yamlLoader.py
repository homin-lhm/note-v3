from main import DIR, ENVIRON
import yaml


class YamlRead:
    @staticmethod
    def env_config():
        """环境变量的读取方式"""
        with open(file=f'{DIR}/data/envConfig/{ENVIRON}/config.yml', mode='r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    @staticmethod
    def api_config():
        with open(file=f'{DIR}/data/apiConfig/config.yml', mode='r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)
