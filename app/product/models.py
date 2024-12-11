from django.db import models

from datetime import timedelta
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Brand(BaseModel):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brand_logos', blank=True, null=True)

    def __str__(self):
        return self.name


class BrandWithImage(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='brand_images')

    def __str__(self):
        return f'{self.name}'


class ParentCategory(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='parent_category_images')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    parent_category = models.ManyToManyField(
        ParentCategory, related_name='categories')
    image = models.ImageField(upload_to='category_images')
    description = models.TextField(blank=True, null=True)
    filters = models.ManyToManyField('Filter')

    def __str__(self):
        return self.name


class Subcategory(BaseModel):
    name = models.CharField(models.Model)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'Category: {self.category}, subcategory: {self.name}'


class Filter(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class FilterValue(BaseModel):
    name = models.CharField(max_length=255)
    filter = models.ForeignKey(
        Filter, on_delete=models.CASCADE, related_name='values')

    def __str__(self):
        return f'{self.filter.name}-{self.name}'


from django.db import models
from django.contrib.postgres.fields import ArrayField

class Product(BaseModel):
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, blank=True, null=True)  
    model = ArrayField(models.CharField(max_length=255), blank=True, null=True)  
    link = models.URLField(blank=True, null=True)  
    description = models.TextField(blank=True, null=True)  
    poe_power_output = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)  
    power_consumption = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    poe_power_budget = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    poe_extend_mode = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    port = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    poe_injector_port = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    sfp_mini_gbic_slots = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    dimensions = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    weight = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    operating_temperature = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    operating_humidity = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    accessories = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    operation_mode = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    power_requirement = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    max_power_consumption = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    interface = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    frequency_band = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    package = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    pixel = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    ir_distance = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    power = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    processor = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    ram = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    graphics_card = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    ssd = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    hdd = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    gpu = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    display = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    color = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    camera = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    sound = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    operating_system = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    compatibility = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    resource = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    monitor = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    raid = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Memory_Type = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    dimm_capacity = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Processor_catch = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Processor_core_aviable = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Processor_number = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Data_rate = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Network_Interface = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Video_Input = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Video_Output = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    usb_Interface = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    sata_Interface = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Exit_Button = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Fire_Alarm_input = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Throughput = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    wan = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    lan = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Console = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Fax_ower_IP = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    System_Capacity = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Access_Mode = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Connectors = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Power_Requirements = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Power_Supply = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    usb_port = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    usp_type_c = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    htmi = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    vga = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Display_Port = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Network = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Wireless = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Webcam = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Fingerprint = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Function = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Connection = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    os_Support = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Print_Speed = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Scan_Feature = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Replacement_cartridges = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Page_yields = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Compatiable_Printers = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Transmission_Distance = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Connector_Type = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Fiber_Type = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Wavelenght = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Voltage = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Input_Voltage_Range = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Battery = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Frequency = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Output_Voltage = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Battery_Charging_Time = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Capacity = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    Print_Technology = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    parent_category = models.ForeignKey(
        ParentCategory, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.brand.name}-{self.model}'


class ProductImages(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images', null=True, blank=True)

    # def __str__(self):
    #     return self.product.model
