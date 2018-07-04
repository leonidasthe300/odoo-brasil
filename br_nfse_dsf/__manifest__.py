# -*- coding: utf-8 -*-
# © 2016 Danimar Ribeiro <danimaribeiro@gmail.com>, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Envio de NFS-e - Provedor DSF',
    'summary': """Permite o envio de NFS-e DSF através das faturas do Odoo
    Mantido por Trustcode""",
    'description': 'Envio de NFS-e - Nota Fiscal DSF',
    'version': '11.0.1.0.0',
    'category': 'account',
    'author': 'Trustcode',
    'license': 'AGPL-3',
    'website': 'http://www.trustcode.com.br',
    'contributors': [
        'Danimar Ribeiro <danimaribeiro@gmail.com>',
    ],
    'depends': [
        'br_account_einvoice',
    ],
    'external_dependencies': {
        'python': [
            'pytrustnfe.nfse.dsf',
            'pytrustnfe.certificado',
            'hashlib',
            'zeep',
        ],
    },
    'data': [
        'views/br_account_service.xml',
        'views/invoice_eletronic.xml',
        'views/account_fiscal_position.xml',
        'views/account_invoice.xml',
        'reports/danfse_dsf.xml',
        'data/res.state.city.csv',
    ],
    'installable': True,
    'application': True,
}
