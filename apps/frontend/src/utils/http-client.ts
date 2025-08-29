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
  const response = await httpClient.post("/upload/files/", formData);
  return response.data;
};

export const requestStorageIndexes = async () => {
  const response = await httpClient.get("/manage/storage");
  return response.data;
};

export const requestParseDocuments = async (fileNames: string[]) => {
  const response = await httpClient.post("/parse/documents/", { fileNames });
}