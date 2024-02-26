<script setup lang="ts">
import { ref, watch } from "vue";

const props = withDefaults(
  defineProps<{
    total?: number;
    page?: number;
    size?: number;
  }>(),
  {
    total: 0,
    page: 0,
    size: 10,
  }
);
const emit = defineEmits<{
  (e: "updatePage", page: number): void;
}>();

const currentPage = ref(props.page);
watch(currentPage, (newPage) => {
  emit("updatePage", newPage);
});
const createArrayUpTo = (num: number) =>
  Array.from({ length: num }, (_, i) => i + 1);
const pageArr = createArrayUpTo(Math.ceil(props.total / props.size));
</script>

<template>
  <div class="flex justify-end pt-3">
    <div class="join">
      <button
        v-if="currentPage > 1"
        class="join-item btn btn-sm"
        @click="
          () => {
            currentPage -= 1;
          }
        "
      >
        «
      </button>
      <template v-for="p in pageArr">
        <input
          v-if="p !== props.page"
          v-model="currentPage"
          class="join-item btn btn-square btn-sm"
          type="radio"
          name="options"
          :aria-label="`${p}`"
          :value="p"
          checked
        />
        <input
          v-else
          v-model="currentPage"
          class="join-item btn btn-square btn-sm btn-active"
          type="radio"
          name="options"
          :aria-label="`${p}`"
          :value="p"
          checked
        />
      </template>
      <button
        v-if="currentPage < pageArr.length"
        class="join-item btn btn-sm"
        @click="
          () => {
            currentPage += 1;
          }
        "
      >
        »
      </button>
    </div>
  </div>
</template>
