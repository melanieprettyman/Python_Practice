from PIL import Image, ImageFilter

# Open an image and examine the images qualities
img = Image.open('./Pokedex/bulbasaur.jpg')
print(img.size)

# Add filters to an image
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blue_img.png', 'png')
filtered_img.show()
# rotate image
filtered_img.rotate(90).save('rotate_img.png', 'png')
# Resize image
filtered_img.resize((300,300)).save('resized_img.png', 'png')


# Astro.jpg is 10MB (huge), we want to shrink it while still maintaining it's aspect ration
huge_image = Image.open('./astro.jpg')
huge_image.thumbnail((400,400))
huge_image.save('thumbnail.png', 'png')