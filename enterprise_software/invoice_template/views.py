from .config_variables import invoice_template_config
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML


# Simulating input that will be generated from billing page form
bill_info = {"customer_name" : "ABC XYZ",
             "customer_phone" : "+91 566451237x",
             "invoice_id" : "202203291212",
             "invoice_date" : "2022-03-29 12:12",
             "item_details" : [
                  {"item_name": "Kurta", "unit_price" : 250, "qty": 2, "amount" : 500},
                  {"item_name": "Nighty", "unit_price" : 130, "qty": 3, "amount" : 390},
                  {"item_name": "Cap", "unit_price" : 80, "qty": 4, "amount" : 320},
              ],
             "sub_total" : {"qty": 9, "amount": "1,210.00"},
             "discount" : {"display": True, "percentage" : "0.00 %", "amount": "0.00"},
             "tax" : {"display": True, "percentage" : "0.00 %", "amount": "0.00"},
             "grand_total" : "1,210.00"
             }


def populate_invoice_template(request):
    context = {"config" : invoice_template_config, "bill_info": bill_info}
    return render(request, "invoice_template/invoice_template.html", context)


def print_invoice(request):
    if request.method == 'POST':
        request_data = request.POST
        # print(request_data)

        context = {"config": invoice_template_config, "bill_info": bill_info}

        current_site = get_current_site(request).domain
        scheme = request.is_secure() and "https" or "http"
        site = '{scheme}://{host}'.format(scheme=scheme, host=current_site)

        invoice = render_to_string("invoice_template/invoice_template.html", context)
        html_invoice = HTML(string=invoice, base_url=site)
        pdf_invoice = html_invoice.write_pdf()

        response = HttpResponse(pdf_invoice, content_type='application/pdf')
        response['Content-Disposition'] = ('inline; filename=' + "invoice.pdf")
        return response

    else:
        return redirect("home_page")


def home_page(request):
    return render(request, "invoice_template/home_page.html")

