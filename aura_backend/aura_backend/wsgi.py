#
# Aura Insurance Engine – Proprietary Software
#
# Copyright © 2025 Jose Reyes (GitHub: @reyesjl). All rights reserved.
#
# This software was developed solely by Jose Reyes – full-stack engineer and designer.
# Jacob Powers contributed as the licensed insurance agent for the project.
# It is a modern insurance submission platform built to streamline the intake
# and processing of insurance applications.
#
# This code is proprietary and confidential. Unauthorized use, reproduction,
# distribution, or modification is strictly prohibited.
#
# Project repository: https://github.com/reyesjl/aura-insurance-engine
# DeepWiki: https://app.devin.ai/wiki/reyesjl/aura-insurance-engine
#

"""
WSGI config for aura_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aura_backend.settings')

application = get_wsgi_application()
