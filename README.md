# LaPoste API client

[![Build Status](https://travis-ci.org/GusTTShowbiz/LaPosteClient.svg?branch=master)](https://travis-ci.org/GusTTShowbiz/LaPosteClient)

Python Client to interact with La Poste API: https://developer.laposte.fr

Available operations :
* TrackShipment (https://api.laposte.fr/suivi/v1/{code})

# Usage
```python
from laposte import LaPoste

def track(code):
  client = LaPoste('Your-X-Okapi-Key')

  return client.trackShipment(code)
```
