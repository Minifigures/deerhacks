"use client";

import { useState } from "react";

/**
 * Floating search bar overlay.
 */
export default function SearchBar({ onSearch, loading }) {
    const [value, setValue] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (value.trim()) onSearch(value.trim());
    };

    return (
        <form
            onSubmit={handleSubmit}
            className="flex items-center gap-2 rounded-2xl bg-zinc-900/80 backdrop-blur-md border border-zinc-700 px-4 py-3 shadow-lg"
        >
            <input
                type="text"
                value={value}
                onChange={(e) => setValue(e.target.value)}
                placeholder="e.g. Basketball for 10 people, budget-friendly, west end"
                className="flex-1 bg-transparent outline-none text-sm text-white placeholder:text-zinc-500"
            />
            <button
                type="submit"
                disabled={loading}
                className="rounded-xl bg-violet-600 hover:bg-violet-500 transition px-4 py-2 text-sm font-medium text-white disabled:opacity-50"
            >
                {loading ? "Finding…" : "Go"}
            </button>
        </form>
    );
}
