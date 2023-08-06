from firefly_iii_client.paths.v1_rules_id.get import ApiForget
from firefly_iii_client.paths.v1_rules_id.put import ApiForput
from firefly_iii_client.paths.v1_rules_id.delete import ApiFordelete


class V1RulesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
