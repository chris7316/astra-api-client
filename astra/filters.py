class _Attr:
    def __getattr__(self, name):
        aliases = {
            "name": "EventName",
            "type": "EventType",
            "start": "StartDate",
            "end": "EndDate"
        }

        if name in aliases:
            name = aliases[name]

        return FilterAttr(name)

Attr = _Attr()

class FilterAttr:
    def __init__(self, name):
        self.name = name

    def __lt__(self, other):
        return Triple(self.name, "<", other)

    def __le__(self, other):
        return Triple(self.name, "<=", other)

    def __gt__(self, other):
        return Triple(self.name, ">", other)

    def __ge__(self, other):
        return Triple(self.name, ">=", other)

    def __eq__(self, other):
        return Triple(self.name, "==", other)

    def __pow__(self, other):
        return Triple(self.name, "?=", "%{}%".format(other))

class Expr:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __and__(self, other):
        return AndExpr(self, other)

    def __or__(self, other):
        return OrExpr(self, other)

class AndExpr(Expr):
    def _expr(self):
        return "(" + self.a._expr() + "&&" + self.b._expr() + ")"

class OrExpr(Expr):
    def _expr(self):
        return "(" + self.a._expr() + "||" + self.b._expr() + ")"

class Triple(Expr):
    def __init__(self, key, condition, value):
        self.key = key
        self.condition = condition
        self.value = '"' + value.replace('"', r'\"') + '"'

    def _expr(self):
        return "(" + self.key + self.condition + self.value + ")"

### Standard filters

from datetime import datetime

def today():
    date_str = datetime.now().strftime("%Y-%m-%dT00:00:00")
    return (Attr.StartDate >= date_str) & (Attr.EndDate <= date_str)
