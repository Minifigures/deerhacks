"use client";

import { useState } from "react";
import SearchBar from "@/components/SearchBar";
import Map from "@/components/Map";
import VenueCard from "@/components/VenueCard";
import { createPlan } from "@/lib/api";

export default function Home() {
    const [venues, setVenues] = useState([]);
    const [loading, setLoading] = useState(false);
    const [selectedVenue, setSelectedVenue] = useState(null);

    const handleSearch = async (prompt) => {
        setLoading(true);
        try {
            const data = await createPlan({ prompt });
            setVenues(data.venues || []);
        } catch (err) {
            console.error("Plan request failed:", err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <main className="relative h-screen w-screen overflow-hidden">
            {/* Map canvas — full bleed */}
            <Map venues={venues} onSelectVenue={setSelectedVenue} />

            {/* Search overlay */}
            <div className="absolute top-6 left-1/2 -translate-x-1/2 z-10 w-full max-w-xl px-4">
                <SearchBar onSearch={handleSearch} loading={loading} />
            </div>

            {/* Venue cards sidebar */}
            {venues.length > 0 && (
                <aside className="absolute top-24 right-4 z-10 w-80 space-y-3 max-h-[calc(100vh-8rem)] overflow-y-auto">
                    {venues.map((v) => (
                        <VenueCard
                            key={v.rank}
                            venue={v}
                            active={selectedVenue?.rank === v.rank}
                            onClick={() => setSelectedVenue(v)}
                        />
                    ))}
                </aside>
            )}
        </main>
    );
}
