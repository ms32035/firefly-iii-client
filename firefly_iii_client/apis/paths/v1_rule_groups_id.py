from firefly_iii_client.paths.v1_rule_groups_id.get import ApiForget
from firefly_iii_client.paths.v1_rule_groups_id.put import ApiForput
from firefly_iii_client.paths.v1_rule_groups_id.delete import ApiFordelete


class V1RuleGroupsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
