
from google.cloud import bigquery

PROJECT_ID = "YOUR_PROJECT_ID"
DATASET_ID = "sales_ai"

client = bigquery.Client(project=PROJECT_ID)

tables = {

    "entity_metadata": [
        bigquery.SchemaField("entity_name", "STRING"),
        bigquery.SchemaField("description", "STRING"),
        bigquery.SchemaField("business_domain", "STRING"),
        bigquery.SchemaField("entity_category", "STRING"),
        bigquery.SchemaField("physical_table", "STRING"),
        bigquery.SchemaField("entity_type", "STRING"),
        bigquery.SchemaField("business_owner", "STRING"),
        bigquery.SchemaField("status", "STRING"),
        bigquery.SchemaField("is_active", "BOOL"),
    ],

    "attribute_metadata": [
        bigquery.SchemaField("entity_name", "STRING"),
        bigquery.SchemaField("attribute_name", "STRING"),
        bigquery.SchemaField("description", "STRING"),
        bigquery.SchemaField("data_type", "STRING"),
        bigquery.SchemaField("physical_attribute", "STRING"),
        bigquery.SchemaField("is_primary_key", "BOOL"),
        bigquery.SchemaField("is_nullable", "BOOL"),
        bigquery.SchemaField("is_filterable", "BOOL"),
        bigquery.SchemaField("is_measure", "BOOL"),
        bigquery.SchemaField("is_dimension", "BOOL"),
        bigquery.SchemaField("business_definition", "STRING"),
    ],

    "metric_metadata": [
        bigquery.SchemaField("metric_id", "STRING"),
        bigquery.SchemaField("entity_name", "STRING"),
        bigquery.SchemaField("metric_name", "STRING"),
        bigquery.SchemaField("display_name", "STRING"),
        bigquery.SchemaField("aggregation_type", "STRING"),
        bigquery.SchemaField("source_column", "STRING"),
        bigquery.SchemaField("description", "STRING"),
        bigquery.SchemaField("display_order", "INT64"),
        bigquery.SchemaField("is_active", "BOOL"),
    ],

    "metric_definitions": [
        bigquery.SchemaField("metric_name", "STRING"),
        bigquery.SchemaField("formula", "STRING"),
        bigquery.SchemaField("description", "STRING"),
    ],

    "business_glossary": [
        bigquery.SchemaField("business_term", "STRING"),
        bigquery.SchemaField("business_definition", "STRING"),
        bigquery.SchemaField("business_domain", "STRING"),
    ],

    "value_synonyms": [
        bigquery.SchemaField("entity_name", "STRING"),
        bigquery.SchemaField("attribute_name", "STRING"),
        bigquery.SchemaField("business_value", "STRING"),
        bigquery.SchemaField("technical_value", "STRING"),
    ],

    "entity_relationship_metadata": [
        bigquery.SchemaField("parent_entity", "STRING"),
        bigquery.SchemaField("child_entity", "STRING"),
        bigquery.SchemaField("join_type", "STRING"),
        bigquery.SchemaField("join_condition", "STRING"),
    ],

    "business_relationship_metadata": [
        bigquery.SchemaField("business_relationship", "STRING"),
        bigquery.SchemaField("description", "STRING"),
    ],

    "dim_customer": [
        bigquery.SchemaField("customer_id", "INT64"),
        bigquery.SchemaField("customer_name", "STRING"),
        bigquery.SchemaField("country", "STRING"),
    ],

    "dim_product": [
        bigquery.SchemaField("product_id", "INT64"),
        bigquery.SchemaField("product_name", "STRING"),
        bigquery.SchemaField("category", "STRING"),
    ],

    "dim_date": [
        bigquery.SchemaField("date_id", "INT64"),
        bigquery.SchemaField("date", "DATE"),
        bigquery.SchemaField("year", "INT64"),
        bigquery.SchemaField("month", "INT64"),
        bigquery.SchemaField("quarter", "STRING"),
    ],

    "dim_salesperson": [
        bigquery.SchemaField("salesperson_id", "INT64"),
        bigquery.SchemaField("sales_manager", "STRING"),
        bigquery.SchemaField("sales_rep", "STRING"),
    ],

    "fact_sales": [
        bigquery.SchemaField("order_id", "INT64"),
        bigquery.SchemaField("customer_id", "INT64"),
        bigquery.SchemaField("product_id", "INT64"),
        bigquery.SchemaField("salesperson_id", "INT64"),
        bigquery.SchemaField("date_id", "INT64"),
        bigquery.SchemaField("order_value_eur", "FLOAT64"),
        bigquery.SchemaField("cost", "FLOAT64"),
    ]
}

dataset_ref = f"{PROJECT_ID}.{DATASET_ID}"

for table_name, schema in tables.items():

    table_id = f"{dataset_ref}.{table_name}"

    table = bigquery.Table(table_id, schema=schema)

    try:
        client.create_table(table)
        print(f"Created {table_name}")
    except Exception as ex:
        print(f"{table_name}: {ex}")

print("\nDone.")
