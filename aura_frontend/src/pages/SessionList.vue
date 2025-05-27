<template>
    <!-- Navigation Bar -->
    <div class="bg-black border-b-1 border-white flex">
        <div class="border-r-1 border-white p-6 px-10 w-fit text-2xl font-bold">
            AURA SOLUTIONS
        </div>
        <div class="border-r-1 border-white p-6 px-10 w-fit flex align-center items-center gap-8 text-sm">
            <router-link to="/" class="text-white hover:underline underline-offset-6">
                Home
            </router-link>
             <router-link to="/agent" class="text-white hover:underline underline-offset-6">
                Create
            </router-link>
             <router-link to="/sessions" class="text-white hover:underline underline-offset-6">
                Track
            </router-link>
        </div>
    </div>
    
    <!-- Landing Content -->
  <div class="container mx-auto py-12 space-y-6">
    <h1 class="text-3xl font-bold">Track Sessions</h1>

    <p class="text-base">
      Track the progress of each session, view details, and download outputs for completed applications.
    </p>

    <button
      class="hover:bg-red-500 hover:text-white px-3 py-1 border-1 border-red-700"
      @click="handleDeleteAll"
      :disabled="isLoading"
    >
      Delete All Sessions
    </button>

    <table class="w-full text-left border-collapse mt-4">
        <tbody>
          <tr v-for="session in sessions" :key="session.token" class="border-b border-white">
            <td class="py-3 px-4 w-12">
              <span
                class="inline-block w-3 h-3 rounded-full"
                :class="{
                  'bg-green-500': session.status === 'completed',
                  'bg-yellow-400': session.status === 'pending',
                  'bg-red-500': session.status === 'error'
                }"
              ></span>
            </td>
            <td class="py-3 px-4 whitespace-nowrap font-mono text-base text-white">
              {{ session.token }}
            </td>
            <td class="py-3 px-4 whitespace-nowrap text-white capitalize">
              {{ session.status }}
            </td>
            <td class="py-3 px-4">
            <button
              class="hover:bg-red-500 hover:text-white px-3 py-1 border-1 border-red-700"
              @click="handleDelete(session.token)"
              :disabled="isLoading"
            >
              Delete
            </button>
          </td>
          </tr>
        </tbody>
      </table>
      <div v-if="sessions.length === 0" class="text-gray-400 mt-8">No sessions found.</div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import type { ApplicationSession } from '@/types'

import { fetchSessions, deleteSession, deleteAllSessions } from '@/api/sessions'

const sessions = ref<ApplicationSession[]>([])
const isLoading = ref(false)

onMounted(async () => {
  isLoading.value = true
  try {
    sessions.value = await fetchSessions()
    isLoading.value = false
  } catch (error) {
    console.error('Error fetching sessions:', error)
    isLoading.value = false
  }
})

async function handleDelete(token: string) {
  if (!confirm('Are you sure you want to delete this session?')) return
  isLoading.value = true
  try {
    await deleteSession(token)
    sessions.value = sessions.value.filter(s => s.token !== token)
  } catch (error) {
    alert('Failed to delete session.')
  } finally {
    isLoading.value = false
  }
}

async function handleDeleteAll() {
  if (!confirm('Are you sure you want to delete ALL sessions?')) return
  isLoading.value = true
  try {
    await deleteAllSessions()
    sessions.value = []
  } catch (error) {
    alert('Failed to delete all sessions.')
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped></style>