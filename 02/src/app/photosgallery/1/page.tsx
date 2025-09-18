import Link from "next/link";
import React from "react";

const FirstPhoto = () => {
  return <div className="text-center">
    <h1>First Photo</h1>
    <p>description: Lorem ipsum dolor sit amet.</p>
    <img src="/images/img1.jpg" alt="first image" className="w-100" />
    <Link href="/photosgallery" className="getBackBtn"> get back to photo gallery</Link>
  </div>;
};

export default FirstPhoto;
