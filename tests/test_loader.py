import pandas as pd
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import logistics_model.models
from logistics_model.database import Base
from logistics_model.services.loader import load_workbook


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db_session = Session()
    yield db_session
    db_session.close()


def test_load_workbook_validates_and_skips_invalid_rows(session, tmp_path):
    excel_path = tmp_path / "test_data.xlsx"

    df_basin = pd.DataFrame({"name": ["Test Basin"]})
    df_port = pd.DataFrame(
        {
            "name": ["", "Invalid Basin ID", "Valid Port"],
            "basin_id": [1, -1, 1],
            "container_turnover": [10.0, 20.0, 30.0],
        }
    )

    with pd.ExcelWriter(excel_path) as writer:
        df_basin.to_excel(writer, sheet_name="basin", index=False)
        df_port.to_excel(writer, sheet_name="port", index=False)

    load_workbook(session, str(excel_path))

    ports = session.query(logistics_model.models.Port).all()
    assert len(ports) == 1
    assert ports[0].name == "Valid Port"
