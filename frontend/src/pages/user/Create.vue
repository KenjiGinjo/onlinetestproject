<script setup lang="ts">
import ButtonVue from "@/components/base/Button.vue";
import AlertVue from "@/components/base/Alert.vue";
import { reactive } from "vue";
import { EnumUserGender } from "@/enums";
import { client } from "@/api/client";
const props = defineProps<{
  refreshUsers: () => void;
  closeModal: () => void;
}>();
const form = reactive({
  name: "",
  gender: EnumUserGender.Male,
});
const notice = reactive({
  type: "error" as "error" | "success",
  message: "",
});
async function createUserHandler() {
  if (!form.name) {
    notice.type = "error";
    notice.message = "Name is required";
    return;
  }
  try {
    await client.user.$post({ body: form });
    notice.type = "success";
    notice.message = "User created successfully";
    props.refreshUsers();
    setTimeout(() => {
      props.closeModal();
    }, 500);
  } catch (e) {
    const error = e as any;
    notice.type = "error";
    notice.message = error.message;
  }
}
function cancelHanlder() {
  form.name = "";
  form.gender = EnumUserGender.Male;
  props.closeModal();
}
</script>
<template>
  <div>
    <AlertVue
      v-if="notice.message"
      :type="notice.type"
      :message="notice.message"
    />
    <label class="input input-sm input-bordered flex items-center gap-2">
      Name
      <input v-model="form.name" type="text" class="grow" />
    </label>
    <select
      v-model="form.gender"
      class="mt-3 select select-sm select-bordered w-full"
    >
      <option selected :value="EnumUserGender.Male">
        {{ EnumUserGender.Male }}
      </option>
      <option :value="EnumUserGender.Female">
        {{ EnumUserGender.Female }}
      </option>
    </select>
    <div class="divider" />
    <div class="flex justify-between">
      <ButtonVue title="Create User" @click="createUserHandler" />
      <ButtonVue title="Cancel" default @click="cancelHanlder" />
    </div>
  </div>
</template>
