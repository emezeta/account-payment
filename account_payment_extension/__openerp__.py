# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2008 Zikzakmedia S.L. (http://zikzakmedia.com)
#                       Jordi Esteve <jesteve@zikzakmedia.com>
#    AvanzOSC, Avanzed Open Source Consulting
#    Copyright (C) 2011-2012 Iker Coranti (www.avanzosc.com).
#    Copyright (c) 2013 Serv. Tecnol. Avanzados (http://www.serviciosbaeza.com)
#                       Pedro Manuel Baeza <pedro.baeza@serviciosbaeza.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Account Payment Extension",
    "version": "1.2",
    "author": "Zikzakmedia SL",
    "category": "Accounting & Finance",
    "website": "www.zikzakmedia.com",
    "license": "AGPL-3",
    "description": """Account payment extension.

This module extends the account_payment module with a lot of features:
    * Definition of payment types (cash, bank transfer, automatical bank
      transfer, ...). The payment type has a translatable name and note that
      can be shown in the invoices.
    * Two default payment types for partners (client and supplier).
    * Automatic selection of payment type in invoices. Now an invoice can have
      a payment term (30 days, 30/60 days, ...) and a payment type (cash, bank
      transfer, ...).
    * A default check field in partner bank accounts. The default partner bank
      accounts are selected in invoices and payments.
    * New menu/tree/forms to see payments to receive and payments to pay.
    * The payments show tree editable fields: Due date, bank account and a check
      field (for example to write down if a bank check in paper support has been
      received).
    * Two types of payment orders: Payable payment orders (from supplier
      invoices) and receivable payment orders (from client invoices). So we can
      make payment orders to receive the payments of our client invoices. Each
      payment order type has its own sequence.
    * The payment orders allow negative payment amounts. So we can have payment
      orders for supplier invoices (pay money) and refund supplier invoices
      (return or receive money). Or for client invoices (receive money) and
      refund client invoices (return or pay money).
    * Payment orders: Selected invoices are filtered by payment type, the second
      message communication can be set at the same time for several invoices.
Based on previous work of Pablo Rocandio & Zikzakmedia (version for 4.2).
""",
    "depends": [
        "base",
        "account",
        "account_payment",
    ],
    "update_xml": [
        "security/account_payment_extension_security.xml",
        "security/ir.model.access.csv",
        "wizard/account_payment_order_view.xml",
        "payment_view.xml",
        "payment_sequence.xml",
        "wizard/account_move_line_payment_view.xml",
    ],
    "installable": True,
}
