# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2016, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from shuup.apps import AppConfig
from shuup.apps.settings import validate_templates_configuration


class ShuupAdminAppConfig(AppConfig):
    name = "shuup.admin"
    verbose_name = "Shuup Admin"
    label = "shuup_admin"
    required_installed_apps = ["bootstrap3"]
    provides = {
        "admin_module": [
            "shuup.admin.modules.system:SystemModule",
            "shuup.admin.modules.products:ProductModule",
            "shuup.admin.modules.product_types:ProductTypeModule",
            "shuup.admin.modules.media:MediaModule",
            "shuup.admin.modules.orders:OrderModule",
            "shuup.admin.modules.taxes:TaxModule",
            "shuup.admin.modules.categories:CategoryModule",
            "shuup.admin.modules.contacts:ContactModule",
            "shuup.admin.modules.contact_groups:ContactGroupModule",
            "shuup.admin.modules.permission_groups:PermissionGroupModule",
            "shuup.admin.modules.users:UserModule",
            "shuup.admin.modules.service_providers:ServiceProviderModule",
            "shuup.admin.modules.services:PaymentMethodModule",
            "shuup.admin.modules.services:ShippingMethodModule",
            "shuup.admin.modules.attributes:AttributeModule",
            "shuup.admin.modules.sales_units:SalesUnitModule",
            "shuup.admin.modules.shops:ShopModule",
            "shuup.admin.modules.demo:DemoModule",
            "shuup.admin.modules.manufacturers:ManufacturerModule",
            "shuup.admin.modules.suppliers:SupplierModule"
        ],
        "service_provider_admin_form": [
            "shuup.admin.modules.service_providers.forms:CustomCarrierForm",
            "shuup.admin.modules.service_providers.forms:CustomPaymentProcessorForm"
        ],
        "service_behavior_component_form": [
            "shuup.admin.modules.services.forms:FixedCostBehaviorComponentForm",
            "shuup.admin.modules.services.forms:WaivingCostBehaviorComponentForm",
            "shuup.admin.modules.services.forms:WeightLimitsBehaviorComponentForm",
            "shuup.admin.modules.services.forms:GroupAvailabilityBehaviorComponentForm",
            "shuup.admin.modules.services.forms.StaffOnlyBehaviorComponentForm",
        ],
        "service_behavior_component_form_part": [
            "shuup.admin.modules.services.weight_based_pricing.WeightBasedPricingFormPart"
        ],
        "admin_order_section": [
            "shuup.admin.modules.orders.sections:ContentsOrderSection",
            "shuup.admin.modules.orders.sections:PaymentOrderSection",
            "shuup.admin.modules.orders.sections:LogEntriesOrderSection",
        ]
    }

    def ready(self):
        from shuup.core.order_creator.signals import order_creator_finished
        from shuup.admin.modules.orders.receivers import handle_custom_payment_return_requests

        order_creator_finished.connect(handle_custom_payment_return_requests,
                                       dispatch_uid='shuup.admin.handle_cash_payments')
        validate_templates_configuration()


default_app_config = "shuup.admin.ShuupAdminAppConfig"
