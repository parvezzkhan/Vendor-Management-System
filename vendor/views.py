from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from django.http import JsonResponse
import json
from .serializers import *
from .models import *



@csrf_exempt
def Createvendor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        vendorcode = request.POST.get('vendorcode')
        Vendor.objects.create(name=name, contact=contact, address=address, vendor_code=vendorcode)
    
        return JsonResponse({'message': 'Vendor created successfully'})
    return JsonResponse({'message': 'Invalid request method'})

@csrf_exempt
def Listall(request):
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return JsonResponse(serializer.data,safe=False)

    return JsonResponse({'message': 'Invalid request method'}, status=400)

@csrf_exempt
def Retrieve(request,pk):
    if request.method == 'GET':
        vendors = Vendor.objects.filter(id=pk)
        serializer = VendorSerializer(vendors, many=True)
        return JsonResponse(serializer.data,safe=False)
    return JsonResponse({'message': 'Invalid request method'}, status=400)

@csrf_exempt
def Updatevendor(request, vendor_code):
    if request.method == 'PUT':
        vendor_instance = get_object_or_404(Vendor, vendor_code=vendor_code)

    if vendor_instance:

        try:
            request_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)


        vendor_instance.name = request_data.get('name', vendor_instance.name)
        vendor_instance.contact = request_data.get('contact', vendor_instance.contact)
        vendor_instance.address = request_data.get('address', vendor_instance.address)

        vendor_instance.save()
        return JsonResponse({'message': f'Vendor with vendor_code {vendor_code} updated successfully'})
    else:
        return JsonResponse({'error': f'Vendor with vendor_code {vendor_code} not found'}, status=404)


@csrf_exempt
def Deletevendor(request, vendor_code):
     if request.method == 'DELETE':
        try:
            vendor = get_object_or_404(Vendor, vendor_code=vendor_code)
            vendor.delete()
            return JsonResponse({'message': 'Vendor deleted successfully.'}, status=200)
        except Vendor.DoesNotExist:
            return JsonResponse({'error': 'Vendor not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {e}'}, status=500)

@csrf_exempt
def CreatePO(request):
    if request.method == 'POST':
        try:
            po_number = request.POST.get('po_number')
            vendor_reference = request.POST.get('vendor_reference')
            order_date = request.POST.get('order_date')
            items = request.POST.get('items')
            quantity = request.POST.get('quantity')
            vendor_name = request.POST.get('vendor') 
            delivery_date = request.POST.get('delivery_date')
            quality_rating = request.POST.get('quality_rating')
            response_time = request.POST.get('response_time')
            fulfilled_without_issue = request.POST.get('fulfilled_without_issue')

            status = 'draft'
            vendor = Vendor.objects.get(name=vendor_name)


            purchase_order = PurchaseOrder.objects.create(
                po_number=po_number,
                vendor_reference=vendor_reference,
                order_date=order_date,
                items=items,
                quantity=quantity,
                status=status,
                vendor=vendor,
                delivery_date=delivery_date,
                quality_rating=quality_rating,
                response_time=response_time,
                fulfilled_without_issue=fulfilled_without_issue,

            )

            return JsonResponse({'message': 'Purchase Order created successfully'}, status=201)

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def ListPO(request):
    if request.method == 'GET':
        purchase_orders = PurchaseOrder.objects.all()

    vendor_filter = request.GET.get('vendor')
    if vendor_filter:
        purchase_orders = purchase_orders.filter(vendor_reference=vendor_filter)

    serialized_purchase_orders = []
    for po in purchase_orders:
        serialized_purchase_orders.append({
            'po_number': po.po_number,
            'vendor_reference': po.vendor_reference,
            'order_date': po.order_date,
            'items': po.items,
            'quantity': po.quantity,
            'status': po.status,
        })

    response_data = {
        'purchase_orders': serialized_purchase_orders,
        'vendors': list(PurchaseOrder.objects.values_list('vendor_reference', flat=True).distinct()),
        'selected_vendor': po.vendor_reference,
    }

    return JsonResponse(response_data, safe=False)

@csrf_exempt
def RetrievePO(request, po_number):
    if request.method == 'GET':
        po_instance = PurchaseOrder.objects.filter(po_number=po_number).first()

   
    if po_instance:
        po_data = {
            'po_number': po_instance.po_number,
            'vendor_reference': po_instance.vendor_reference,
            'order_date': po_instance.order_date,
            'items': po_instance.items,
            'quantity': po_instance.quantity,
            'status': po_instance.status,
        }

        return JsonResponse(po_data)
    else:
        return JsonResponse({'error': f'PurchaseOrder with po_number {po_number} not found'}, status=404)
    

@csrf_exempt
def UpdatePO(request, po_number):
    if request.method == 'PUT':
        po_instance = get_object_or_404(PurchaseOrder, po_number=po_number)

    if po_instance:
      
        try:
            request_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        po_instance.vendor_reference = request_data.get('vendor_reference', po_instance.vendor_reference)
        po_instance.order_date = request_data.get('order_date', po_instance.order_date)
        po_instance.items = request_data.get('items', po_instance.items)
        po_instance.quantity = request_data.get('quantity', po_instance.quantity)
        po_instance.status = request_data.get('status', po_instance.status)

        po_instance.save()

       
        return JsonResponse({'message': f'PurchaseOrder with po_number {po_number} updated successfully'})
    else:
       
        return JsonResponse({'error': f'PurchaseOrder with po_number {po_number} not found'}, status=404)

@csrf_exempt
def DeletePO(request, po_number):
    if request.method == 'DELETE':
        try:
            po = get_object_or_404(PurchaseOrder, po_number=po_number)
            po.delete()
            return JsonResponse({'message': 'Purchase Order deleted successfully.'}, status=200)
        except Vendor.DoesNotExist:
            return JsonResponse({'error': 'Purchase Order not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {e}'}, status=500)
        

@csrf_exempt
def Retrievevendorprfm(request, pk):
    if request.method == 'GET':
     vendor = get_object_or_404(Vendor, pk=pk)

    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    on_time_orders = PurchaseOrder.objects.filter(vendor=vendor, fulfilled_without_issue=True).count()

    average_response_time = calculate_average_response_time(vendor)

    fulfillment_rate = (on_time_orders / total_orders) * 100 if total_orders else 0

    data = {
        'on_time_delivery_rate': fulfillment_rate,
        'average_response_time': average_response_time,
        'fulfillment_rate': fulfillment_rate,
    }

    return JsonResponse(data, status=200)

@csrf_exempt
def calculate_average_response_time(vendor):

    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()

    sum_response_time = 0
    for order in PurchaseOrder.objects.filter(vendor=vendor):
        if order.fulfilled_without_issue and order.delivery_date:
            sum_response_time += (order.delivery_date - order.order_date).days

    return sum_response_time / total_orders if total_orders else 0