"use client";

/**
 * Venue result card — shows name, why, watch-out, scores.
 */
export default function VenueCard({ venue, active, onClick }) {
    return (
        <div
            onClick={onClick}
            className={`cursor-pointer rounded-xl border p-4 backdrop-blur-md transition
        ${active
                    ? "border-violet-500 bg-violet-950/60"
                    : "border-zinc-700 bg-zinc-900/70 hover:border-zinc-500"
                }`}
        >
            <div className="flex items-start justify-between">
                <h3 className="font-semibold text-white text-sm">
                    #{venue.rank} {venue.name}
                </h3>
                {venue.vibe_score != null && (
                    <span className="text-xs text-violet-400">
                        vibe {Math.round(venue.vibe_score * 100)}%
                    </span>
                )}
            </div>

            <p className="mt-1 text-xs text-zinc-400">{venue.address}</p>

            {venue.why && (
                <p className="mt-2 text-xs text-emerald-400">✓ {venue.why}</p>
            )}
            {venue.watch_out && (
                <p className="mt-1 text-xs text-amber-400">⚠ {venue.watch_out}</p>
            )}
        </div>
    );
}
