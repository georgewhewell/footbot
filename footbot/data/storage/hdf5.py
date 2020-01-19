from pandas import read_hdf

STORE = '{}.h5'

def get_entry_df(
        dataset='fpl',
        table='top_entries_1920',
):
    return read_hdf(STORE.format(dataset), table)

def write_to_table(
        dataset,
        table,
        df,
        write_disposition='WRITE_APPEND',
        secrets_path='./secrets/service_account.json'
):
    df.to_hdf(STORE.format(dataset), table, append=(write_disposition == 'WRITE_APPEND'), format='t')
