from firefly_iii_client.paths.v1_recurrences_id.get import ApiForget
from firefly_iii_client.paths.v1_recurrences_id.put import ApiForput
from firefly_iii_client.paths.v1_recurrences_id.delete import ApiFordelete


class V1RecurrencesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
