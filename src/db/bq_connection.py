from google.cloud import bigquery

from db.bq_setup import BQSetup
from common.exceptions import (
    DatabaseAlreadyConnectedError,
    DatabaseNotConnectedError
)


class BQConnection:

    def __init__(self):
        self.client = None
        self.setup = BQSetup()

    def connect(self):

        if self.client:
            raise DatabaseAlreadyConnectedError(
                "Database is already connected."
            )

        try:
            self.setup.setup()

            self.client = bigquery.Client(
                project=self.setup.project_id
            )

            return self.client

        except Exception:
            raise

    def disconnect(self):

        self.setup.reset()
        self.client = None

    def execute_query(self, query, params=None):

        if self.client is None:
            raise DatabaseNotConnectedError(
                "Database not connected."
            )

        try:

            job = self.client.query(
                query,
                job_config=None
            )

            return list(job.result())

        except Exception:
            raise

    def execute_single(self, query, params=None):

        rows = self.execute_query(query, params)

        if rows:
            return rows[0]

        return None

    def execute_sql(self, sql: str):

        if self.client is None:
            self.connect()

        job = self.client.query(sql)

        return list(job.result())