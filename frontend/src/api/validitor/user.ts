import { z } from "zod";

export type vUserListQuery = z.infer<typeof vUserListQuery>;

export const vUserListQuery = z.object({
  page: z.number({
    required_error: "页码不能为空",
    invalid_type_error: "页码参数错误",
  }),
});
export type vCreateUser = z.infer<typeof vCreateUser>;

export const vCreateUser = z.object({
  name: z.string({
    required_error: "姓名不能为空",
    invalid_type_error: "姓名参数错误",
  }),
  gender: z.nativeEnum(EnumUserGender, {
    required_error: "性别不能为空",
    invalid_type_error: "性别参数错误",
  }),
});

export const vEditUser = vCreateUser;
