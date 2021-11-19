# generated by datamodel-codegen:
#   filename:  schema/operations/workflows/ingestion.json
#   timestamp: 2021-11-19T16:01:14+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, constr

from ...type import basic, entityHistory, entityReference, tagLabel


class IngestionType(Enum):
    bigquery = 'bigquery'
    bigquery_usage = 'bigquery-usage'
    redshift = 'redshift'
    redshift_usage = 'redshift-usage'
    snowflake = 'snowflake'
    snowflake_usage = 'snowflake-usage'
    hive = 'hive'
    mssql = 'mssql'
    mysql = 'mysql'
    postgres = 'postgres'
    trino = 'trino'
    vertica = 'vertica'


class ConnectorConfig(BaseModel):
    username: Optional[str] = Field(
        None, description='username to connect  to the data source.'
    )
    password: Optional[str] = Field(
        None, description='password to connect  to the data source.'
    )
    host: Optional[str] = Field(None, description='Host and port of the data source.')
    database: Optional[str] = Field(None, description='Database of the data source.')
    includeViews: Optional[bool] = Field(
        'true',
        description='optional configuration to turn off fetching metadata for views.',
    )
    enableDataProfiler: Optional[bool] = Field(
        'false',
        description='Run data profiler as part of ingestion to get table profile data.',
    )
    includeFilterPattern: Optional[List[str]] = Field(
        None,
        description='Regex to only fetch tables or databases that matches the pattern.',
    )
    excludeFilterPattern: Optional[List[str]] = Field(
        None, description='Regex exclude tables or databases that matches the pattern.'
    )


class IngestionStatus(BaseModel):
    state: Optional[str] = Field(
        None, description='Workflow status denotes if its failed or succeeded.'
    )
    startDate: Optional[str] = Field(
        None,
        description='startDate of the Ingestion Pipeline run for this particular execution.',
    )
    endDate: Optional[str] = Field(
        None,
        description='endDate of the Ingestion pipeline run for this particular execution.',
    )


class Ingestion(BaseModel):
    id: Optional[basic.Uuid] = Field(
        None, description='Unique identifier that identifies this Ingestion.'
    )
    name: constr(min_length=1, max_length=256) = Field(
        ..., description='Name that identifies this ingestion instance uniquely.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this Ingestion.'
    )
    description: Optional[str] = Field(None, description='Description of the workflow.')
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this Ingestion.'
    )
    fullyQualifiedName: Optional[constr(min_length=1, max_length=128)] = Field(
        None, description='Name that uniquely identifies a Ingestion.'
    )
    ingestionType: Optional[IngestionType] = None
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags associated with the Ingestion.'
    )
    forceDeploy: Optional[bool] = Field(
        'false',
        description='Deploy the workflow by overwriting existing workflow with the same name.',
    )
    pauseWorkflow: Optional[bool] = Field(
        'false',
        description='pause the workflow from running once the deploy is finished successfully.',
    )
    concurrency: Optional[int] = Field(1, description='Concurrency of the Pipeline.')
    startDate: basic.Date = Field(..., description='Start date of the workflow.')
    endDate: Optional[basic.Date] = Field(None, description='End Date of the workflow.')
    nextExecutionDate: Optional[basic.Date] = Field(
        None,
        description='Next execution date from the underlying workflow platform once the ingestion scheduled.',
    )
    workflowTimezone: Optional[str] = Field(
        'UTC', description='Timezone in which workflow going to be scheduled.'
    )
    retries: Optional[int] = Field(1, description='Retry workflow in case of failure.')
    retryDelay: Optional[int] = Field(
        300, description='Delay between retries in seconds.'
    )
    workflowCatchup: Optional[bool] = Field(
        'false', description='Run past executions if the start date is in the past.'
    )
    scheduleInterval: Optional[str] = Field(
        None, description='Scheduler Interval for the Workflow in cron format.'
    )
    workflowTimeout: Optional[int] = Field(
        60, description='Timeout for the workflow in seconds.'
    )
    connectorConfig: ConnectorConfig
    ingestionStatuses: Optional[List[IngestionStatus]] = Field(
        None, description='List of executions and status for the Ingestion Pipeline.'
    )
    service: entityReference.EntityReference = Field(
        ...,
        description='Link to the database service where this database is hosted in.',
    )
    href: Optional[basic.Href] = Field(
        None, description='Link to this ingestion resource.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.DateTime] = Field(
        None,
        description='Last update time corresponding to the new version of the entity.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that led to this version of the entity.'
    )
