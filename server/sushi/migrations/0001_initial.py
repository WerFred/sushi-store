from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

categories = [
    {
        'name': 'Baked'
    },
    {
        'name': 'Classic'
    },
    {
        'name': 'Felix'
    },
    {
        'name': 'Sweet'
    },
    {
        'name': 'Maki'
    },
    {
        'name': 'Dragon'
    }
]

sushi_items = [
    {
        'category': 2,
        'image': 'img/philadelphia-salmon.png',
        'name': 'Філадельфія з лососем',
        'quantity': 320,
        'description': ' - лосось, норі, огірок, рис, сир вершковий',
        'price': 265,
        'discount': 0.0,
    },
    {
        'category': 1,
        'image': 'img/baked-salmon.png',
        'name': 'Запечений лосось',
        'quantity': 350,
        'description': '- лосось, норі, рис, сир вершковий, авокадо, ікра, сирна шапочка',
        'price': 265,
        'discount': 0.0,
    },
    {
        'category': 2,
        'image': 'img/philadelphia-acne.png',
        'name': 'Філадельфія з вугрем',
        'quantity': 320,
        'description': ' - норі, огірок, рис, сир вершковий, кунжут, cоус унаги, вугор',
        'price': 335,
        'discount': 0.0,
    },
    {
        'category': 5,
        'image': 'img/maki-salmon.png',
        'name': 'Макі лосось',
        'quantity': 110,
        'description': ' - лосось, норі, рис',
        'price': 105,
        'discount': 0.0,
    },
    {
        'category': 1,
        'image': 'img/baked-acne.png',
        'name': 'Запечений вугор',
        'quantity': 325,
        'description': ' - норі, рис, сир вершковий, кунжут, вугор, авокадо, сирна шапочка',
        'price': 315,
        'discount': 0.0,
    },
    {
        'category': 5,
        'image': 'img/maki-tuna.png',
        'name': 'Макі тунець',
        'quantity': 320,
        'description': ' - норі, рис, тунець',
        'price': 110,
        'discount': 0.0,
    },
    {
        'category': 4,
        'image': 'img/sweet-bounty.png',
        'name': 'Bounty',
        'quantity': 255,
        'description': ' - сир вершковий, банан, кокосова стружка, рисове тісто, кокосовий сироп',
        'price': 160,
        'discount': 0.0,
    },
    {
        'category': 6,
        'image': 'img/dragon-green.png',
        'name': 'Зелений дракон',
        'quantity': 310,
        'description': ' - норі, рис, сир вершковий, cоус унаги, авокадо, креветка, манго, манго-ананасовий соус',
        'price': 290,
        'discount': 0.0,
    },
    {
        'category': 3,
        'image': 'img/felix-salmon.png',
        'name': 'Фелікс лосось',
        'quantity': 330,
        'description': ' - лосось, норі, рис, сир вершковий, авокадо, ікра, салат айсберг, соус шрірача, японський',
        'price': 270,
        'discount': 0.0,
    },
    {
        'category': 4,
        'image': 'img/sweet-oreo.png',
        'name': 'Oreo',
        'quantity': 285,
        'description': ' - сир вершковий, банан, нутелла, орео, рисове тісто, карамельний топінг',
        'price': 180,
        'discount': 0.0,
    },
    {
        'category': 6,
        'image': 'img/dragon-golden.png',
        'name': 'Золотий дракон',
        'quantity': 320,
        'description': ' - норі, рис, cоус унаги, вугор, тунець, авокадо, ікра, японський омлет тамаго',
        'price': 370,
        'discount': 0.0,
    },
    {
        'category': 3,
        'image': 'img/felix-acne.png',
        'name': 'Фелікс вугор',
        'quantity': 295,
        'description': ' - норі, рис, сир вершковий, кунжут, вугор, авокадо, ікра, салат айсберг, соус шрірача, японський',
        'price': 300,
        'discount': 0.0,
    }
]


def load_data(apps, schema_editor):
    Sushi = apps.get_model("sushi", "Sushi")
    Category = apps.get_model("sushi", "Category")
    db_alias = schema_editor.connection.alias

    for category in categories:
        Category.objects.using(db_alias).create(
            category_name=category['name']
        )

    for sushi_item in sushi_items:
        Sushi.objects.using(db_alias).create(
            name=sushi_item['name'],
            description=sushi_item['description'],
            category=Category.objects.get(pk=sushi_item['category']),
            image=sushi_item['image'],
            quantity=sushi_item['quantity'],
            price=sushi_item['price'],
            discount=sushi_item['discount'],
        )


def create_slug(apps, schema_editor):
    Sushi = apps.get_model("sushi", "Sushi")
    for sushi_item in Sushi.objects.all():
        sushi_item.slug = sushi_item.image.url.replace(
            settings.MEDIA_URL + settings.MEDIA_ROOT_PATH, '').split('.')[0]
        sushi_item.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Sushi',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='img/')),
                ('description', models.TextField(default='')),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('price', models.DecimalField(
                    decimal_places=2, default=0.0, max_digits=6)),
                ('discount', models.DecimalField(
                    decimal_places=2, default=0.0, max_digits=3)),
                ('slug', models.SlugField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='category', to='sushi.category')),
            ],
            options={
                'verbose_name_plural': 'Sushi',
            },
        ),
        migrations.RunPython(load_data),
        migrations.RunPython(create_slug)
    ]
