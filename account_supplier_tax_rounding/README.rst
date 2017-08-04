.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================
Supplier Tax Rounding
=====================

Sometimes supplier systems use a different rounding method for taxes
than your own.  In NZ and Austrlia (and most VAT based countries) if you ordinarily
supply ex Tax you must use round globally.  However, some systems do not support this
and often supplier invoices mismatch by a cent or so.  This module claculates tax using
round_per_line if set on the supplier for their invoices.

NOTE: This module does nothing if your default rounding method is round_per_line.

Installation
============

There are no special installation instructions for this module.

Configuration
=============

There are no specific configuration options in this module.

Usage
=====

To use this module, you need to:

#. Set the rounding method to Round per Line on the partner.

Known issues / Roadmap
======================

* Currently no tests.
* The field is not multicompany aware.  Shouldn't be an issue in practice as ordinarily tax policy is country based and cross border transactions do not attract value added tax.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/odoonz/account/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Contributors
------------

* Graeme Gellatly <g@o4sb.com>

Maintainer
----------

This module is maintained by Open for Small Business Ltd.

Open for Small Business is a small developer and integrator of Odoo software since 2009.
