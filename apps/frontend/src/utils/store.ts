import { Action, Thunk, action, createStore, thunk } from "easy-peasy";
import { requestGetConfig, requestStorageIndexes } from "./http-client";
export interface IConfig {
  chunkingConfig?: any;
  retrievalConfig?: any;
}
export interface IAppStoreModel {
  config?: any;
  setConfig: Action<IAppStoreModel, any>;
  updateConfig: Thunk<IAppStoreModel>;

  storageIndexes?: any;
  setStorageIndexes: Action<IAppStoreModel, any>;
  updateStorageIndexes: Thunk<IAppStoreModel>;
}

export const storeModel: IAppStoreModel = {
  setConfig: action((state, payload) => {
    state.config = payload;
  }),
  updateConfig: thunk(async (actions) => {
    const config = await requestGetConfig();
    actions.setConfig(config);
  }),

  setStorageIndexes: action((state, payload) => {
    state.storageIndexes = payload;
  }),
  
  updateStorageIndexes: thunk(async (actions) => {
    const indexes = await requestStorageIndexes();
    actions.setStorageIndexes(indexes);
  }),
};

export const store = createStore(storeModel);
