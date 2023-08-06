from firefly_iii_client.paths.v1_object_groups_id.get import ApiForget
from firefly_iii_client.paths.v1_object_groups_id.put import ApiForput
from firefly_iii_client.paths.v1_object_groups_id.delete import ApiFordelete


class V1ObjectGroupsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
