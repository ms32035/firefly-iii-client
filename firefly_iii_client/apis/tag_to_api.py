import typing_extensions

from firefly_iii_client.apis.tags import TagValues
from firefly_iii_client.apis.tags.about_api import AboutApi
from firefly_iii_client.apis.tags.accounts_api import AccountsApi
from firefly_iii_client.apis.tags.attachments_api import AttachmentsApi
from firefly_iii_client.apis.tags.autocomplete_api import AutocompleteApi
from firefly_iii_client.apis.tags.available_budgets_api import AvailableBudgetsApi
from firefly_iii_client.apis.tags.bills_api import BillsApi
from firefly_iii_client.apis.tags.budgets_api import BudgetsApi
from firefly_iii_client.apis.tags.categories_api import CategoriesApi
from firefly_iii_client.apis.tags.charts_api import ChartsApi
from firefly_iii_client.apis.tags.configuration_api import ConfigurationApi
from firefly_iii_client.apis.tags.currencies_api import CurrenciesApi
from firefly_iii_client.apis.tags.data_api import DataApi
from firefly_iii_client.apis.tags.insight_api import InsightApi
from firefly_iii_client.apis.tags.links_api import LinksApi
from firefly_iii_client.apis.tags.object_groups_api import ObjectGroupsApi
from firefly_iii_client.apis.tags.piggy_banks_api import PiggyBanksApi
from firefly_iii_client.apis.tags.preferences_api import PreferencesApi
from firefly_iii_client.apis.tags.recurrences_api import RecurrencesApi
from firefly_iii_client.apis.tags.rule_groups_api import RuleGroupsApi
from firefly_iii_client.apis.tags.rules_api import RulesApi
from firefly_iii_client.apis.tags.search_api import SearchApi
from firefly_iii_client.apis.tags.summary_api import SummaryApi
from firefly_iii_client.apis.tags.tags_api import TagsApi
from firefly_iii_client.apis.tags.transactions_api import TransactionsApi
from firefly_iii_client.apis.tags.users_api import UsersApi
from firefly_iii_client.apis.tags.webhooks_api import WebhooksApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ABOUT: AboutApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.AUTOCOMPLETE: AutocompleteApi,
        TagValues.AVAILABLE_BUDGETS: AvailableBudgetsApi,
        TagValues.BILLS: BillsApi,
        TagValues.BUDGETS: BudgetsApi,
        TagValues.CATEGORIES: CategoriesApi,
        TagValues.CHARTS: ChartsApi,
        TagValues.CONFIGURATION: ConfigurationApi,
        TagValues.CURRENCIES: CurrenciesApi,
        TagValues.DATA: DataApi,
        TagValues.INSIGHT: InsightApi,
        TagValues.LINKS: LinksApi,
        TagValues.OBJECT_GROUPS: ObjectGroupsApi,
        TagValues.PIGGY_BANKS: PiggyBanksApi,
        TagValues.PREFERENCES: PreferencesApi,
        TagValues.RECURRENCES: RecurrencesApi,
        TagValues.RULE_GROUPS: RuleGroupsApi,
        TagValues.RULES: RulesApi,
        TagValues.SEARCH: SearchApi,
        TagValues.SUMMARY: SummaryApi,
        TagValues.TAGS: TagsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.USERS: UsersApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ABOUT: AboutApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.AUTOCOMPLETE: AutocompleteApi,
        TagValues.AVAILABLE_BUDGETS: AvailableBudgetsApi,
        TagValues.BILLS: BillsApi,
        TagValues.BUDGETS: BudgetsApi,
        TagValues.CATEGORIES: CategoriesApi,
        TagValues.CHARTS: ChartsApi,
        TagValues.CONFIGURATION: ConfigurationApi,
        TagValues.CURRENCIES: CurrenciesApi,
        TagValues.DATA: DataApi,
        TagValues.INSIGHT: InsightApi,
        TagValues.LINKS: LinksApi,
        TagValues.OBJECT_GROUPS: ObjectGroupsApi,
        TagValues.PIGGY_BANKS: PiggyBanksApi,
        TagValues.PREFERENCES: PreferencesApi,
        TagValues.RECURRENCES: RecurrencesApi,
        TagValues.RULE_GROUPS: RuleGroupsApi,
        TagValues.RULES: RulesApi,
        TagValues.SEARCH: SearchApi,
        TagValues.SUMMARY: SummaryApi,
        TagValues.TAGS: TagsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.USERS: UsersApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)
