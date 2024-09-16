from django.db import connection
from django.contrib.auth.hashers import make_password
import os
from dotenv import load_dotenv
from django import setup

load_dotenv()
setup()
# settings.configure()

data = {
    'User': [
        {
            'email': 'gredg32@gmail.com',
            'password': make_password('Gtse32t5'),
            'is_superuser': True
        },
        {
            'email': 'Hgr2@gmail.com',
            'password': make_password('Hhb43f')
        }
    ]
}

model_update_fields = {
    'User': ['email']
}

model_unique_fields = {
    'User': ['email']
}


def get_custom_models():
    tables = connection.introspection.table_names()
    seen_models = connection.introspection.installed_models(tables)

    model_mapping = tuple({model.__name__: model} for model in seen_models if model.__name__ not in ('Session', 'Permission', 'Group',
                                                                                            'ContentType', 'LogEntry'))
    return model_mapping


def get_objects_data(model_name, model):
    return data.get(model_name)


def create_model_objects(list_of_objects_data, model):
    objects = [model(**object_data) for object_data in list_of_objects_data]
    return objects


def save_objects(object_list, model, model_name):
    update_fields = model_update_fields.get(model_name)
    unique_fields = model_unique_fields.get(model_name)
    model.objects.bulk_create(object_list, update_conflicts=True, update_fields=update_fields,
                              unique_fields=unique_fields)


def seed_models(model_list):
    for item in model_list:
        model_name, model = list(item.items())[0]
        model_data = get_objects_data(model_name, model)
        object_list = create_model_objects(model_data, model)
        save_objects(object_list, model, model_name)


models = get_custom_models()
seed_models(models)





