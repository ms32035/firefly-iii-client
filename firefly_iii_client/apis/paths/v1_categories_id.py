from firefly_iii_client.paths.v1_categories_id.get import ApiForget
from firefly_iii_client.paths.v1_categories_id.put import ApiForput
from firefly_iii_client.paths.v1_categories_id.delete import ApiFordelete


class V1CategoriesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
