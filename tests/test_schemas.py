from datetime import date

import pytest
from pydantic import ValidationError

from logistics_model.schemas.basin import BasinIn
from logistics_model.schemas.container_turnover import ContainerTurnoverIn
from logistics_model.schemas.port import PortIn


def test_basin_in_valid():
    basin = BasinIn(name="Балтийский бассейн")
    assert basin.name == "Балтийский бассейн"


def test_basin_in_invalid_empty_name():
    with pytest.raises(ValidationError):
        BasinIn(name="")


def test_port_in_valid():
    port = PortIn(name="Большой порт Санкт-Петербург", basin_id=1, container_turnover=150.5)
    assert port.name == "Большой порт Санкт-Петербург"
    assert port.basin_id == 1


def test_port_in_invalid_negative_basin_id():
    with pytest.raises(ValidationError):
        PortIn(name="Тест", basin_id=-1)


def test_container_turnover_in_valid_date():
    ct = ContainerTurnoverIn(port_id=1, date=date(2023, 1, 31), teu=100.0)
    assert ct.date == date(2023, 1, 31)
