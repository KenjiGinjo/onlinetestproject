<script setup lang="ts">
const props = defineProps<{
  title?: string;
  outLine?: boolean;
  showModal: boolean;
}>();
</script>

<template>
  <div id="app_modal" class="modal" :class="{ 'modal-open': showModal }">
    <div class="modal-box">
      <h3 class="font-bold text-lg">{{ props.title }}</h3>
      <div class="py-3">
        <slot></slot>
      </div>
    </div>
  </div>
</template>
