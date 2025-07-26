/*
 * Aura Insurance Engine – Proprietary Software
 *
 * Copyright © 2025 Jose Reyes (GitHub: @reyesjl). All rights reserved.
 *
 * This software was developed solely by Jose Reyes – full-stack engineer and designer.
 * Jacob Powers contributed as the licensed insurance agent for the project.
 * It is a modern insurance submission platform built to streamline the intake
 * and processing of insurance applications.
 *
 * This code is proprietary and confidential. Unauthorized use, reproduction,
 * distribution, or modification is strictly prohibited.
 *
 * Project repository: https://github.com/reyesjl/aura-insurance-engine
 * DeepWiki: https://app.devin.ai/wiki/reyesjl/aura-insurance-engine
 */

import { test, expect } from '@playwright/test';

// See here how to get started:
// https://playwright.dev/docs/intro
test('visits the app root url', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('h1')).toHaveText('You did it!');
})
