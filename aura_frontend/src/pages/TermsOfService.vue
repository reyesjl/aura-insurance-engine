<template>
  <NavBar />
  <div class="bg-white text-black min-h-screen pt-20">
    <div class="container content py-16">
      <div class="max-w-4xl mx-auto">
        <div class="text-5xl font-bold text-black mb-16">Terms of Service</div>

        <div class="prose prose-lg max-w-none">
          <div class="text-2xl font-bold mb-8">AURA Insurance Engine Terms of Service</div>

          <div class="mb-8">
            <div class="text-lg font-semibold mb-4">Effective Date: January 1, 2025</div>
            <p class="text-base leading-relaxed mb-6">
              These Terms of Service ("Terms") govern your use of the AURA Insurance Engine platform
              and services provided by Aura Solutions ("Company", "we", "us", or "our").
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">1. Acceptance of Terms</div>
            <p class="text-base leading-relaxed">
              By accessing or using our services, you agree to be bound by these Terms. If you do
              not agree to these Terms, you may not use our services.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">2. Description of Service</div>
            <p class="text-base leading-relaxed">
              AURA Insurance Engine is a comprehensive platform providing insurance application
              processing, agent workflows, and related services. We reserve the right to modify or
              discontinue services at any time.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">3. User Accounts and Responsibilities</div>
            <p class="text-base leading-relaxed mb-4">Users are responsible for:</p>
            <ul class="list-disc list-inside space-y-2 text-base leading-relaxed ml-4">
              <li>Maintaining the security of their account credentials</li>
              <li>All activities that occur under their account</li>
              <li>Providing accurate and current information</li>
              <li>Complying with all applicable laws and regulations</li>
            </ul>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">4. Prohibited Uses</div>
            <p class="text-base leading-relaxed mb-4">You may not use our services to:</p>
            <ul class="list-disc list-inside space-y-2 text-base leading-relaxed ml-4">
              <li>Violate any laws or regulations</li>
              <li>Infringe on intellectual property rights</li>
              <li>Transmit harmful or malicious content</li>
              <li>Attempt to gain unauthorized access to our systems</li>
              <li>Use the service for fraudulent activities</li>
            </ul>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">5. Data Privacy and Security</div>
            <p class="text-base leading-relaxed">
              We are committed to protecting your data in accordance with applicable privacy laws.
              Your use of our services is also governed by our Privacy Policy, which is incorporated
              by reference into these Terms.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">6. Intellectual Property</div>
            <p class="text-base leading-relaxed">
              All content, features, and functionality of our services are owned by Aura Solutions
              and are protected by copyright, trademark, and other intellectual property laws.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">7. Service Availability</div>
            <p class="text-base leading-relaxed">
              While we strive for high availability, we do not guarantee uninterrupted service. We
              may perform maintenance or updates that temporarily affect service availability.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">8. Limitation of Liability</div>
            <p class="text-base leading-relaxed">
              Our liability is limited to the maximum extent permitted by law. We are not liable for
              any indirect, incidental, or consequential damages arising from your use of our
              services.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">9. Termination</div>
            <p class="text-base leading-relaxed">
              We may terminate or suspend your access to our services at any time for violation of
              these Terms or for any other reason at our sole discretion.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">10. Changes to Terms</div>
            <p class="text-base leading-relaxed">
              We reserve the right to modify these Terms at any time. Changes will be effective upon
              posting. Your continued use of our services constitutes acceptance of the modified
              Terms.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">11. Governing Law</div>
            <p class="text-base leading-relaxed">
              These Terms are governed by the laws of the State of North Carolina, USA, without
              regard to conflict of law principles.
            </p>
          </div>

          <div class="mb-8">
            <div class="text-xl font-bold mb-4">12. Contact Information</div>
            <p class="text-base leading-relaxed">
              If you have questions about these Terms, please contact us at contact@aura.soon
            </p>
          </div>

          <div class="border-t border-gray-200 pt-8 mt-12">
            <div class="text-sm text-gray-600 text-center">Last Updated: January 1, 2025</div>
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
