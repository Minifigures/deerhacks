"use client";

import { useRef, useEffect } from "react";
import mapboxgl from "mapbox-gl";
import "mapbox-gl/dist/mapbox-gl.css";

mapboxgl.accessToken = process.env.NEXT_PUBLIC_MAPBOX_TOKEN || "";

/**
 * Interactive Mapbox canvas.
 * Renders venue pins + isochrone overlays.
 */
export default function Map({ venues = [], onSelectVenue }) {
    const containerRef = useRef(null);
    const mapRef = useRef(null);

    // Initialise map once
    useEffect(() => {
        if (mapRef.current) return;
        mapRef.current = new mapboxgl.Map({
            container: containerRef.current,
            style: "mapbox://styles/mapbox/dark-v11",
            center: [-79.3832, 43.6532], // Toronto default
            zoom: 12,
        });

        mapRef.current.addControl(new mapboxgl.NavigationControl(), "bottom-right");
    }, []);

    // Update pins when venues change
    useEffect(() => {
        const map = mapRef.current;
        if (!map || !venues.length) return;

        // Clear old markers (simple approach)
        document.querySelectorAll(".pf-marker").forEach((el) => el.remove());

        venues.forEach((v) => {
            const el = document.createElement("div");
            el.className = "pf-marker";
            el.style.cssText =
                "width:28px;height:28px;border-radius:50%;background:#7c3aed;border:2px solid #fff;cursor:pointer;";

            new mapboxgl.Marker(el).setLngLat([v.lng, v.lat]).addTo(map);

            el.addEventListener("click", () => onSelectVenue?.(v));
        });

        // Fit bounds
        const bounds = new mapboxgl.LngLatBounds();
        venues.forEach((v) => bounds.extend([v.lng, v.lat]));
        map.fitBounds(bounds, { padding: 80 });
    }, [venues, onSelectVenue]);

    return <div ref={containerRef} className="absolute inset-0" />;
}
