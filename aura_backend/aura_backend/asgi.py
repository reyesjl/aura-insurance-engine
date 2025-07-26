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
ASGI config for aura_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aura_backend.settings')

application = get_asgi_application()
