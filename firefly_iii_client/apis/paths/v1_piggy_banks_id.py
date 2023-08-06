from firefly_iii_client.paths.v1_piggy_banks_id.get import ApiForget
from firefly_iii_client.paths.v1_piggy_banks_id.put import ApiForput
from firefly_iii_client.paths.v1_piggy_banks_id.delete import ApiFordelete


class V1PiggyBanksId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
