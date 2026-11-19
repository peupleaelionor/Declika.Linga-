declare module "nitro/storage" {
  export function useStorage(base?: string): {
    getItem(key: string): Promise<unknown>;
    getItemRaw(key: string): Promise<Uint8Array | Buffer | string | null>;
  };
}

