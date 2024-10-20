from sqlalchemy import Column, ForeignKey, Integer, Text

from app.core import Base
from .mixins import Invested


class Donation(Invested, Base):
    comment = Column(Text, nullable=True)
    user_id = Column(Integer,
                     ForeignKey(
                         column='user.id',
                         name='fk_donation_user_id_user'),
                     index=True)

    def __repr__(self):
        return (
            f"<Donation("
            f"user_id={self.user_id}, "
            f"{super().__repr__()})>")
