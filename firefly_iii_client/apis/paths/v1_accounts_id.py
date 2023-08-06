from firefly_iii_client.paths.v1_accounts_id.get import ApiForget
from firefly_iii_client.paths.v1_accounts_id.put import ApiForput
from firefly_iii_client.paths.v1_accounts_id.delete import ApiFordelete


class V1AccountsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
