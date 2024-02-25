import { initClient } from "@ts-rest/core";
import { contract } from "./contract";
import axios, {
  Method,
  AxiosError,
  AxiosResponse,
  isAxiosError,
  AxiosHeaders,
} from "axios";
export const client = initClient(contract, {
  baseUrl: process.env.API_BASE_URL as string,
  baseHeaders: {
    "Content-Type": "application/json",
  },
  api: async ({ path, method, headers, body }) => {
    try {
      const result = await axios.request({
        method: method as Method,
        url: `${process.env.API_BASE_URL as string}/${path}`,
        headers: headers as AxiosHeaders,
        data: body,
      });
      return {
        status: result.status,
        body: result.data,
        headers: result.headers as any,
      };
    } catch (e: Error | AxiosError | any) {
      if (isAxiosError(e)) {
        const error = e as AxiosError;
        const response = error.response as AxiosResponse;
        return {
          status: response.status,
          body: response.data,
          headers: response.headers,
        };
      }
      throw e;
    }
  },
});
