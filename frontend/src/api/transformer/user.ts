import { Expose } from "class-transformer";

export class DctUser {
  @Expose()
  id: number;
  @Expose()
  name: string;
  @Expose()
  gender: EnumUserGender;
}
