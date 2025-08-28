import { IAppStoreModel, IConfig } from "@/utils/store";
import { useStoreState } from "easy-peasy";
import { useEffect } from "react";

export const RetrievalComboboxContainer = () => {
  const config = useStoreState<IAppStoreModel, IConfig>(
    (state) => state.config
  );
  useEffect(() => {
    if (!config?.retrievalConfig) {
      return;
    }
    console.log("retrieval config:", config.retrievalConfig);
  }, [config]);
  if (!config.retrievalConfig) {
    return <div>Loading...</div>;
  }
  return (
    <div className="size-full flex flex-col justify-start items-center"></div>
  );
};
