from decimal import Decimal

from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Product

product_index = Index('products')
product_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@registry.register_document
class ProductDocument(Document):
    id = fields.IntegerField()
    title = fields.TextField(fields={'raw': fields.KeywordField()})
    description = fields.TextField()
    price = fields.IntegerField()
    category = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(fields={'raw': fields.KeywordField()}),
    })
    user = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'username': fields.TextField(fields={'raw': fields.KeywordField()}),
    })

    class Index:
        name = "products"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }

    class Django:
        model = Product
        fields = ['created_at', 'updated_at']