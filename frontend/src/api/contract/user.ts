import { initContract } from "@ts-rest/core";
import { vCreateUser, vEditUser, vUserListQuery } from "../validitor/user";
import { DctUser } from "../transformer/user";

const c = initContract();

export const user = c.router({
  users: {
    $get: {
      method: "GET",
      path: "/users",
      responses: {
        200: c.type<{
          users: DctUser[];
          page: number;
          pages: number;
          total: number;
        }>(),
      },
      query: vUserListQuery,
      summary: "获取用户",
    },
  },
  $post: {
    method: "POST",
    path: "/user",
    responses: {
      200: c.type<DctUser>(),
    },
    body: vCreateUser,
    summary: "创建用户",
  },
  $put: {
    method: "PUT",
    path: "/user/:userId",
    responses: {
      200: c.type<DctUser>(),
    },
    body: vEditUser,
    summary: "更新用户",
  },
});
