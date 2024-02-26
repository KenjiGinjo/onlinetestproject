<script setup lang="ts">
import PagenationVue from "@/components/base/Pagenation.vue";
import ModalVue from "@/components/base/Modal.vue";
import TableVue from "./_Table.vue";
import ToolBarVue from "./_ToolBar.vue";
import CreateUserVue from "./Create.vue";
import EditeUserVue from "./Edite.vue";
import { onMounted, reactive, ref } from "vue";
import { client } from "@/api/client";
import { DctUser } from "@/api/transformer/user";

const EditeUserVueRef = ref<InstanceType<typeof EditeUserVue> | null>(null);
type State = {
  createFormShow: boolean;
  editFormShow: boolean;
  data: DctUser[];
  page: number;
  pageTotal: number;
};
const state = reactive<State>({
  createFormShow: false,
  editFormShow: false,
  data: [],
  page: 1,
  pageTotal: 0,
});
onMounted(async () => {
  await setUsers();
});
async function setUsers() {
  const response: any = await client.user.users.$get({
    query: {
      page: state.page,
    },
  });
  state.data = response?.body ? response.body.users : [];
  state.pageTotal = response?.body ? response.body.total : 0;
}

async function refreshUsers() {
  state.page = 1;
  await setUsers();
}
function closeModal() {
  state.createFormShow = false;
  state.editFormShow = false;
}
</script>
<template>
  <div class="border-2 p-4">
    <ToolBarVue
      :onClick="
        () => {
          state.createFormShow = true;
        }
      "
    />
    <TableVue
      :data="state.data"
      :onEdit="
        (row) => {
          EditeUserVueRef?.setForm(row);
          state.editFormShow = true;
        }
      "
    />
    <PagenationVue
      :total="100"
      :page="1"
      :size="20"
      @updatePage="
        async (page) => {
          state.page = page;
          await setUsers();
        }
      "
    />
    <ModalVue
      :title="state.createFormShow ? 'Create User' : 'Edit User'"
      :showModal="state.createFormShow || state.editFormShow"
    >
      <CreateUserVue
        v-if="state.createFormShow"
        :refreshUsers="refreshUsers"
        :closeModal="closeModal"
      />
      <EditeUserVue
        ref="EditeUserVueRef"
        v-show="state.editFormShow"
        :form="state.editFormShow"
        :refreshUsers="refreshUsers"
        :closeModal="closeModal"
      />
    </ModalVue>
  </div>
</template>
