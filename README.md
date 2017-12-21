# LaPosteClient
Python Client to interact with La Poste API: https://developer.laposte.fr

Available operations : 
* TrackShipment (https://api.laposte.fr/suivi/v1/{code})

# Usage
```python
from laposte import LaPoste

def track(code):
  client = new LaPoste('Your-X-Okapi-Key')
  
  return client.trackShipment(code)
```
