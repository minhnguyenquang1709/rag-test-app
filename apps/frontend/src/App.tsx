import { useEffect } from "react";
import { ChunkingComboboxContainer } from "./components/Chunking";
import { useStoreActions } from "easy-peasy";
import { IAppStoreModel, IConfig } from "./utils/store";
import FileUpload from "./components/FileUpload";

function App() {
  const updateConfig = useStoreActions<IAppStoreModel>(
    (actions) => actions.updateConfig
  );
  useEffect(() => {
    updateConfig();
  }, []);
  return (
    <div className="size-full">
      <div className="grid grid-cols-3">
        <ChunkingComboboxContainer />
        <FileUpload />
      </div>
    </div>
  );
}

export default App;
