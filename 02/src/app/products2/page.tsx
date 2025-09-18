"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

type Product = {
  id: number;
  title: string;
  thumbnail: string
};

type ProductResponse = {
  products: Product[];
};

const ProductList = () => {
  const [products, setProducts] = useState<Product[]>([]);

  useEffect(() => {
    fetch("https://dummyjson.com/products?limit=15")
      .then((res) => res.json())
      .then((data: ProductResponse) => setProducts(data.products));
  }, []);

  return (
    <div className="flex flex-col items-center h-full">
      <h1 className="text-red-400">Product Page Fetch on Client</h1>
      <Link href="/" className="getBackBtn"> get back to home </Link>
      <ul className="mt-4">
        {products.map((product) => (
          <li key={product.id} className="text-red-600 text-center font-bold bg-gray-900 p-4 rounded mb-2"> 
            <img 
              src={product.thumbnail} 
              alt={product.title} 
              className="w-full h-48 object-cover mb-2 rounded"
            />
            <h2>{product.title}</h2>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;


// client side fetching
// standard use of useEffect and useState as on react
// need to use manually tailwind classes instead of box because of top screen cut
