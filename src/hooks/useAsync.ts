import { useEffect, useRef, useState } from "react";

interface AsyncState<T> {
  data: T | null;
  error: string | null;
  loading: boolean;
}

export function useAsync<T>(load: () => Promise<T>, key = "default"): AsyncState<T> {
  const loadRef = useRef(load);
  const [state, setState] = useState<AsyncState<T>>({
    data: null,
    error: null,
    loading: true,
  });

  loadRef.current = load;

  useEffect(() => {
    let cancelled = false;
    setState((current) => ({ ...current, loading: true, error: null }));

    loadRef.current()
      .then((data) => {
        if (!cancelled) {
          setState({ data, error: null, loading: false });
        }
      })
      .catch((error: unknown) => {
        if (!cancelled) {
          setState({
            data: null,
            error: error instanceof Error ? error.message : "未知错误",
            loading: false,
          });
        }
      });

    return () => {
      cancelled = true;
    };
  }, [key]);

  return state;
}
