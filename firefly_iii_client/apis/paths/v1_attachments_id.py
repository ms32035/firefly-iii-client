from firefly_iii_client.paths.v1_attachments_id.get import ApiForget
from firefly_iii_client.paths.v1_attachments_id.put import ApiForput
from firefly_iii_client.paths.v1_attachments_id.delete import ApiFordelete


class V1AttachmentsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
