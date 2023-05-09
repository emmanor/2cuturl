from PIL import Image, ImageDraw, ImageFont
import random
import urllib.request

# Set up ad sizes
ad_sizes = [(300, 250), (728, 90), (160, 600), (300, 600), (970, 250)]

# Set up font size
font_size = 50

# Function to generate a random background color
def get_random_color():
    url = 'https://source.unsplash.com/random'
    with urllib.request.urlopen(url) as u:
        f = u.read()
        bg_color = Image.open(BytesIO(f)).convert('RGB')
    return random.choice(bg_color.getdata())

# Loop through ad sizes
for size in ad_sizes:
    # Set up image dimensions and background color
    width, height = size
    bg_color = get_random_color()

    # Create a new image object with the specified dimensions and background color
    img = Image.new('RGB', (width, height), bg_color)

    # Create a draw object for the image
    draw = ImageDraw.Draw(img)

    # Set up text and font
    text = "Sale"
    font = ImageFont.truetype('arial.ttf', font_size)

    # Calculate the text size and position
    text_width, text_height = draw.textsize(text, font)
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Set up text color based on background color for readability
    r, g, b = bg_color
    text_color = (255 - r, 255 - g, 255 - b)

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=text_color)

    # Save the image
    img.save(f'ad_image_{width}x{height}.png')
