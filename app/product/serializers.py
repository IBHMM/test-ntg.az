from rest_framework import serializers
from product.models import Product, ProductImages, Brand, BrandWithImage, ParentCategory, Category, Subcategory, Filter, FilterValue


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ('id', 'image')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'logo')


class FilterValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterValue
        fields = ('id', 'name')


class FilterSerializer(serializers.ModelSerializer):
    values = FilterValueSerializer(many=True, read_only=True)

    class Meta:
        model = Filter
        fields = ('id', 'name', 'values')


class CategorySerializer(serializers.ModelSerializer):
    filters = FilterSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'description', 'filters')


class ParentCategorySerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = ParentCategory
        fields = ('id', 'name', 'categories', 'image', 'description')


class CustomParentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentCategory
        fields = ('id', 'name', 'image', 'description')


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImagesSerializer(many=True, read_only=True)
    brand = BrandSerializer(read_only=True)
    parent_category = CustomParentCategorySerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    subcategory = SubcategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {key: value for key, value in representation.items() if value is not None and value != []}


class BrandWithImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandWithImage
        fields = ('id', 'name', 'image')
        read_only_fields = ['name', 'image']
