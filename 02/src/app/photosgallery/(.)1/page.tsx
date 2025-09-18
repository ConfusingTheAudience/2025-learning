import React from "react";
import Photos from "../page"; // Komponent galerii
import Link from "next/link";

const FirstPhotoIntercepting = () => {
  return (
    <div className="relative">
      <div className="opacity-30 pointer-events-none">
        <Photos />
      </div>

      <div className="fixed inset-0 flex items-center justify-center z-50">
        <div className="relative">
          <Link
            href="/photosgallery"
            className="absolute top-4 right-4 bg-blue-400 text-white w-10 h-10 flex items-center justify-center rounded-full hover:bg-gray-800"
          >
            X
          </Link>

          <img
            src="/images/img1.jpg"
            alt="first image"
            className="rounded-lg shadow-lg"
          />
        </div>
      </div>
    </div>
  );
};

export default FirstPhotoIntercepting;
