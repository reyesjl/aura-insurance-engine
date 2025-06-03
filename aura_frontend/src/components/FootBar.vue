<template>
  <div class="bg-black text-white">
    <div class="container content">
      <div class="flex flex-col md:flex-row gap-8 md:justify-between">
        <!-- Left footer column -->
        <div>
          <div class="w-fit">
            <router-link to="/">
              <img
                src="@/assets/aura_logo_light.svg"
                alt="Aura Logo"
                class="mr-5 min-w-[80px] max-w-[80px] md:max-w-[90px]"
              />
            </router-link>
          </div>
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
                  <li>AURA Engine</li>
                  <li>UMSI Integration</li>
                </ul>
              </div>
            </div>

            <div class="flex flex-col gap-6 mt-10">
              <div class="text-xs">CONTACT US</div>
              <ul class="flex flex-col gap-2 list-none p-0 m-0">
                <li>contact@aura.soon</li>
                <li>Leave Feedback</li>
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
            <li>Privacy Policy</li>
            <li>Terms of Use</li>
            <li>Modern AI Policy</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
