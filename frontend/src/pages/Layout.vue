<script setup lang="ts">
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
</script>
<template>
  <div class="artboard artboard-horizontal phone-3">
    <Header />
    <slot></slot>
    <Footer />
  </div>
</template>
