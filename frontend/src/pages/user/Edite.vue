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
  id: "",
  name: "",
  gender: EnumUserGender.Male,
});
const notice = reactive({
  type: "error" as "error" | "success",
  message: "",
});
async function updateUserHandler() {
  if (!form.name) {
    notice.type = "error";
    notice.message = "Name is required";
    return;
  }
  try {
    await client.user.$put({
      body: {
        name: form.name,
        gender: form.gender,
      },
      params: { userId: form.id },
    });
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
function setForm(e: any) {
  form.id = e.uid;
  form.name = e.name;
  form.gender = e.gender;
}
defineExpose({
  setForm,
});
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
      <ButtonVue title="Update User" @click="updateUserHandler" />
      <ButtonVue title="Cancel" default @click="cancelHanlder" />
    </div>
  </div>
</template>
