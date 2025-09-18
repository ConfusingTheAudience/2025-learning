import Link from "next/link";
import React from "react";

const Photos = () => {
  return (
  <div className="flex flex-col items-center h-full">
    <h1 className="text-orange-400">Photos Gallery</h1>
    <p>if you press on first image and refresh you will see intercepting route</p>
    <Link href="/" className="getBackBtn"> get back to home</Link>
    <div className="flex pt-4 pb-4">
        <Link href="photosgallery/1"><img src="/images/img1.jpg" alt="first image" className="m-4 w-80" /></Link>
        <img src="/images/img2.jpg" alt="second image" className="m-4 w-80" />
        <img src="/images/img3.jpg" alt="third image" className="m-4 w-80" />
    </div>
  </div>
  )
};

export default Photos;

// Photos from:
// https://www.pexels.com/pl-pl/zdjecie/grey-trunk-green-leaf-tree-obok-zbiornika-wodnego-762679/
// https://www.pexels.com/pl-pl/zdjecie/kosmos-przestrzen-kurz-pyl-6307488/
// https://www.pexels.com/pl-pl/zdjecie/domy-w-miescie-zima-311066/

// intercepting route (.)1 used to show modal