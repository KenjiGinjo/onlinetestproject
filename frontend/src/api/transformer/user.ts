import { EnumUserGender } from "@/enums";
export type DctUser = {
  id: number;
  name: string;
  gender: EnumUserGender;
};
