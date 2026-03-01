from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database import Base

class Abstract(Base):
    __tablename__ = "abstracts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    original_text = Column(Text)
    improved_text = Column(Text)
    style = Column(String)
