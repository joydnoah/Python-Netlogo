from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Data(Base):
    __tablename__ = 'Data'
    id = Column(Integer, primary_key=True)
    data = Column(String)
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return 'id: {}, root cause: {}'.format(self.id, self.root_cause)