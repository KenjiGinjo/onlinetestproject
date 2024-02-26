<script setup lang="ts">
const props = defineProps<{
  title?: string;
  outLine?: boolean;
  default?: boolean;
}>();
</script>
<template>
  <button
    :class="`btn btn-sm ${props.default ? '' : 'btn-primary'} ${
      props.outLine ? 'btn-outline' : ''
    }`"
  >
    {{ props.title }}
  </button>
</template>
