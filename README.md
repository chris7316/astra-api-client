# astra-api-client

An interface to Astra Schedule's "API" to search events. Built because
heavyweight ASP.NET applications are not fun to use. Tested at the University of
Alabama in Huntsville (although I have no affiliation with them, apart from
being a student there).

## How to use

Using the library is pretty simple:

```py
from astra.client import Client
from astra.filters import Attr

client = Client("http://schedule.myuniversity.edu/Prod")
events = client.get_events(Attr.EventType == "Student Event")
```

`events` is a list of `astra.event.Event` objects, which have attributes like
`name`, `type`, `begin`, `end`, `location`, and `description`. Any of these may
be `None` for any reason, so make sure to check.

## TODO

It'd be nice to have better filters so C# style UpperCamelCase isn't everywhere.
