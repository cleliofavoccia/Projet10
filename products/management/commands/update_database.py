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
                number_of_pages=1
            )
        )

        products_list = cleaner_request.clean(products_list)

        # Products in database to update
        products_to_update_list = Product.objects.all()
        # Index of the product that want to update
        product_index_to_update = 0
        # Categories in database to update
        categories_to_update_list = Category.objects.all()
        # Index of the category that want to update
        category_index_to_update = 0

        # Update products in database with new datas
        for product in products_list:
            # Product in products_to_update_list choose by index
            product_to_update = products_to_update_list[product_index_to_update]

            # Update product with new datas
            product_to_update.name = product['name']
            product_to_update.description = product['description']
            product_to_update.nutriscore = product['nutriscore']
            product_to_update.url = product['url']
            product_to_update.image_url = product['image_url']
            product_to_update.nutrition_image_url = product['image_nutrition_url']

            # Next product to update in next loop
            product_index_to_update += 1

            # Update categories in database with new datas
            for category in product['categories']:
                # Category in categories_to_update_list choose by index
                category_to_update = categories_to_update_list[category_index_to_update]

                # Update category with new datas
                category_to_update.name = category

                # Next category to update in next loop
                category_index_to_update += 1

            self.stdout.write(
                self.style.SUCCESS(
                    '"%s" is successfully updated' % product['name']
                )
            )
