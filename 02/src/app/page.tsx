import Link from "next/link";

export default function Home() {
  return (
    <div className="box">
        <h1>Home Page</h1>
        <Link href="/about" className="text-white hover:text-blue-500 transition-colors duration-200">About Page</Link>
    </div>
  );
}

// basic Link usage
