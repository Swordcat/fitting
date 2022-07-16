from dataclasses import dataclass, make_dataclass
from dataclasses_json import dataclass_json


@dataclass_json()
@dataclass()
class Parameter:
    value: float
    error: float

    def to_text(self, format: str ="") -> str:
        return f'{self.value:{format}} \u00B1 {self.error:{format}}'  # \u00B1 : plus minus symbol


def factory(name: str, attributes:list[str]):
    def _values(self) -> list[float]: return [param['value'] for param in self.to_dict().values()]
    def _errors(self) -> list[float]: return [param['error'] for param in self.to_dict().values()]
    def _parameters(self) -> list[float]: return [key for key in self.to_dict().keys()]

    def _to_text(self, format: str= "") -> str:
        return "\n".join([f'\t{param}: {getattr(self, param).to_text(format)}' for param in self.__annotations__.keys()])
    fields = [(attr, Parameter) for attr in attributes]
    namespace = {"values": _values, "errors": _errors, "parameters": _parameters, "to_text": _to_text}
    return dataclass_json(make_dataclass(name, fields, namespace=namespace))