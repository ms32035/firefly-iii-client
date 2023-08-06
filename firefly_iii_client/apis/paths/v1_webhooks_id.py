from firefly_iii_client.paths.v1_webhooks_id.get import ApiForget
from firefly_iii_client.paths.v1_webhooks_id.put import ApiForput
from firefly_iii_client.paths.v1_webhooks_id.delete import ApiFordelete


class V1WebhooksId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
