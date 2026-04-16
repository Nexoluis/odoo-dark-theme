{
    'name': 'AGX Dark Theme',
    'version': '17.0.2.0.0',
    'category': 'Web',
    'summary': 'Complete Catppuccin Mocha dark theme for Odoo 17 Community backend',
    'description': 'Elegant dark mode for Odoo 17 Community. Based on the Catppuccin Mocha palette. Covers all backend views with correct SCSS variable overrides.',
    'author': 'AGX OSINT SL.',
    'website': 'https://github.com/agxosint/odoo-dark-theme',
    'license': 'LGPL-3',
    'depends': ['web'],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'agx_dark_theme/static/src/scss/_variables.scss'),
        ],
        'web.assets_backend': [
            ('append', 'agx_dark_theme/static/src/scss/_overrides.scss'),
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
