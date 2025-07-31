<template>
  <div class="bg-black text-white">
    <div class="container content">
      <div class="flex flex-col md:flex-row gap-8 md:justify-between">
        <!-- Left footer column -->
        <div calss="flex flex-col">
          <div class="w-fit">
            <router-link to="/">
              <img
                src="@/assets/aura_logo_light.svg"
                alt="Aura Logo"
                class="mr-5 min-w-[80px] max-w-[80px] md:max-w-[90px]"
              />
            </router-link>
          </div>
          <!-- Footer badges
          <div class="text-xs py-5 flex flex-col gap-1">
            <div>
              Sic Semper Tyrannis
              <img
                :src="vaSeal"
                alt="VA Flag Seal"
                class="max-h-[18px] inline-block align-middle"
              />
            </div>
            <div>
              Happy
              <img :src="prideBadge" alt="Pride Badge" class="inline-block align-middle" />
              Month
            </div>
            <div>
              Be
              <img :src="niceBadge" alt="Nice Badge" class="inline-block align-middle" />
              Always
            </div>
          </div> -->
        </div>

        <!-- Right footer column -->
        <div class="md:w-1/2">
          <!-- Wrapper for footer right-column sections -->
          <div class="flex flex-col">
            <!-- Column menus -->
            <div class="flex gap-6">
              <div class="flex flex-col gap-6">
                <div class="text-xs">ABOUT US</div>
                <ul class="flex flex-col gap-2 list-none p-0 m-0">
                  <li>Mission</li>
                  <li>Leadership</li>
                </ul>
              </div>
              <div class="flex flex-col gap-6">
                <div class="text-xs">PRODUCTS</div>
                <ul class="flex flex-col gap-2 list-none p-0 m-0">
                  <li>AURA Intake</li>
                  <li>AURA Bridge</li>
                  <li>AURA Insight</li>
                </ul>
              </div>
            </div>

            <div class="flex flex-col gap-6 mt-10">
              <div class="text-xs">CONTACT US</div>
              <ul class="flex flex-col gap-2 list-none p-0 m-0">
                <li>contact@aura.soon</li>
                <li>
                  <router-link to="/feedback" class="hover:text-gray-300 transition-colors">
                    Leave Feedback
                  </router-link>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <!-- End of right column -->
      </div>

      <!-- Copyright & policy strip -->
      <div class="flex flex-col-reverse md:flex-row justify-between mt-30 text-xs">
        <div class="mt-10 md:mt-0">@Aura Solutions, 2025</div>
        <div class="md:w-1/2">
          <ul class="list-none p-0 m-0 flex gap-6">
            <li>
              <router-link to="/license" class="hover:text-gray-300 transition-colors">
                License
              </router-link>
            </li>
            <li>
              <router-link to="/terms-of-service" class="hover:text-gray-300 transition-colors">
                Terms of Service
              </router-link>
            </li>
            <li>Modern AI Policy</li>
          </ul>
        </div>
      </div>

      <!-- <div class="text-xs py-5">
        Sic semper tyrannis
      </div> -->
    </div>
  </div>
</template>

<script setup lang="ts"></script>
