from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from product.models import Product


class CustomArrayWidget(forms.Textarea):
    def format_value(self, value):
        if (not value):
            return ''
        value = value.split(",")
        return '\n'.join(value)

    def value_from_datadict(self, data, files, name):
        raw_value = data.get(name)
        if raw_value:
            return [item.strip() for item in raw_value.split('\n') if item.strip()]
        return []


class ProductModelAdminForm(forms.ModelForm):
    poe_power_output = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    max_power_consumption = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    poe_power_budget = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    port = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    poe_injector_port = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    accessories = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    operation_mode = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    interface = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    package = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    ir_distance = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    sfp_mini_gbic_slots = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    power_consumption = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    poe_extend_mode = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    dimensions = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    weight = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    operating_temperature = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    operating_humidity = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    power_requirement = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    frequency_band = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    pixel = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    ) 
    power = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    processor = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    ram = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    graphics_card = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    ssd = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    hdd = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    display = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    color = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    camera = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    sound = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    operating_system = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    compatibility = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    resource = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    monitor = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    raid = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Memory_Type = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    dimm_capacity = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Processor_catch = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Processor_core_aviable = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Processor_number = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Data_rate = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Network_Interface = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Video_Input = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Video_Output = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    usb_Interface = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    sata_Interface = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Exit_Button = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Fire_Alarm_input = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Throughput = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    wan = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    lan = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    console = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    fax_ower_ip = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    system_capacity = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Access_Mode = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Connectors = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Power_Requirements = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Power_Supply = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    usp_port = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    usb_type_c = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    htmi = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    vga = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Display_Port = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Network = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Wireless = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Webcam = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Fingerprint = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Function = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Connection = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    os_Support = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Print_Speed = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Scan_Feature = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Replacement_cartridges = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Page_yields = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Compatiable_Printers = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Transmission_Distance = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Connector_Type = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Fiber_Type = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Wavelenght = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Voltage = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Input_Voltage_Range = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Battery = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Frequency = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Output_Voltage = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Battery_Charging_Time = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Capacity = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    Print_Technology = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )


    class Meta:
        model = Product
        fields = '__all__'
