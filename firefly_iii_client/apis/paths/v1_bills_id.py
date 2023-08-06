from firefly_iii_client.paths.v1_bills_id.get import ApiForget
from firefly_iii_client.paths.v1_bills_id.put import ApiForput
from firefly_iii_client.paths.v1_bills_id.delete import ApiFordelete


class V1BillsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
