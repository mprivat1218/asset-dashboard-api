from database import Base
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey

class Client(Base):
    __tablename__ = "clients"

    #PK column, it's inferred as autoincrementing int
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    risk_tolerance: Mapped[str]

    #one-to-many relationship, single client holds multiple assets, allows easy access to a client's stock holdings
    portfolios: Mapped[list["Portfolio"]] = relationship("Portfolio", back_populates="client")

class Portfolio(Base):
    __tablename__ = "portfolios"
    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    ticker_symbol: Mapped[str]
    shares: Mapped[int]
    client: Mapped[list["Client"]] = relationship("Client", back_populates="portfolios")