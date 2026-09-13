import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "SLAJURY — Incident evidence chamber",
  description: "Evidence-backed SLA service-credit receipts with deterministic uptime calculations and GenLayer consensus.",
  icons: { icon: "/favicon.svg", shortcut: "/favicon.svg" },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body className="antialiased">{children}</body></html>;
}
