from alembic import command
from alembic.config import Config

def run_database_migration():
    # Specify the path to your Alembic configuration file
    alembic_config_path = '/path/to/alembic.ini'
    
    # Create an Alembic configuration object
    alembic_config = Config(alembic_config_path)
    
    # Run the database migration
    command.upgrade(alembic_config, 'head')

# Example usage
run_database_migration()

