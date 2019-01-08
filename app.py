from flask import Flask, render_template
app = Flask(__name__)

# teamplate rendering


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/characters")
def characters():
    
    c_list = [
        {
            "name": "captan",
            "image": "https://cdn.vox-cdn.com/thumbor/pXNjzQY4UTqZBX1maWJq3Daozv4=/0x0:2000x1000/1200x800/filters:focal(711x131:1031x451)/cdn.vox-cdn.com/uploads/chorus_image/image/59057741/Thanos_MCU.0.jpg",
            "link": "https://www.google.com/search?q=image+thanos&tbm=isch&source=iu&ictx=1&fir=MXpNHS0sGSRJbM%253A%252CKe1nHHu5sh2GVM%252C_&usg=AI4_-kQA5koOzMq_BoPNkYrf2yav17RAPg&sa=X&ved=2ahUKEwi_9-_J2NbfAhVWUN4KHSMPAlcQ9QEwAHoECAUQBA#imgrc=MXpNHS0sGSRJbM:"
        },
        {
            "name": "Thanos",
            "image": "https://www.sideshowtoy.com/wp-content/uploads/2018/04/marvel-avengers-infinity-war-thanos-sixth-scale-figure-hot-toys-feature-903429-1.jpg",
            "link": "https://www.google.com/search?q=image+thanos&tbm=isch&source=iu&ictx=1&fir=MXpNHS0sGSRJbM%253A%252CKe1nHHu5sh2GVM%252C_&usg=AI4_-kQA5koOzMq_BoPNkYrf2yav17RAPg&sa=X&ved=2ahUKEwi_9-_J2NbfAhVWUN4KHSMPAlcQ9QEwAHoECAUQBA#imgrc=jQDI0E1bHEoVwM:"
        },
        {
            "name": "spider man",
            "image": "https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/5/52/Empire_March_Cover_IW_6_Textless.png/revision/latest?cb=20180325144529",
            "link": "https://www.google.com/search?q=image+thanos&tbm=isch&source=iu&ictx=1&fir=MXpNHS0sGSRJbM%253A%252CKe1nHHu5sh2GVM%252C_&usg=AI4_-kQA5koOzMq_BoPNkYrf2yav17RAPg&sa=X&ved=2ahUKEwi_9-_J2NbfAhVWUN4KHSMPAlcQ9QEwAHoECAUQBA#imgrc=OrPWQAyNU6Sy2M:"
        },
    ]       
    return render_template("characters_list.html",
                           characters_list = c_list)
        
f_items = [
        {
            "name": "Bun cha",
            "image": "http://via.placeholder.com/200x200",
            "link": "http://google.com?q=bun+cha",
            "ytid": "Fhf0ZEZ0edc"
        },
        {
            "name": "Bun ca",
            "image": "https://znews-photo.zadn.vn/w660/Uploaded/rotntt/2014_11_25/bun_ca.jpg",
            "link": "http://google.com?q=bun+ca",
            "ytid": "gQ_DcQVlIO0"
        },
        {
            "name": "Bun dau mam tom",
            "image": "http://via.placeholder.com/200x200",
            "link": "http://google.com?q=bun+dau+mam+tom",
            "ytid": "aifx3izVmHI"
        },
    ]  
@app.route("/names")
def name():
    name_list = ["Huy","Hung","Tuan"]
    return render_template("names.html",
                           name_list = name_list)
@app.route("/food_items")
def food():
    return render_template("food.html",
                           food_items = f_items)
@app.route("/food_detail/<int:index>")
def food_detail(index):
    f_item = f_items[index]
    return render_template("food_detail.html",food_item = f_item)

@app.route("/documents")
def document():
    return render_template("document.html")
    
if __name__ == "__main__":
    app.run(debug=True)
