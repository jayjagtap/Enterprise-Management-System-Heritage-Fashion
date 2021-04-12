import json


def generate_spe_line(length, marker):
    return f"{marker}" * length


invoice_template_config = {
    "shop_title_img": "invoice_creator/invoice_title.png",
    "shop_address": "Shop No 10, Chikhali Road, Sane Chowk, Pune - 412222.",
    "shop_contact": "+91 566451237x",
    "available_items": [["Kurta", "Leggings", "Palazo", "Harem pants", "Cigar pants", "Kurti pants"],
                        ["Jeans", "Tops", "Gowns", "Odhani", "Night dress", "Track pants"]],
    "end_msg": "Thanks for shopping ! Do visit us again !",
    "page_width": "80mm",
    "page_margins": "5mm 2mm 5mm 2mm",
    "font_size": "9px",
    "separation_line": generate_spe_line(93, "-")
}
