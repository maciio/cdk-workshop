from dynaconf import Dynaconf

# settings = LazySettings(
#     ROOT_PATH_FOR_DYNACONF="./configuration/"
# )
settings = Dynaconf(
    settings_files=[                      # Paths or globs to any toml|yaml|ini|json|py
        "config/default_settings.toml",  # a file for default settings
        "config/settings.toml",          # a file for main settings
        "config/.secrets.toml"           # a file for sensitive data (gitignored)
    ],

    environments=True,                    # Enable layered environments
                                          # (sections on config file for development, production, testing)

    load_dotenv=True,                     # Load envvars from a file named `.env`
                                          # TIP: probably you don't want to load dotenv on production environments
                                          #      pass `load_dotenv={"when": {"env": {"is_in": ["development"]}}}

    envvar_prefix="DYNACONF",             # variables exported as `DYNACONF_FOO=bar` becomes `settings.FOO == "bar"`
    env_switcher="ENV_FOR_DYNACONF",      # to switch environments `export ENV_FOR_DYNACONF=production`

    dotenv_path="configs/.env"            # custom path for .env file to be loaded
)

env = settings.get("ENV", None)
if not env:
    raise EnvironmentError("Please set environment: USE `export ENV_FOR_DYNACONF=environment` e.g. [dev, stage]")
    
class ConfigurationLoader:

    @staticmethod
    def getSetting(setting_key: str):
        return settings[setting_key]
    @staticmethod
    def getSettings():
        return settings
    @staticmethod
    def build_naming_convention(resource_name: str):
        env = settings.ENV
        project_name = settings.PROJECT_NAME
        return f"{env}-{project_name}-{resource_name}-stack"
    @staticmethod
    def build_simple_name(resource_name: str):
        env = settings.ENV
        return f"{env}-{resource_name}"