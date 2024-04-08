# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: 2.0.12
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from firefly_iii_client.models.chart_data_point import ChartDataPoint
from typing import Optional, Set
from typing_extensions import Self

class ChartDataSet(BaseModel):
    """
    ChartDataSet
    """ # noqa: E501
    currency_code: Optional[StrictStr] = None
    currency_decimal_places: Optional[StrictInt] = Field(default=None, description="Number of decimals for the currency associated to the data in the entries.")
    currency_id: Optional[StrictStr] = Field(default=None, description="The currency ID of the currency associated to the data in the entries.")
    currency_symbol: Optional[StrictStr] = None
    end_date: Optional[datetime] = None
    entries: Optional[List[ChartDataPoint]] = Field(default=None, description="The actual entries for this data set. They 'key' value is the label for the data point. The value is the actual (numerical) value.")
    label: Optional[StrictStr] = Field(default=None, description="This is the title of the current set. It can refer to an account, a budget or another object (by name).")
    start_date: Optional[datetime] = None
    type: Optional[StrictStr] = Field(default=None, description="Indicated the type of chart that is expected to be rendered. You can safely ignore this if you want.")
    y_axis_id: Optional[StrictInt] = Field(default=None, description="Used to indicate the Y axis for this data set. Is usually between 0 and 1 (left and right side of the chart).", alias="yAxisID")
    __properties: ClassVar[List[str]] = ["currency_code", "currency_decimal_places", "currency_id", "currency_symbol", "end_date", "entries", "label", "start_date", "type", "yAxisID"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ChartDataSet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in entries (list)
        _items = []
        if self.entries:
            for _item in self.entries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entries'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChartDataSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currency_code": obj.get("currency_code"),
            "currency_decimal_places": obj.get("currency_decimal_places"),
            "currency_id": obj.get("currency_id"),
            "currency_symbol": obj.get("currency_symbol"),
            "end_date": obj.get("end_date"),
            "entries": [ChartDataPoint.from_dict(_item) for _item in obj["entries"]] if obj.get("entries") is not None else None,
            "label": obj.get("label"),
            "start_date": obj.get("start_date"),
            "type": obj.get("type"),
            "yAxisID": obj.get("yAxisID")
        })
        return _obj


