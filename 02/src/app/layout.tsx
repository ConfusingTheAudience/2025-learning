import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Next Learning",
  description: "2025",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        
        <header className="w-full p-4 bg-gray-800 text-white text-center">
          --- HEADER ---
        </header>

        <main className="flex-grow flex justify-center items-center">
          {children}
        </main>
        
        <footer className="w-full p-4 bg-gray-800 text-white text-center">
          --- FOOTER ---
        </footer>

      </body>
    </html>
  );
}
