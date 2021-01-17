import os

train_directory = './train'
train_images = []
test_directory = './test'
test_images = []

for file in os.listdir(train_directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg"):
        train_images.append(filename)

with open("train.txt", "w") as text_file:
    for name in train_images:
        text_file.write('{} {}.rbox\n'.format(name, name))

for file in os.listdir(test_directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg"):
        test_images.append(filename)

with open("test.txt", "w") as text_file:
    for name in test_images:
        text_file.write('{} {}.rbox\n'.format(name, name))
