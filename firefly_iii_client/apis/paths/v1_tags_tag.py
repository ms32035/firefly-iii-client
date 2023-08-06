from firefly_iii_client.paths.v1_tags_tag.get import ApiForget
from firefly_iii_client.paths.v1_tags_tag.put import ApiForput
from firefly_iii_client.paths.v1_tags_tag.delete import ApiFordelete


class V1TagsTag(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
