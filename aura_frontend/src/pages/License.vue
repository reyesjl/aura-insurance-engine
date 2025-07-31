<template>
  <NavBar />
  <div class="bg-white text-black min-h-screen pt-20">
    <div class="container content py-16">
      <div class="max-w-4xl mx-auto">
        <div class="text-5xl font-bold text-black mb-16">License Agreement</div>

        <div class="prose prose-lg max-w-none">
          <div class="text-2xl font-bold mb-8">AURA INSURANCE ENGINE LICENSE AGREEMENT</div>

          <div class="mb-8">
            <div class="text-lg font-semibold mb-4">Copyright © 2025 Jose Reyes</div>
            <p class="text-base leading-relaxed mb-6">
              This software ("AURA Insurance Engine") is proprietary and confidential. All rights
              reserved.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">1. License Grant</div>
            <p class="text-base leading-relaxed">
              Subject to the terms of this agreement, the Licensor (Jose Reyes) grants the Licensee
              a non-exclusive, non-transferable, non-sublicensable license to use the Software
              solely for internal business operations.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">2. Restrictions</div>
            <p class="text-base leading-relaxed mb-4">The Licensee shall not:</p>
            <ul class="list-disc list-inside space-y-2 text-base leading-relaxed ml-4">
              <li>Copy, distribute, or modify the Software;</li>
              <li>Reverse engineer, decompile, or attempt to derive source code;</li>
              <li>
                Use the Software for any commercial purpose without express written consent from the
                Licensor;
              </li>
              <li>Share access or license keys with any third party.</li>
            </ul>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">3. Ownership</div>
            <p class="text-base leading-relaxed">
              All intellectual property rights, including but not limited to the dynamic template
              system, question snapshotting, agent workflows, and API integrations, remain the sole
              property of Jose Reyes.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">4. Confidentiality</div>
            <p class="text-base leading-relaxed">
              Licensee agrees to treat all software, architecture, workflows, and associated
              documentation as strictly confidential.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">5. Termination</div>
            <p class="text-base leading-relaxed">
              Any breach of this agreement terminates the license immediately. Upon termination, the
              Licensee must cease all use and destroy all copies.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">6. No Warranty</div>
            <p class="text-base leading-relaxed">
              The software is provided "as is" without warranties of any kind, express or implied.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">7. Governing Law</div>
            <p class="text-base leading-relaxed">
              This Agreement shall be governed by and construed in accordance with the laws of the
              State of North Carolina, USA.
            </p>
          </div>

          <div class="border-t border-gray-200 pt-8 mt-12">
            <div class="text-sm text-gray-600 text-center">End of License Agreement</div>
          </div>
        </div>

        <div class="mt-16 flex justify-center">
          <router-link
            to="/"
            class="px-8 py-4 bg-black text-black font-bold hover:bg-gray-800 transition duration-300"
          >
            Back to Home
          </router-link>
        </div>
      </div>
    </div>
  </div>
  <FootBar />
</template>

<script setup lang="ts">
import FootBar from '@/components/FootBar.vue'
import NavBar from '@/components/NavBar.vue'
</script>
