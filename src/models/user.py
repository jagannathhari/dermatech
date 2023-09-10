
from sqlalchemy import create_engine, Column, Integer, String,Date, ForeignKey, Table 
from sqlalchemy.orm import relationship, Session, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    birthdate = Column(Date)
    contact = Column(String)
    email = Column(String, unique=True)
    profile_photo = Column(String)
    health_records = relationship("HealthRecord", back_populates="user")

    uploaded_skin_images = relationship("UploadedSkinImage", back_populates="user")


class HealthRecord(Base):
    __tablename__ = "health_records"

    id = Column(Integer, primary_key=True)
    disease = Column(String)
    time_duration = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="health_records")


class UploadedSkinImage(Base):
    __tablename__ = "uploaded_skin_images"

    id = Column(Integer, primary_key=True)
    image = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="uploaded_skin_images")


if __name__ == "__main__":
    engine = create_engine("sqlite:///my_database.db")
    Base.metadata.create_all(engine)

    session = Session(engine)

    user = User(
        name="John Doe",
        age=30,
        contact="123-456-7890",
        email="john@example.com",
        photo="john.jpg",
    )
    user.health_records = [
        HealthRecord(disease="Disease1", time_duration="6 months"),
        HealthRecord(disease="Disease2", time_duration="1 year"),
    ]
    user.uploaded_skin_images = [
        UploadedSkinImage(image="image1.jpg"),
        UploadedSkinImage(image="image2.jpg"),
    ]
    session.add(user)
    session.commit()
