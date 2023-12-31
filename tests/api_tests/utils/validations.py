from jsonschema import validate
import os
import json
import allure


def load_schema(name):
    current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    schemas_path = os.path.join(current_path, f'schemas')
    path = os.path.join(schemas_path, name)
    with open(path) as file:
        schema = json.loads(file.read())
    return schema


@allure.step("Валидация схемы")
def validate_schema(current_response, schema_name):
    schema = load_schema(schema_name)
    validate(instance=current_response, schema=schema)


@allure.step("Проверка статус кода")
def assert_status_code(current_status_code, expected_status_code):
    assert current_status_code == expected_status_code, f'Current status_code == {current_status_code}; Expected status_code == {int(expected_status_code)} '
