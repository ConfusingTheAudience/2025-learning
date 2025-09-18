import React from "react";
import Link from "next/link";
import { notFound } from "next/navigation";

type Product = {
  id: number;
  title: string;
  description: string;
  thumbnail: string
};

const SpecificProduct = async ({ params }: { params: { id: string } }) => {
  const res = await fetch(`https://dummyjson.com/products/${params.id}`);
  const product: Product = await res.json();

  const allowedId = Number(params.id); // I'm working with string so I need to convert it to number

  if (isNaN(allowedId) || allowedId < 1 || allowedId > 15) {
    notFound();
  }

  if (!res.ok) {
    notFound();
  }

  return (
    <div className="box">
      <h1 className="text-2xl font-bold text-lime-400">
        Product: {product.title}
      </h1>
      <p className="mt-2 text-gray-300">ID: {product.id}</p>
      <p className="mb-4">Description: {product.description}</p>
      <img 
        src={product.thumbnail} 
        alt={product.title} 
        className="h-48 object-cover mb-2 rounded"
       />
      <Link href="/products" className="getBackBtn"> get back to products</Link>
    </div>
  );
};

export default SpecificProduct;

// dynamic routes
// remember it is async function
// params only take what is in URL so only id of fe 1 - /products/1
// if I want aslo show the title of picked element I need to do it with fetch specific item by mine id I get (remember that id could start from 0 this time it doesn't)

// notFound function to detect if product exist (so use can't manually type url and get to product that doesn't exist)
// added if statement for manually go to url by user (not allowed for the one product that aren't showed in /products)
