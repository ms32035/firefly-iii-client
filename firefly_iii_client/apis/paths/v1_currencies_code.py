from firefly_iii_client.paths.v1_currencies_code.get import ApiForget
from firefly_iii_client.paths.v1_currencies_code.put import ApiForput
from firefly_iii_client.paths.v1_currencies_code.delete import ApiFordelete


class V1CurrenciesCode(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
