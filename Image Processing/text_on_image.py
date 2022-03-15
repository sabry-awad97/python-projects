from PIL import Image, ImageFont, ImageDraw

# Choose an Image
my_image = Image.open("./images/nature.jpeg")

# Font Selection
title_font = ImageFont.truetype('./fonts/PlayfairDisplay-Regular.ttf', 120)

# Render the Text
title_text = "The Beauty of Nature"
image_editable = ImageDraw.Draw(my_image)
image_editable.text((15, 15), title_text, (237, 230, 211), font=title_font)

# Export the Result
my_image.save("result.jpg")
