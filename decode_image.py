import base64
import zlib
from PIL import Image

compressed1 = input()
compressed2 = input()
compressed = compressed1 + compressed2
decompressed = base64.b64decode(zlib.decompress(base64.b64decode(compressed)))

with open(f"{compressed[:5]}.png", "wb") as binary_file:

	# Write bytes to file
	binary_file.write(decompressed)

img = Image.open(f"{compressed[:5]}.png")
img = img.resize((img.size[0]*20, img.size[1]*20), Image.Resampling.NEAREST)
img.save(f"{compressed[:5]}_resized.png")