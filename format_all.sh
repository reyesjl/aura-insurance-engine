#!/bin/bash

#
# Aura Insurance Engine – Proprietary Software
#
# Copyright © 2025 Jose Reyes (GitHub: @reyesjl). All rights reserved.
#
# This software was developed solely by Jose Reyes – full-stack engineer and designer.
# It is a modern insurance submission platform built to streamline the intake
# and processing of insurance applications.
#
# This code is proprietary and confidential. Unauthorized use, reproduction,
# distribution, or modification is strictly prohibited.
#
# Project repository: https://github.com/reyesjl/aura-insurance-engine
# DeepWiki: https://app.devin.ai/wiki/reyesjl/aura-insurance-engine
#

# Format all code in the Aura Insurance Engine project

echo "🎨 Formatting Aura Insurance Engine codebase..."

# Format Frontend (Vue, TypeScript, JavaScript)
echo "📱 Formatting frontend code..."
cd aura_frontend
npm run format
npm run lint
cd ..

# Format Backend (Python)
echo "🐍 Formatting backend code..."
cd aura_backend
source venv/bin/activate
black . --line-length 88
isort . --profile black
deactivate
cd ..

echo "✅ All code formatted successfully!"
