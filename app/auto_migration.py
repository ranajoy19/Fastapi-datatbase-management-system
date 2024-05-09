import alembic.config
from alembic import command

def migrate_database(current_version):
    # List of migration versions in order
    migration_versions = [
        '3dec6c402185', # a)
        '8948c2cca505', # b)
        '9259a6edad0a', # c)
        'dee430663c1d', # d)
        'b701adb4ee94'  # e)
    ]
    alembic_cfg = alembic.config.Config("alembic.ini")
    # Determine the index of the current version in the list
    current_index = migration_versions.index(current_version)
    
    # Migrate to the latest version
    for migration_version in migration_versions[current_index:]:
        command.upgrade(alembic_cfg, revision=migration_version)

if __name__ == "__main__":
    current_version = '3dec6c402185'  
    migrate_database(current_version)
