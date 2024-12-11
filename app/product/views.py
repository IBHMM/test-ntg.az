from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from product.models import Product, Brand, BrandWithImage, ParentCategory, Category
from product.serializers import ProductSerializer, BrandSerializer, BrandWithImageSerializer, ParentCategorySerializer, CategorySerializer
from django.db.models import Q


from drf_spectacular.utils import extend_schema, OpenApiParameter
# Create your views here.


class ProductsPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'page_size'
    max_page_size = 100


@extend_schema(
    parameters=[
        OpenApiParameter(name='price_min', type=int,
                         location='query', description='Minimum price filter'),
        OpenApiParameter(name='price_max', type=int,
                         location='query', description='Maximum price filter'),
        OpenApiParameter(name='parent_category', type=str,
                         location='query', description='Parent category filter'),
        OpenApiParameter(name='category', type=str,
                         location='query', description='Category filter'),
        OpenApiParameter(name='subcategory', type=str,
                         location='query', description='Subcategory filter'),
        OpenApiParameter(name='brand', type=str,
                         location='query', description='Brand name filter'),
        OpenApiParameter(name='model', type=str,
                         location='query', description='Model name filter'),
        OpenApiParameter(name='poe_power_output', type=str,
                         location='query', description='PoE power output filter'),
        OpenApiParameter(name='category_id', type=int,
                         location='query', description='Category ID filter'),
        OpenApiParameter(name='parent_category_id', type=int,
                         location='query', description='Parent Category ID filter'),
        OpenApiParameter(name='subcategory_id', type=int,
                         location='query', description='Subcategory ID filter'),
        OpenApiParameter(name='brand_id', type=int,
                         location='query', description='Brand ID filter'),
    ]
)
class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = ProductsPagination

    def get_queryset(self):
        query_params = self.request.query_params

        try:
            queryset = Product.objects.all()
        except:
            queryset = []

        filters = {
            'parent_category__name': query_params.get('parent_category'),
            'category__name': query_params.get('category'),
            'subcategory__name': query_params.get('subcategory'),
            'brand__name': query_params.get('brand'),
            'model': query_params.get('model'),
            'poe_power_output': query_params.get('poe_power_output'),
            'price__gte': query_params.get('price_min'),
            'price__lte': query_params.get('price_max')
        }

        category_id = query_params.get('category_id')
        parent_category_id = query_params.get('parent_category_id')
        subcategory_id = query_params.get('subcategory_id')
        brand_id = query_params.get('brand_id')
        if category_id:
            queryset = queryset.filter(category_id__id=category_id)
        if parent_category_id:
            queryset = queryset.filter(parent_category_id__id=parent_category_id)
        if subcategory_id:
            queryset = queryset.filter(subcategory_id__id=subcategory_id)
        if brand_id:
            queryset = queryset.filter(brand_id__id=brand_id)


        filters = {k: v for k, v in filters.items() if v is not None}

        queryset = queryset.filter(**filters)

        return queryset


class ProductDetailView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Extend the schema to describe query parameters
@extend_schema(
    parameters=[
        OpenApiParameter(name='search_term', type=str,
                         location='query', description='Search term filter'),
        OpenApiParameter(name='page_size', type=int,
                         location='query', description='Number of results per page', required=False),
        OpenApiParameter(name='page', type=int,
                         location='query', description='Page number to retrieve', required=False),
    ]
)
@api_view(['GET', ])
def search_products(request):
    # Retrieve search term from query parameters
    search_term = request.query_params.get('search_term', '')
    page_size = request.query_params.get('page_size', 10)  # Default page size is 10 if not provided
    page = request.query_params.get('page', 1)  # Default to the first page if not provided

    # Ensure the page_size is a valid integer and not less than 1
    try:
        page_size = max(int(page_size), 1)  # Set a minimum of 1 for page size
        page = max(int(page), 1)  # Ensure page number is at least 1
    except ValueError:
        return Response({'detail': 'Invalid page_size or page parameter.'}, status=status.HTTP_400_BAD_REQUEST)

    # If a search term is provided, filter products based on it
    if search_term:
        queryset = Product.objects.filter(
            Q(brand__name__icontains=search_term) | 
            Q(model__icontains=search_term) | 
            Q(parent_category__name__icontains=search_term) | 
            Q(category__name__icontains=search_term)
        )

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = page_size  # Set the page size dynamically
        paginator.page = page  # Set the page number dynamically
        result_page = paginator.paginate_queryset(queryset, request)

        # Serialize the results and return the paginated response
        serializer = ProductSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    else:
        return Response({'detail': 'Please provide a search term.'}, status=status.HTTP_400_BAD_REQUEST)


@ api_view(['GET'])
def get_brands(request):
    brands = Brand.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(brands, request)
    serializer = BrandSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@ extend_schema(request=BrandWithImageSerializer)
@ api_view(['POST'])
def get_brands_with_images(request):
    gender = request.data.get('gender')
    if gender:
        filtered_brands = BrandWithImage.objects.filter(gender=gender)
        serializer = BrandWithImageSerializer(filtered_brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'Gender not provided'}, status=status.HTTP_400_BAD_REQUEST)


@ api_view(['GET'])
def get_parent_categories(request):
    parent_categories = ParentCategory.objects.all()
    serializer = ParentCategorySerializer(parent_categories, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_all_categories(request):
    parent_categories = ParentCategory.objects.all()
    result = {}

    parent_categories_data = ParentCategorySerializer(
        parent_categories, many=True).data

    for parent_categorie in parent_categories_data:
        # brends = Brand.objects.filter(
        #     product__parent_category__in=parent_categories).distinct()
        # brends = BrandSerializer(brends, many=True).data

        result[parent_categorie['name']] = {
            'categories': [category['name'] for category in parent_categorie['categories'] if category['name']],
            # 'brands': [brand['name'] for brand in brends]
        }

    return Response(result, status=status.HTTP_200_OK)
