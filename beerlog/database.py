from sqlmodel import create_engine
from beerlog.config import settings
from beerlog import models

engine = create_engine(settings.database.URL)

models.SQLModel.metadata.create_all(engine)