from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class SystemBezeichnung(BaseModel):
    system1: str
    system2: str
    system3: str
    system4: str

class Schnittstelle(BaseModel):
    modbusTCP_IP: str
    snmp: str
    opc_ua: str
    mqtt: str
    profibus: str

class Teilnehmer(BaseModel):
    systembezeichnungen: SystemBezeichnung
    schnittstellen: Schnittstelle
    ipAdresse: str
    macAdresse: str
    vlan: int
    port: int
    inventarisierungsnummer: str
    beschreibung: str
    kommentar: str
    abteilung: str
    keyuser: str
    erstellungsdatum: datetime
    letzteAenderung: datetime

class Netzwerkanschluss(BaseModel):
    switch: Dict[str, str]
    teilnehmer: List[Teilnehmer]

class Fertigungsmaschine(BaseModel):
    typ: str
    inventarisierungsnummer: str
    beschreibung: str
    kommentar: str
    abteilung: str
    keyuser: str
    erstellungsdatum: datetime
    letzteAenderung: datetime
    netzwerkanschluss: Netzwerkanschluss
