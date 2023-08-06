from firefly_iii_client.paths.v1_users_id.get import ApiForget
from firefly_iii_client.paths.v1_users_id.put import ApiForput
from firefly_iii_client.paths.v1_users_id.delete import ApiFordelete


class V1UsersId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
