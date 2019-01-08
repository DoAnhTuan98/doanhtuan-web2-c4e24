# 1.connect to database
import mlab
from mongoengine import Document,StringField,IntField
mlab.connect()

# 2.define model(document)
class Movie(Document):
  title = StringField()
  image = StringField()
  link = StringField()
  rate = IntField()
# 3.create data
# m = Movie(title="Aquaman",
#           image = "https://vignette.wikia.nocookie.net/marvel_dc/images/9/96/Aquaman_DC_Extended_Universe.jpg/revision/latest?cb=20160403020054",
#           link = "https://www.google.com/search?q=image+aquaman&tbm=isch&source=iu&ictx=1&fir=1L77qzA6y0_VYM%253A%252CyCzeAZccP5y_rM%252C_&usg=AI4_-kSJ7eo71_NSrBBe_O_bD4LApmTfnw&sa=X&ved=2ahUKEwjXlNS19tbfAhVTAogKHQeYB94Q9QEwAHoECAAQBA#imgrc=1L77qzA6y0_VYM:",
#           rate = 7)
# m.save()

movie_list = Movie.objects(rate__gte= 7, title__icontains="Intfinity") # lazy loading 
for m in movie_list:
    
    print(m.title, m.rate)