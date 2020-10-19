



class CheckerRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'posts':
            return 'd61nc0nbgsq65g'
        elif model._meta.app_label == 'users':
            return 'dee41dc7ts59ga'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'posts':
            return 'd61nc0nbgsq65g'
        elif model._meta.app_label == 'users':
            return 'dee41dc7ts59ga'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'posts' or obj2._meta.app_label == 'posts':
            return True
        elif 'posts' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        elif obj1._meta.app_label == 'users' or obj2._meta.app_label == 'users':
            return True
        elif 'users' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'posts':
            return db == 'd61nc0nbgsq65g'
        elif app_label == 'users':
            return db == 'djlbldcxpzonpy'
        return None