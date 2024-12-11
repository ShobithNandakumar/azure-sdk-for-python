from featuremanagement import FeatureManager
from azure.appconfiguration.provider import load
from azure.appconfiguration import AzureAppConfigurationClient
import json


class ModelConfiguration:
    """ Class definition of Model Configurations to be loaded. """
    
    def __init__(self, app_config_connection_string: str, key: str):
        """ init constructor for Model Configuration class. """
        self.app_config_connection_string = app_config_connection_string
        self.app_config_client = AzureAppConfigurationClient.from_connection_string(
            app_config_connection_string
        )
        self.connection_string = app_config_connection_string
        self.app_config_connection_string = app_config_connection_string
        self.key = key
        self.config_provider = load(
            connection_string=app_config_connection_string,
            feature_flag_enabled=True,
            feature_flag_refresh_enabled=True,
        )
        self.feature_manager = FeatureManager(self.config_provider)

    def get_all_models_configs(self):
        """ get all model configs for enabled feature flags """
        setting = self.app_config_client.list_configuration_settings(
            key_filter=".appconfig.featureflag/%s" % self.key
        )
        model_configs = json.loads(setting.next().value)
        return model_configs.get("variants")

    def get_model_config(self, user_id):
        """ get model configs using user id """
        self.config_provider.refresh()
        return self.feature_manager.get_variant(self.key, user_id)

    def get_model_config_feature_flag(self, ff_key: str):
        """ get model configs using feature flag key """
        self.config_provider.refresh()
        setting = self.app_config_client.list_configuration_settings(
            key_filter=".appconfig.featureflag/%s" % self.key
        )
        model_configs = json.loads(setting.next().value)
        return model_configs.get(ff_key)
    
    def get_model_config_from_file_path(self, file_path: str):
        """ get model configs from file path """
        with open(file_path) as f:
            model_configs = json.load(f)
        return model_configs
