from firefly_iii_client.paths.v1_budgets_id.get import ApiForget
from firefly_iii_client.paths.v1_budgets_id.put import ApiForput
from firefly_iii_client.paths.v1_budgets_id.delete import ApiFordelete


class V1BudgetsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
