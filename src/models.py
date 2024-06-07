"""Autogenerated SQLAlchemy models based on OpenAlchemy models."""
# pylint: disable=no-member,super-init-not-called,unused-argument

import datetime
import typing

import sqlalchemy
from sqlalchemy import orm

from open_alchemy import models

Base = models.Base  # type: ignore


class _MeasurementDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    lat: float
    long: float
    time: str
    variable: str


class MeasurementDict(_MeasurementDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int
    value: typing.Optional[float]


class TMeasurement(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        id: Identifikacioni broj (interni ključ)
        lat: Geografska širina
        long: Geografska dužina
        time: Vreme merenja
        variable: Naziv meteorološke promenljive
        value: Vrednost meteorološke promenljive

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    lat: 'sqlalchemy.Column[float]'
    long: 'sqlalchemy.Column[float]'
    time: 'sqlalchemy.Column[datetime.datetime]'
    variable: 'sqlalchemy.Column[str]'
    value: 'sqlalchemy.Column[typing.Optional[float]]'

    def __init__(self, lat: float, long: float, time: datetime.datetime, variable: str, id: typing.Optional[int] = None, value: typing.Optional[float] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (interni ključ)
            lat: Geografska širina
            long: Geografska dužina
            time: Vreme merenja
            variable: Naziv meteorološke promenljive
            value: Vrednost meteorološke promenljive

        """
        ...

    @classmethod
    def from_dict(cls, lat: float, long: float, time: datetime.datetime, variable: str, id: typing.Optional[int] = None, value: typing.Optional[float] = None) -> "TMeasurement":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (interni ključ)
            lat: Geografska širina
            long: Geografska dužina
            time: Vreme merenja
            variable: Naziv meteorološke promenljive
            value: Vrednost meteorološke promenljive

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TMeasurement":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> MeasurementDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Measurement: typing.Type[TMeasurement] = models.Measurement  # type: ignore


class _LocationDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str
    country: str
    lat: float
    long: float
    type: str
    altitude: float


class LocationDict(_LocationDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TLocation(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        id: Identifikacioni broj (interni ključ)
        name: Naziv lokacije
        country: Država lokacije
        lat: Geografska širina
        long: Geografska dužina
        type: Tip lokacije (grad, selo, planinski vrh, jezero, reka, itd.)
        altitude: Nadmorska visina

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    country: 'sqlalchemy.Column[str]'
    lat: 'sqlalchemy.Column[float]'
    long: 'sqlalchemy.Column[float]'
    type: 'sqlalchemy.Column[str]'
    altitude: 'sqlalchemy.Column[float]'

    def __init__(self, name: str, country: str, lat: float, long: float, type: str, altitude: float, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv lokacije
            country: Država lokacije
            lat: Geografska širina
            long: Geografska dužina
            type: Tip lokacije (grad, selo, planinski vrh, jezero, reka, itd.)
            altitude: Nadmorska visina

        """
        ...

    @classmethod
    def from_dict(cls, name: str, country: str, lat: float, long: float, type: str, altitude: float, id: typing.Optional[int] = None) -> "TLocation":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv lokacije
            country: Država lokacije
            lat: Geografska širina
            long: Geografska dužina
            type: Tip lokacije (grad, selo, planinski vrh, jezero, reka, itd.)
            altitude: Nadmorska visina

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TLocation":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> LocationDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Location: typing.Type[TLocation] = models.Location  # type: ignore


class _VariableDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str
    data_type: str
    unit: str
    accuracy: str
    measurement_range: str
    frequency: str
    source: str
    description: str


class VariableDict(_VariableDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TVariable(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Meteorološka promenljiva

    Attrs:
        id: Identifikacioni broj (interni ključ)
        name: Naziv meteorološke promenljive.
        data_type: Tip podataka koji se meri (npr. float, integer, string).
        unit: Jedinica merenja (npr. °C, %, m/s).
        accuracy: Tačnost merenja promenljive (npr. ±0.5°C, ±5%).
        measurement_range: Opseg vrednosti koje se mogu meriti.
        frequency: Frekvencija uzorkovanja podataka (npr. svakih 5 minuta,
            svakog sata).
        source: Izvor podataka o promenljivoj (npr. meteorološka stanica,
            senzor).
        description: Detaljan opis meteorološke promenljive.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    data_type: 'sqlalchemy.Column[str]'
    unit: 'sqlalchemy.Column[str]'
    accuracy: 'sqlalchemy.Column[str]'
    measurement_range: 'sqlalchemy.Column[str]'
    frequency: 'sqlalchemy.Column[str]'
    source: 'sqlalchemy.Column[str]'
    description: 'sqlalchemy.Column[str]'

    def __init__(self, name: str, data_type: str, unit: str, accuracy: str, measurement_range: str, frequency: str, source: str, description: str, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv meteorološke promenljive.
            data_type: Tip podataka koji se meri (npr. float, integer, string).
            unit: Jedinica merenja (npr. °C, %, m/s).
            accuracy: Tačnost merenja promenljive (npr. ±0.5°C, ±5%).
            measurement_range: Opseg vrednosti koje se mogu meriti.
            frequency: Frekvencija uzorkovanja podataka (npr. svakih 5 minuta,
                svakog sata).
            source: Izvor podataka o promenljivoj (npr. meteorološka stanica,
                senzor).
            description: Detaljan opis meteorološke promenljive.

        """
        ...

    @classmethod
    def from_dict(cls, name: str, data_type: str, unit: str, accuracy: str, measurement_range: str, frequency: str, source: str, description: str, id: typing.Optional[int] = None) -> "TVariable":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv meteorološke promenljive.
            data_type: Tip podataka koji se meri (npr. float, integer, string).
            unit: Jedinica merenja (npr. °C, %, m/s).
            accuracy: Tačnost merenja promenljive (npr. ±0.5°C, ±5%).
            measurement_range: Opseg vrednosti koje se mogu meriti.
            frequency: Frekvencija uzorkovanja podataka (npr. svakih 5 minuta,
                svakog sata).
            source: Izvor podataka o promenljivoj (npr. meteorološka stanica,
                senzor).
            description: Detaljan opis meteorološke promenljive.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TVariable":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> VariableDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Variable: typing.Type[TVariable] = models.Variable  # type: ignore


class _SourceDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    code: str
    name: str
    lat: float
    long: float
    type: str
    description: str
    email: str
    phone: str
    installation_date: str


class SourceDict(_SourceDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TSource(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Naziv izvora

    Attrs:
        id: Identifikacioni broj (kluč)
        code: Kod (skraćeni naziv)
        name: Naziv izvora
        lat: Geografska širina
        long: Geografska dužina
        type: Tip mereća (npr. Meteo stanica, Senzor, Satelit)
        description: Opis izvora
        email: Email adresa za kontakt
        phone: Telefonski broj za kontakt
        installation_date: Datum instalacije izvora

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    code: 'sqlalchemy.Column[str]'
    name: 'sqlalchemy.Column[str]'
    lat: 'sqlalchemy.Column[float]'
    long: 'sqlalchemy.Column[float]'
    type: 'sqlalchemy.Column[str]'
    description: 'sqlalchemy.Column[str]'
    email: 'sqlalchemy.Column[str]'
    phone: 'sqlalchemy.Column[str]'
    installation_date: 'sqlalchemy.Column[datetime.date]'

    def __init__(self, code: str, name: str, lat: float, long: float, type: str, description: str, email: str, phone: str, installation_date: datetime.date, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (kluč)
            code: Kod (skraćeni naziv)
            name: Naziv izvora
            lat: Geografska širina
            long: Geografska dužina
            type: Tip mereća (npr. Meteo stanica, Senzor, Satelit)
            description: Opis izvora
            email: Email adresa za kontakt
            phone: Telefonski broj za kontakt
            installation_date: Datum instalacije izvora

        """
        ...

    @classmethod
    def from_dict(cls, code: str, name: str, lat: float, long: float, type: str, description: str, email: str, phone: str, installation_date: datetime.date, id: typing.Optional[int] = None) -> "TSource":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (kluč)
            code: Kod (skraćeni naziv)
            name: Naziv izvora
            lat: Geografska širina
            long: Geografska dužina
            type: Tip mereća (npr. Meteo stanica, Senzor, Satelit)
            description: Opis izvora
            email: Email adresa za kontakt
            phone: Telefonski broj za kontakt
            installation_date: Datum instalacije izvora

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TSource":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> SourceDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Source: typing.Type[TSource] = models.Source  # type: ignore


class _WeatherStationDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str
    location_id: int
    type: str
    capacity: int
    installation_date: str
    last_maintenance_date: str
    status: str
    operator: str


class WeatherStationDict(_WeatherStationDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TWeatherStation(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        id: Identifikacioni broj meteorološke stanice (interni ključ)
        name: Naziv meteorološke stanice
        location_id: Identifikacioni broj lokacije gde se nalazi stanica
        type: Tip meteorološke stanice
        capacity: Kapacitet stanice (broj merenja po jedinici vremena, npr.
            merenja po satu)
        installation_date: Datum instalacije stanice
        last_maintenance_date: Datum poslednjeg održavanja stanice
        status: Status stanice (aktivna, neaktivna, u kvaru)
        operator: Ime organizacije ili osobe koja upravlja stanicom

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    location_id: 'sqlalchemy.Column[int]'
    type: 'sqlalchemy.Column[str]'
    capacity: 'sqlalchemy.Column[int]'
    installation_date: 'sqlalchemy.Column[datetime.date]'
    last_maintenance_date: 'sqlalchemy.Column[datetime.date]'
    status: 'sqlalchemy.Column[str]'
    operator: 'sqlalchemy.Column[str]'

    def __init__(self, name: str, location_id: int, type: str, capacity: int, installation_date: datetime.date, last_maintenance_date: datetime.date, status: str, operator: str, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj meteorološke stanice (interni ključ)
            name: Naziv meteorološke stanice
            location_id: Identifikacioni broj lokacije gde se nalazi stanica
            type: Tip meteorološke stanice
            capacity: Kapacitet stanice (broj merenja po jedinici vremena, npr.
                merenja po satu)
            installation_date: Datum instalacije stanice
            last_maintenance_date: Datum poslednjeg održavanja stanice
            status: Status stanice (aktivna, neaktivna, u kvaru)
            operator: Ime organizacije ili osobe koja upravlja stanicom

        """
        ...

    @classmethod
    def from_dict(cls, name: str, location_id: int, type: str, capacity: int, installation_date: datetime.date, last_maintenance_date: datetime.date, status: str, operator: str, id: typing.Optional[int] = None) -> "TWeatherStation":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj meteorološke stanice (interni ključ)
            name: Naziv meteorološke stanice
            location_id: Identifikacioni broj lokacije gde se nalazi stanica
            type: Tip meteorološke stanice
            capacity: Kapacitet stanice (broj merenja po jedinici vremena, npr.
                merenja po satu)
            installation_date: Datum instalacije stanice
            last_maintenance_date: Datum poslednjeg održavanja stanice
            status: Status stanice (aktivna, neaktivna, u kvaru)
            operator: Ime organizacije ili osobe koja upravlja stanicom

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TWeatherStation":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> WeatherStationDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


WeatherStation: typing.Type[TWeatherStation] = models.WeatherStation  # type: ignore