"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.5.6
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from firefly_iii_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from firefly_iii_client.exceptions import ApiAttributeError



class RuleTriggerKeyword(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'FROM_ACCOUNT_STARTS': "from_account_starts",
            'FROM_ACCOUNT_ENDS': "from_account_ends",
            'FROM_ACCOUNT_IS': "from_account_is",
            'FROM_ACCOUNT_CONTAINS': "from_account_contains",
            'TO_ACCOUNT_STARTS': "to_account_starts",
            'TO_ACCOUNT_ENDS': "to_account_ends",
            'TO_ACCOUNT_IS': "to_account_is",
            'TO_ACCOUNT_CONTAINS': "to_account_contains",
            'AMOUNT_LESS': "amount_less",
            'AMOUNT_EXACTLY': "amount_exactly",
            'AMOUNT_MORE': "amount_more",
            'DESCRIPTION_STARTS': "description_starts",
            'DESCRIPTION_ENDS': "description_ends",
            'DESCRIPTION_CONTAINS': "description_contains",
            'DESCRIPTION_IS': "description_is",
            'TRANSACTION_TYPE': "transaction_type",
            'CATEGORY_IS': "category_is",
            'BUDGET_IS': "budget_is",
            'TAG_IS': "tag_is",
            'CURRENCY_IS': "currency_is",
            'HAS_ATTACHMENTS': "has_attachments",
            'HAS_NO_CATEGORY': "has_no_category",
            'HAS_ANY_CATEGORY': "has_any_category",
            'HAS_NO_BUDGET': "has_no_budget",
            'HAS_ANY_BUDGET': "has_any_budget",
            'HAS_NO_TAG': "has_no_tag",
            'HAS_ANY_TAG': "has_any_tag",
            'NOTES_CONTAIN': "notes_contain",
            'NOTES_START': "notes_start",
            'NOTES_END': "notes_end",
            'NOTES_ARE': "notes_are",
            'NO_NOTES': "no_notes",
            'ANY_NOTES': "any_notes",
            'SOURCE_ACCOUNT_IS': "source_account_is",
            'DESTINATION_ACCOUNT_IS': "destination_account_is",
            'SOURCE_ACCOUNT_STARTS': "source_account_starts",
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """RuleTriggerKeyword - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): The type of thing this trigger responds to. A limited set is possible., must be one of ["from_account_starts", "from_account_ends", "from_account_is", "from_account_contains", "to_account_starts", "to_account_ends", "to_account_is", "to_account_contains", "amount_less", "amount_exactly", "amount_more", "description_starts", "description_ends", "description_contains", "description_is", "transaction_type", "category_is", "budget_is", "tag_is", "currency_is", "has_attachments", "has_no_category", "has_any_category", "has_no_budget", "has_any_budget", "has_no_tag", "has_any_tag", "notes_contain", "notes_start", "notes_end", "notes_are", "no_notes", "any_notes", "source_account_is", "destination_account_is", "source_account_starts", ]  # noqa: E501

        Keyword Args:
            value (str): The type of thing this trigger responds to. A limited set is possible., must be one of ["from_account_starts", "from_account_ends", "from_account_is", "from_account_contains", "to_account_starts", "to_account_ends", "to_account_is", "to_account_contains", "amount_less", "amount_exactly", "amount_more", "description_starts", "description_ends", "description_contains", "description_is", "transaction_type", "category_is", "budget_is", "tag_is", "currency_is", "has_attachments", "has_no_category", "has_any_category", "has_no_budget", "has_any_budget", "has_no_tag", "has_any_tag", "notes_contain", "notes_start", "notes_end", "notes_are", "no_notes", "any_notes", "source_account_is", "destination_account_is", "source_account_starts", ]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """RuleTriggerKeyword - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): The type of thing this trigger responds to. A limited set is possible., must be one of ["from_account_starts", "from_account_ends", "from_account_is", "from_account_contains", "to_account_starts", "to_account_ends", "to_account_is", "to_account_contains", "amount_less", "amount_exactly", "amount_more", "description_starts", "description_ends", "description_contains", "description_is", "transaction_type", "category_is", "budget_is", "tag_is", "currency_is", "has_attachments", "has_no_category", "has_any_category", "has_no_budget", "has_any_budget", "has_no_tag", "has_any_tag", "notes_contain", "notes_start", "notes_end", "notes_are", "no_notes", "any_notes", "source_account_is", "destination_account_is", "source_account_starts", ]  # noqa: E501

        Keyword Args:
            value (str): The type of thing this trigger responds to. A limited set is possible., must be one of ["from_account_starts", "from_account_ends", "from_account_is", "from_account_contains", "to_account_starts", "to_account_ends", "to_account_is", "to_account_contains", "amount_less", "amount_exactly", "amount_more", "description_starts", "description_ends", "description_contains", "description_is", "transaction_type", "category_is", "budget_is", "tag_is", "currency_is", "has_attachments", "has_no_category", "has_any_category", "has_no_budget", "has_any_budget", "has_no_tag", "has_any_tag", "notes_contain", "notes_start", "notes_end", "notes_are", "no_notes", "any_notes", "source_account_is", "destination_account_is", "source_account_starts", ]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self