# generated by datamodel-codegen:
#   filename:  schema/entity/services/databaseService.json
#   timestamp: 2021-11-19T16:01:14+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, constr

from ...type import basic, entityHistory, jdbcConnection, schedule


class DatabaseServiceType(Enum):
    BigQuery = 'BigQuery'
    MySQL = 'MySQL'
    Redshift = 'Redshift'
    Snowflake = 'Snowflake'
    Postgres = 'Postgres'
    MSSQL = 'MSSQL'
    Hive = 'Hive'
    Oracle = 'Oracle'
    Athena = 'Athena'
    Presto = 'Presto'
    Trino = 'Trino'
    Vertica = 'Vertica'
    Glue = 'Glue'
    MariaDB = 'MariaDB'


class DatabaseService(BaseModel):
    id: basic.Uuid = Field(
        ..., description='Unique identifier of this database service instance.'
    )
    name: constr(min_length=1, max_length=64) = Field(
        ..., description='Name that identifies this database service.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this database service.'
    )
    serviceType: DatabaseServiceType = Field(
        ...,
        description='Type of database service such as MySQL, BigQuery, Snowflake, Redshift, Postgres...',
    )
    description: Optional[str] = Field(
        None, description='Description of a database service instance.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.DateTime] = Field(
        None,
        description='Last update time corresponding to the new version of the entity.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: basic.Href = Field(
        ..., description='Link to the resource corresponding to this database service.'
    )
    jdbc: jdbcConnection.JdbcInfo = Field(
        ..., description='JDBC connection information.'
    )
    ingestionSchedule: Optional[schedule.Schedule] = Field(
        None, description='Schedule for running metadata ingestion jobs.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
