# Emfit Data Reader

Reads heart rate and respiration rate from Emfit QS device.

Uses the html page served by the device on the local network. This code must be run on the same local network as the Emfit QS device to work.

# Usage
```Python
from emfit_data_getter import EmfitDataGetter

data_getter = EmfitDataGetter()

while True:
    print(data_getter.get_heart_rate())
    print(data_getter.get_respiration_rate())
    time.sleep(2)
```
