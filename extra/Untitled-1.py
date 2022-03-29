# from pywhatkit import image_to_ascii_art as tk

# img = "r3.png"
# text= "text"
n="{"
m="}"

# tk(img,text)
for i in range(25):
    a=f"""    function kkr{i}(){n}
        var kkr{i} = document.getElementById("kkr{i}");
        document.getElementById("kkr{i}").innerHTML += "<div class=\\"row row-cols-2 mt-2\\"><div class=\\"col-3\\"><input type=\\"checkbox\\" name=\\"c{i}\\" value=\\"\\" id=\\"c{i}\\" style=\\"height: 50px; width: 50px;\\"></div><div class=\\"col\\"><p style=\\"font-size: 25px;\\"></p></div></div>";
    {m}"""

    print(a)