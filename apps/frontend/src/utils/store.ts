import { Action, Thunk, action, createStore, thunk } from "easy-peasy";
import { requestGetConfig } from "./http-client";
export interface IConfig {
  chunkingConfig?: any;
  retrievalConfig?: any;
}
export interface IAppStoreModel {
  config?: any;
  setConfig: Action<IAppStoreModel, any>;
  updateConfig: Thunk<IAppStoreModel>;
}

export const storeModel: IAppStoreModel = {
  setConfig: action((state, payload) => {
    state.config = payload;
  }),
  updateConfig: thunk(async (actions) => {
    const config = await requestGetConfig();
    actions.setConfig(config);
  }),
};

export const store = createStore(storeModel);
