import os
from google.cloud import bigquery

def set_up_bigquery(
        secrets_path='./secrets/service_account.json'
):
    '''set up bigquery client'''
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = secrets_path
    return bigquery.Client()


def run_query(
        sql,
        secrets_path='./secrets/service_account.json'
):
    '''run bigquery sql and return dataframe'''
    try:
        client = set_up_bigquery(secrets_path)
        return client.query(sql).to_dataframe()
    except Exception as e:
        print(e)


def write_to_table(
        dataset,
        table,
        df,
        write_disposition='WRITE_APPEND',
        secrets_path='./secrets/service_account.json'
):
    '''write data to bigquery table'''
    try:
        client = set_up_bigquery(secrets_path)

        dataset_ref = client.dataset(dataset)
        table_ref = dataset_ref.table(table)

        job_config = bigquery.LoadJobConfig()
        job_config.autodetect = True
        job_config.write_disposition = write_disposition

        client.load_table_from_dataframe(
            df, table_ref, job_config=job_config
        )

    except Exception as e:
        print(e)

def get_entry_df():
    client = set_up_bigquery()
    sql = 'SELECT * FROM `footbot-001.fpl.top_entries_1920`'
    return client.query(sql).to_dataframe()
