import { IAppStoreModel, IConfig } from "@/utils/store";
import { useStoreState } from "easy-peasy";
import { useEffect, useState } from "react";
import { Popover, PopoverContent, PopoverTrigger } from "./ui/popover";
import { Button } from "./ui/button";
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "./ui/command";
import { Check, ChevronsUpDown } from "lucide-react";
import { cn } from "@/lib/utils";

export const ChunkingComboboxContainer = () => {
  const config = useStoreState<IAppStoreModel, IConfig>(
    (state) => state.config
  );
  const [chunkingStrategies, setChunkingStrategies] = useState<any[]>([]);

  /**Combobox */
  const [open, setOpen] = useState(false);
  const [value, setValue] = useState("");

  useEffect(() => {
    if (!config?.chunkingConfig) {
      return;
    }
    console.log("chunking config exists");
    setChunkingStrategies(config.chunkingConfig);
  }, [config]);
  if (!chunkingStrategies) {
    return <div>Loading...</div>;
  }
  return (
    <div className="size-full flex flex-col justify-start items-center border-solid border-2 rounded-2xl p-2">
      <Popover open={open} onOpenChange={setOpen}>
        <PopoverTrigger asChild>
          <Button
            variant="outline"
            role="combobox"
            aria-expanded={open}
            className="w-full justify-between overflow-x-clip"
          >
            {value
              ? chunkingStrategies.find((strategy: any) => strategy.id == value)
                  ?.name
              : "Select Chunking Strategy..."}
            <ChevronsUpDown className="opacity-50" />
          </Button>
        </PopoverTrigger>
        <PopoverContent className="w-full p-0">
          <Command>
            <CommandInput
              placeholder="Search chunking strategy..."
              className="h-9"
            />
            <CommandList>
              <CommandEmpty>No chunking strategy found.</CommandEmpty>
              <CommandGroup className=" contrast-150">
                {chunkingStrategies.map((strategy: any) => (
                  <CommandItem
                    key={strategy.id}
                    value={strategy.id}
                    onSelect={(currentId) => {
                      setValue(currentId === value ? "" : currentId);
                      setOpen(false);
                    }}
                    className=""
                  >
                    {strategy.name}
                    <Check
                      className={cn(
                        "ml-auto",
                        value === strategy.id ? "opacity-100" : "opacity-0"
                      )}
                    />
                  </CommandItem>
                ))}
              </CommandGroup>
            </CommandList>
          </Command>
        </PopoverContent>
      </Popover>
    </div>
  );
};
