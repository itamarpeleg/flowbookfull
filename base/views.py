from django.shortcuts import render
from .models import Choice

def home(request):
    return render(request, 'base/home.html')



flowers = [
    {'id': 1, 'id_n': 2, 'f1': 'https://www.shutterbug.com/images/photo_post/[uid]/N9010100_mod4.jpg', 'f1_color': 'yellow', 'f2': 'https://cdn6.bigcommerce.com/s-oqm1pc/images/stencil/1280x1280/products/1270/939/aptenia-cordifolia-variegata-crystal__29727.1406313636.jpg?c=2', 'f2_color': 'red'},
    {'id': 2, 'id_n': 3, 'f1': 'https://plants.com.pk/wp-content/uploads/2020/05/Abutilon-Chittendenii-Indian-Mallow.jpg', 'f1_color': 'yellow', 'f2': 'https://img.crocdn.co.uk/images/products2/pr/20/00/03/54/pr2000035454_card4_lg.jpg', 'f2_color': 'blue'},
    {'id': 3, 'id_n': 4, 'f1': 'https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/yellow-hibiscus-of-maui-daniel-baralt.jpg', 'f1_color': 'yellow', 'f2': 'https://www.gardenexpress.com.au/wp-content/uploads/2015/02/crinum-lily-pink-pkcripin.jpg', 'f2_color': 'pink'},
    {'id': 4, 'id_n': 5, 'f1': 'https://www.enature.qa/wp-content/uploads/2015/08/image-flora-aaronsohnia-factorovskyi.jpg', 'f1_color': 'yellow', 'f2': 'https://www.mantur-flower.co.il/upload/3_1484565669.jpg', 'f2_color': 'red'},
    {'id': 5, 'id_n': 6, 'f1': 'https://quelle-est-cette-fleur.com/img/especes/hd/urosperme-faux-picris-1.jpg', 'f1_color': 'yellow', 'f2': 'https://a6adc47bb216dfe8a383-49bf67815854ec9e2c04a8f4abb9cbf5.ssl.cf3.rackcdn.com/images/products2/pl/00/00/00/27/pl0000002730_card3_lg.jpg', 'f2_color': 'blue'},
    {'id': 6, 'id_n': 7, 'f1': 'https://img.plantsam.com/wp-content/uploads/2016/05/Iris-pseudacorus-4.jpg', 'f1_color': 'yellow', 'f2': 'https://cdn.notonthehighstreet.com/system/product_images/images/001/929/087/original_plant-gift-scented-lilac-plant.jpg', 'f2_color': 'pink'},
    {'id': 7, 'id_n': 8, 'f1': 'http://www.flowersinisrael.com/Flowgallery/Adonis_dentata_thumb.jpg', 'f1_color': 'yellow', 'f2': 'https://www.gan-yarak.co.il/wp-content/uploads/2019/09/2004Orange_2A-570x570.jpg', 'f2_color': 'red'},
    {'id': 8, 'id_n': 9, 'f1': 'https://i1.treknature.com/photos/14253/broomrape.jpg', 'f1_color': 'yellow', 'f2': 'https://cactusjungle.com/wp-content/uploads/2013/03/Iris-PCH1.jpg', 'f2_color': 'blue'},
    {'id': 9, 'id_n': 10, 'f1': 'https://www.glissandogardencenter.ro/wp-content/uploads/2018/12/NUPHAR-0.jpg', 'f1_color': 'yellow', 'f2': 'https://cdn.notonthehighstreet.com/system/product_images/images/001/929/087/original_plant-gift-scented-lilac-plant.jpg', 'f2_color': 'pink'},
    {'id': 10, 'id_n': 11, 'f1': 'https://2obrvy1w2pxe17pte628gss5-wpengine.netdna-ssl.com/wp-content/uploads/HERBS-084.jpg', 'f1_color': 'yellow', 'f2': 'https://upload.wikimedia.org/wikipedia/commons/9/94/Calendula_G.JPG', 'f2_color': 'red'},
    {'id': 11, 'id_n': 12, 'f1': 'https://img.crocdn.co.uk/images/products2/pl/20/00/01/78/pl2000017897.jpg?width=940&height=940', 'f1_color': 'red', 'f2': 'https://4.bp.blogspot.com/-jtXR5ovQ6_A/V1SXfSZIKpI/AAAAAAAAqhw/9SOkFYx4B88fMmPTlXvvYx70gU2JYvYPgCKgB/s1600/DSC06820a.jpg', 'f2_color': 'blue'},
    {'id': 12, 'id_n': 13, 'f1': 'https://img.crocdn.co.uk/images/products2/pl/20/00/01/61/pl2000016106.jpg?width=940&height=940', 'f1_color': 'red', 'f2': 'https://greenseedgarden.com/wp-content/uploads/2018/09/Hyacinth-16.jpg', 'f2_color': 'pink'},
    {'id': 13, 'id_n': 14, 'f1': 'https://www.simpleleaffarm.com/wp-content/uploads/2020/08/SLF-Zinnia-Queen-Lime-Orange-5627-scaled.jpg', 'f1_color': 'red', 'f2': 'https://www.klostra.se/media/catalog/product/s/c/scabiosa_oxford_blue.jpg', 'f2_color': 'blue'},
    {'id': 14, 'id_n': 15, 'f1': 'https://h2.commercev3.net/cdn.brecks.com/images/500/06737.jpg', 'f1_color': 'red', 'f2': 'https://www.bartonarboretum.org/arblog/wp-content/uploads/2016/06/IMG_2707.jpg', 'f2_color': 'pink'},
    {'id': 15, 'id_n': 16, 'f1': 'https://order.eurobulb.nl/1108-large_default/tulipa-couleur-cardinal-6301.jpg', 'f1_color': 'red', 'f2': 'https://www.klostra.se/media/catalog/product/s/c/scabiosa_oxford_blue.jpg', 'f2_color': 'blue'},
    {'id': 16, 'id_n': 17, 'f1': 'https://i.etsystatic.com/23212321/r/il/667aee/2401250447/il_794xN.2401250447_njta.jpg', 'f1_color': 'red', 'f2': 'https://i5.walmartimages.com/asr/16717c8a-5bf5-403b-8e12-c6d4a39bccd9_1.d293201d47e5ccd5a948df566b6bcd27.jpeg', 'f2_color': 'pink'},
    {'id': 17, 'id_n': 18, 'f1': 'https://img.crocdn.co.uk/images/products2/pl/20/00/01/24/pl2000012403.jpg?width=940&height=940', 'f1_color': 'blue', 'f2': 'https://www.daveli.it/garden/wp-content/uploads/2020/01/camelia_daveli1.jpg', 'f2_color': 'pink'},
    {'id': 18, 'id_n': 19, 'f1': 'https://i.pinimg.com/originals/13/90/54/1390549d4d29d13748289008720e6b9f.jpg', 'f1_color': 'blue', 'f2': 'https://hollybethorganics.com/wp-content/uploads/2017/06/yarrow-1024x1024.jpg', 'f2_color': 'pink'},
    {'id': 19, 'id_n': 20, 'f1': 'https://www.photos-public-domain.com/wp-content/uploads/2012/04/grape-hyacinth.jpg', 'f1_color': 'blue', 'f2': 'https://www.maysgardenseed.com/wp-content/uploads/2020/10/75.-Mixed-Petunia-Seeds-Veined-Mix-3.jpg', 'f2_color': 'pink'},
    {'id': 20, 'id_n': 21, 'f1': 'https://www.rhododendrons.co.uk/images/products/large/1958.jpg?iconography=iconography', 'f1_color': 'pink', 'f2': 'https://i.pinimg.com/originals/50/cb/25/50cb2549d499efae883f311024f210d6.jpg', 'f2_color': 'blue'},
]

def one(request, pk):

    if request.method == 'POST':
        color = request.POST["send1"]
        choice = Choice(color_choice=color, age="one")
        choice.save()

    one = None
    for i in flowers:
        if (i['id'] == int(pk) and int(pk) != 21):
            one = i
        elif int(pk) == 21:
            return render(request, 'base/oneend.html')

    context = {'one': one}


    return render(request, 'base/one.html', context)


def two(request, pk):

    if request.method == 'POST':
        color = request.POST["send2"]
        choice = Choice(color_choice=color, age="two")
        choice.save()

    two = None
    for i in flowers:
        if (i['id'] == int(pk) and int(pk) != 21):
            two = i
        elif int(pk) == 21:
            return render(request, 'base/oneend.html')

    context = {'two': two}


    return render(request, 'base/two.html', context)

def three(request, pk):

    if request.method == 'POST':
        color = request.POST["send3"]
        choice = Choice(color_choice=color, age="three")
        choice.save()

    three = None
    for i in flowers:
        if (i['id'] == int(pk) and int(pk) != 21):
            three = i
        elif int(pk) == 21:
            return render(request, 'base/oneend.html')

    context = {'three': three}


    return render(request, 'base/three.html', context)