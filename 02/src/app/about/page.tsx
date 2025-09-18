"use client";

import { useRouter } from "next/navigation";
import React from "react";

const About = () => {
  const router = useRouter();

  const backToHome = () => {
    router.push("/");
  };

  return (
    <div className="box">
      <h1 className="text-lime-400">About Page</h1>
      <button onClick={backToHome} className="getBackBtn">get back to home</button>
    </div>
  );
};

export default About;

// useRouter means I need to make client component