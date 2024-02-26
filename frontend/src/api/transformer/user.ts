import { Expose } from 'class-transformer';
import { EnumUserGender } from '@/enums';
export class DctUser {
  @Expose()
  id: number;
  @Expose()
  name: string;
  @Expose()
  gender: EnumUserGender;
}
