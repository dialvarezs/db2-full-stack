from litestar import Litestar
from litestar.config.cors import CORSConfig

from app.controlers import AuthorController, BookController
from app.database import sqlalchemy_config

cors_config = CORSConfig(allow_origins=["http://localhost:5173"])

app = Litestar(
    [AuthorController, BookController],
    debug=True,
    plugins=[sqlalchemy_config],
    cors_config=cors_config
)
