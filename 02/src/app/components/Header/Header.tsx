"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import React from "react";

const Header = () => {
  const pathname = usePathname();

  return (
    <header className="w-full p-4 bg-gray-800 text-white text-center">
      <div>
        {pathname === "/" ? (
          <>
            <Link
              href="/login"
              className="bg-green-400 text-white font-bold py-2 px-3 rounded mr-4 cursor-pointer hover:bg-blue-400"
            >
              Login
            </Link>
            <Link
              href="/register"
              className="bg-amber-500 text-white font-bold py-2 px-3 rounded cursor-pointer hover:bg-blue-400"
            >
              Register
            </Link>
          </>
        ) : (
          "--- HEADER ---"
        )}
      </div>
    </header>
  );
};

export default Header;

// usePathname used and use client directive
// Header with Login/Register is shown on main page, on sub pages it's only --- HEADER ---
