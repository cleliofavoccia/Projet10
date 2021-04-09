"""Command to fill the Django database create
by models with Open Food Facts datas"""

from django.core.management.base import BaseCommand
from products.models import Product, Category
from products.requests_to_OFF import apiclient, cleaner


class Command(BaseCommand):
    """Attributes and method useful for fill
    the database with Open Food Facts datas"""

    def handle(self, *args, **kwargs):
        """Fetch bests products on OFF"""
        off_request = apiclient.OpenfoodfactsClient()
        cleaner_request = cleaner.Cleaner()

        products_list = (
            off_request
            .get_products_by_popularity(
                page_size=1000,
                number_of_pages=3
            )
        )

        products_list = cleaner_request.clean(products_list)

        # Update products in database with new datas
        for product in products_list:
            # Product in products_to_update_list choose by index
            try:
                product_to_update = Product.objects.get(url=product['url'])

                # Update product with new datas
                product_to_update.name = product.get('product', product_to_update.name)
                product_to_update.description = product.get('description', product_to_update.description)
                product_to_update.nutriscore = product.get('nutriscore', product_to_update.nutriscore)
                product_to_update.url = product.get('url', product_to_update.url)
                product_to_update.image_url = product.get('image_url', product_to_update.image_url)
                product_to_update.nutrition_image_url = product.get('image_nutrition_url',
                                                                    product_to_update.image_nutrition_url)

                product_to_update.categories.clear()
                for category in product['categories']:
                    category, created = Category.objects.get_or_create(name=category)
                    product_to_update.categories.add(category)

                product_to_update.save()
            except Product.DoesNotExist:
                continue

            self.stdout.write(
                self.style.SUCCESS(
                    '"%s" is successfully updated' % product['name']
                )
            )
