import json
from pathlib import Path
from config import BASE_DIR


def load_schema(file_name: str) -> dict:
    """Загружает JSON-схему из файла."""
    schema_path = Path(BASE_DIR) / 'project_test_demoblaze' / 'json_schemas' / file_name
    with schema_path.open(encoding='utf-8') as file:
        return json.load(file)
