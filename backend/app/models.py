from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Dict
from datetime import datetime

# Define the base class for SQLAlchemy models
Base = declarative_base()

class DBSystemName(Base):
    """
    Represents the 'system_names' table in the database.
    """
    __tablename__ = 'system_names'
    id = Column(Integer, primary_key=True)
    system_names = Column(JSON)
    participant_id = Column(Integer, ForeignKey('participants.id'))

class DBInterface(Base):
    """
    Represents the 'interfaces' table in the database.
    """
    __tablename__ = 'interfaces'
    id = Column(Integer, primary_key=True)
    modbusTCP_IP = Column(String)
    snmp = Column(String)
    opc_ua = Column(String)
    mqtt = Column(String)
    profibus = Column(String)
    participant_id = Column(Integer, ForeignKey('participants.id'))

class DBParticipant(Base):
    """
    Represents the 'participants' table in the database.
    """
    __tablename__ = 'participants'
    id = Column(Integer, primary_key=True)
    ip_address = Column(String)
    mac_address = Column(String)
    vlan = Column(Integer)
    port = Column(Integer)
    inventory_number = Column(String)
    description = Column(String)
    comment = Column(String)
    department = Column(String)
    key_user = Column(String)
    creation_date = Column(DateTime)
    last_change = Column(DateTime)
    system_names = relationship("DBSystemName", backref="participant")
    interfaces = relationship("DBInterface", backref="participant")

class DBManufacturingMachine(Base):
    """
    Represents the 'manufacturing_machines' table in the database.
    """
    __tablename__ = 'manufacturing_machines'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    inventory_number = Column(String)
    description = Column(String)
    comment = Column(String)
    department = Column(String)
    key_user = Column(String)
    creation_date = Column(DateTime)
    last_change = Column(DateTime)
    network_connection = Column(JSON)

class SystemNameItem(BaseModel):
    """
    Pydantic model for an item in system names.
    """
    name: str
    description: Optional[str] = None
    key_user: Optional[str] = None
    link: Optional[HttpUrl] = None

class SystemName(BaseModel):
    """
    Pydantic model for system names.
    """
    system_names: List[SystemNameItem]

class Interface(BaseModel):
    """
    Pydantic model for interface types.
    """
    modbusTCP_IP: str
    snmp: str
    opc_ua: str
    mqtt: str
    profibus: str

class ParticipantCreate(BaseModel):
    """
    Pydantic model for creating a new participant.
    """
    system_names: SystemName
    interfaces: Interface
    ip_address: str
    mac_address: str
    vlan: int
    port: int
    inventory_number: str
    description: str
    comment: str
    department: str
    key_user: str
    creation_date: datetime
    last_change: datetime

class Participant(ParticipantCreate):
    """
    Pydantic model for a participant with an ID.
    """
    id: int

class NetworkConnection(BaseModel):
    """
    Pydantic model for network connection.
    """
    switch: Dict[str, str]
    participants: List[Participant]

class ManufacturingMachineCreate(BaseModel):
    """
    Pydantic model for creating a new manufacturing machine.
    """
    type: str
    inventory_number: str
    description: str
    comment: str
    department: str
    key_user: str
    creation_date: datetime
    last_change: datetime
    network_connection: NetworkConnection

class ManufacturingMachine(ManufacturingMachineCreate):
    """
    Pydantic model for a manufacturing machine with an ID.
    """
    id: int
