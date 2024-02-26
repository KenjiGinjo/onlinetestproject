<script lang="ts" setup>
const props = defineProps<{
  data: Array<Record<string, any>>;
  onEdit: (row: any) => void;
}>();
</script>
<template>
  <div class="overflow-x-auto">
    <table class="table">
      <thead>
        <tr>
          <th>Id</th>
          <th>Name</th>
          <th>Gender</th>
          <th class="text-right">Operation</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in props.data">
          <td>{{ row.uid }}</td>
          <td>{{ row.name }}</td>
          <td>{{ row.gender }}</td>
          <td class="text-right">
            <button class="btn btn-sm btn-ghost" @click="onEdit(row)">
              Edit
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
