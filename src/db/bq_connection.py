from google.cloud import bigquery

from db.bq_setup import BQSetup


class BQConnection:

    def __init__(self):
        self.client = None
        self.project_id = None

    def connect(self):
        """
        Creates BigQuery client
        """

        setup = BQSetup()
        setup.setup()

        self.project_id = setup.project_id

        self.client = bigquery.Client(
            project=self.project_id
        )

        print("✓ Connected to BigQuery")

        return self.client

    def execute_query(self, sql):

        if self.client is None:
            self.connect()

        query_job = self.client.query(sql)

        return query_job.result()

    def close(self):

        setup = BQSetup()
        setup.reset()

        print("✓ BigQuery session closed")