import Link from "next/link";
import React from "react";

type Product = {
  id: number;
  title: string;
};

const Product = async () => {

  const res = await fetch("https://dummyjson.com/products?limit=15");
  const data = await res.json();
  const products: Product[] = data.products;

  return (
    <div className="flex flex-col items-center h-full">
      <h1 className="text-red-400">Product Page Fetch on Server (standard)</h1>
      <p>click on title to get to dynamic route</p>
      <Link href="/" className="getBackBtn"> get back to home</Link>

      <ul className="mt-4">
        {products.map((product) => (
            <li key={product.id} className="text-red-600 text-center font-bold bg-gray-900 p-4 rounded mb-2">
               <Link href={`/products/${product.id}`} key={product.id}>{product.title}</Link>
            </li>
        ))}
      </ul>
    </div>
  );
};

export default Product;

// server side fetching - we do not do it with getStaticProps() anymore (app folder doesn't support it)
// remeber to make async function
// need to use manually tailwind classes instead of box because of top screen cut
// Link should be in li not other way