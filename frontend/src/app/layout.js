import "./globals.css";

export const metadata = {
    title: "PATHFINDER",
    description:
        "Intelligent, vibe-aware group activity and venue planning with predictive risk analysis.",
};

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body>{children}</body>
        </html>
    );
}
