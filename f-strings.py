x = 99
# check the website. It says witdth and not width.
# print(f"{x} padded to a witdth of three characters is |{x:3}| and padded to a width of five characters is |{x:5}|")
print(f"{x} padded to a width of three characters is |{x:3}| and padded to a width of five characters is |{x:5}|")

x = 22
y = 7
print(f"{x} / {y} in a field of width four, to one decimal place, is |{x/y:4.1f}| and in a field of width eight, to five decimal places, is |{x/y:8.5f}|.")

txt = 'hello'
print(f"Here is the world '{txt}' left-justified in a field of width seven |{txt:<7}| and now right-justified |{txt:>7}| and now centred |{txt:^7}|")