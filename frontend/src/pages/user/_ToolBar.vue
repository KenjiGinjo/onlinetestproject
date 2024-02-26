<script setup lang="ts">
import ButtonVue from "@/components/base/Button.vue";
const props = defineProps<{
  onClick: () => void;
}>();
</script>
<template>
  <div class="flex pb-2 justify-between">
    <h1 class="pl-2 font-bold">Users Panel</h1>
    <ButtonVue title="Add User" @click="props.onClick" />
  </div>
</template>
