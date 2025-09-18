// app/products/page.tsx
import Link from "next/link";
import { use } from "react";

type Product = {
  id: number;
  title: string;
};

async function getProducts(): Promise<Product[]> {
  const res = await fetch("https://dummyjson.com/products?limit=15");
  const data = await res.json();
  return data.products;
}

const ProductPage = () => {
  const products = use(getProducts());

  return (
    <div className="flex flex-col items-center h-full">
      <h1 className="text-red-400">Products Page Fetch on Server with use()</h1>
      <Link href="/" className="getBackBtn"> get back to home</Link>
      
      <ul className="mt-4">
        {products.map(product => (
          <li key={product.id} className="text-red-600 text-center font-bold bg-gray-900 p-4 rounded mb-2">{product.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default ProductPage;

// server side fetching
// use() only works in Server Components (so you can't have "use client" at the top of the file)
// you must import use from "react"
// need to use manually tailwind classes instead of box because of top screen cut
