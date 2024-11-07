class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app_postgres':
            return 'default'
        elif model._meta.app_label == 'app_mysql':
            return 'mysql_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app_postgres':
            return 'default'
        elif model._meta.app_label == 'app_mysql':
            return 'mysql_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'app_postgres':
            return db == 'default'
        elif app_label == 'app_mysql':
            return db == 'mysql_db'
        return None
