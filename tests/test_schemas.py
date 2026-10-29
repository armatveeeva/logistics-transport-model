import pytest
from pydantic import ValidationError

from logistics_model.schemas.port import PortIn


def test_port_in_validation_fails_on_empty_name():
    """Проверка, что пустое имя порта корректно отклоняется валидатором."""
    with pytest.raises(ValidationError):
        PortIn(name="", basin_id=1)


def test_port_in_validation_fails_on_negative_basin_id():
    """Проверка, что некорректный basin_id (если есть gt=0) отклоняется."""
    with pytest.raises(ValidationError):
        PortIn(name="Тестовый порт", basin_id=-1)
