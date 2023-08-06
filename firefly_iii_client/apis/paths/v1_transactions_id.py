from firefly_iii_client.paths.v1_transactions_id.get import ApiForget
from firefly_iii_client.paths.v1_transactions_id.put import ApiForput
from firefly_iii_client.paths.v1_transactions_id.delete import ApiFordelete


class V1TransactionsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
