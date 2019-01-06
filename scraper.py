import requests
from bs4 import BeautifulSoup


villagers = [
    'George.png',
    'Gus.png',
    'Jas.png',
    'Jodi.png',
    'Kent.png',
    'Krobus.png',
    'Lewis.png',
    'Linus.png',
    'Marnie.png',
    'Pam.png',
    'Pierre.png',
    'Robin.png',
    'Sandy.png',
    'Vincent.png',
    'Willy.png',
    'Wizard.png',
    'Bouncer.png',
    'Gil.png',
    'Governor.png',
    'Grandpa.png',
    'Gunther.png',
    'Henchman_Portrait_1.png',
    'Marlon.png',
    'Morris.png',
    'Mr._Qi.png',
]

crops = [
    'https://stardewvalleywiki.com/mediawiki/images/2/2f/Blue_Jazz.png',
    'https://stardewvalleywiki.com/mediawiki/images/a/aa/Cauliflower.png',
    'https://stardewvalleywiki.com/mediawiki/images/3/33/Coffee_Bean.png',
    'https://stardewvalleywiki.com/mediawiki/images/c/cc/Garlic.png',
    'https://stardewvalleywiki.com/mediawiki/images/5/5c/Green_Bean.png',
    'https://stardewvalleywiki.com/mediawiki/images/d/d1/Kale.png',
    'https://stardewvalleywiki.com/mediawiki/images/d/db/Parsnip.png',
    'https://stardewvalleywiki.com/mediawiki/images/c/c2/Potato.png',
    'https://stardewvalleywiki.com/mediawiki/images/6/6e/Rhubarb.png',
    'https://stardewvalleywiki.com/mediawiki/images/6/6d/Strawberry.png',
    'https://stardewvalleywiki.com/mediawiki/images/c/cf/Tulip.png',
    'https://stardewvalleywiki.com/mediawiki/images/9/9e/Blueberry.png',
    'https://stardewvalleywiki.com/mediawiki/images/f/f8/Corn.png',
    'https://stardewvalleywiki.com/mediawiki/images/5/59/Hops.png',
    'https://stardewvalleywiki.com/mediawiki/images/f/f1/Hot_Pepper.png',
    'https://stardewvalleywiki.com/mediawiki/images/1/19/Melon.png',
    'https://stardewvalleywiki.com/mediawiki/images/3/37/Poppy.png',
    'https://stardewvalleywiki.com/mediawiki/images/d/d5/Radish.png',
    'https://stardewvalleywiki.com/mediawiki/images/2/2d/Red_Cabbage.png',
    'https://stardewvalleywiki.com/mediawiki/images/d/db/Starfruit.png',
    'https://stardewvalleywiki.com/mediawiki/images/9/9f/Summer_Spangle.png',
    'https://stardewvalleywiki.com/mediawiki/images/8/81/Sunflower.png',
    'https://stardewvalleywiki.com/mediawiki/images/9/9d/Tomato.png',
    'https://stardewvalleywiki.com/mediawiki/images/e/e2/Wheat.png',
    'https://stardewvalleywiki.com/mediawiki/images/f/f6/Amaranth.png',
    'https://stardewvalleywiki.com/mediawiki/images/d/dd/Artichoke.png',
    'https://stardewvalleywiki.com/mediawiki/images/a/a4/Beet.png',
    'https://stardewvalleywiki.com/mediawiki/images/4/40/Bok_Choy.png',
    'https://stardewvalleywiki.com/mediawiki/images/6/6e/Cranberries.png',
    'https://stardewvalleywiki.com/mediawiki/images/8/8f/Eggplant.png',
    'https://stardewvalleywiki.com/mediawiki/images/5/5c/Fairy_Rose.png',
    'https://stardewvalleywiki.com/mediawiki/images/c/c2/Grape.png',
    'https://stardewvalleywiki.com/mediawiki/images/6/64/Pumpkin.png',
    'https://stardewvalleywiki.com/mediawiki/images/5/52/Yam.png',
    'https://stardewvalleywiki.com/mediawiki/images/0/01/Ancient_Fruit.png',
    'https://stardewvalleywiki.com/mediawiki/images/3/32/Cactus_Fruit.png',
    'https://stardewvalleywiki.com/mediawiki/images/2/2e/Mixed_Seeds.png',
    'https://stardewvalleywiki.com/mediawiki/images/8/88/Sweet_Gem_Berry.png',
    'https://stardewvalleywiki.com/mediawiki/images/thumb/3/39/Spring_Seeds.png/36px-Spring_Seeds.png',
    'https://stardewvalleywiki.com/mediawiki/images/thumb/c/c4/Summer_Seeds.png/36px-Summer_Seeds.png',
    'https://stardewvalleywiki.com/mediawiki/images/thumb/5/55/Fall_Seeds.png/36px-Fall_Seeds.png',
    'https://stardewvalleywiki.com/mediawiki/images/thumb/d/dd/Winter_Seeds.png/36px-Winter_Seeds.png',
]


def main():
    base_url = 'https://stardewvalleywiki.com/'
    response = requests.get(base_url + 'Villagers')
    # soup = BeautifulSoup(response.content)
    # imgs = soup.find_all('img')
    # srcs = list(x['src'] for x in imgs)
    for crop in crops:
        name = crop.split('/')[-1]
        with open('stardew_valley/static/media/items/crops/' + name, 'wb') as f:
            # link = ''.join(x for x in srcs if x.endswith(villager))
            f.write(requests.get(crop).content)


if __name__ == "__main__":
    main()
