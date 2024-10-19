from sqlalchemy import Column, String, Text

from app.core import Base
from .mixins import InvestedMixin


class CharityProject(InvestedMixin, Base):
    name = Column(String(
        length=100),
        unique=True,
        nullable=False)
    description = Column(
        Text,
        nullable=False)

    def __repr__(self):
        return (
            f"<CharityProject("
            f"name={self.name}, "
            f"description={self.description}, "
            f"{super().__repr__()})>")
