import axios from "axios";

export const httpClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});
httpClient.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export const requestGetConfig = async () => {
  // const response = await httpClient.get("/config");
  // return response.data;

  // mock data
  return {
    chunkingConfig: [
      { id: "0", name: "Fixed-size", config: {} },
      { id: "1", name: "Semantic", config: {} },
    ],
    retrievalConfig: [{}],
  };
};

export const requestUploadFiles = async (formData: FormData) => {
  const response = await httpClient.post("/upload/file/", formData);
  return response.data;
}