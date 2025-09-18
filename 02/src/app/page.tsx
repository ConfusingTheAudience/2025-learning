import Link from "next/link";

export default function Home() {
  return (
    <div className="box">
        <h1>Home Page</h1>
        <Link href="/about" className="text-white hover:text-blue-500 transition-colors duration-200">About Page</Link>
        <Link href="/products" className="text-white hover:text-blue-500 transition-colors duration-200 mt-4">Product First Page</Link>
        <Link href="/products2" className="text-white hover:text-blue-500 transition-colors duration-200">Product Second Page</Link>
        <Link href="/products3" className="text-white hover:text-blue-500 transition-colors duration-200 mb-4">Product Third Page</Link>
    </div>
  );
}

// basic Link usage
