from firefly_iii_client.paths.v1_transaction_links_id.get import ApiForget
from firefly_iii_client.paths.v1_transaction_links_id.put import ApiForput
from firefly_iii_client.paths.v1_transaction_links_id.delete import ApiFordelete


class V1TransactionLinksId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
