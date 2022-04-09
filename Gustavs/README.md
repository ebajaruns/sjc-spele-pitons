# Bildites scalošanas lieta ja kādam vajaga
```
from PIL import Image, ImageTk

def imagess(path, ImageSizeModifier):
    tempp = Image.open(path)
    tempp = tempp.resize((tempp.size[0] // ImageSizeModifier, tempp.size[1] // ImageSizeModifier))
    return ImageTk.PhotoImage(tempp)

bildite = imagess('path', 0.1)
# piemers
# bildite = imagess('Gustavs/assets/sss.png', 0.1)
```