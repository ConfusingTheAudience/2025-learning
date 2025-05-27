import { db } from "@/utils/db";
import React from "react";

async function createUser(formData: FormData) {
  "use server";

  const input = formData.get("input") as string;
  await db.user.create({
    data: { name: input },
  });
}

const Home = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-blue-50">
      <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
        <form action={createUser} className="flex flex-col sm:flex-row gap-4">
          <input
            type="text"
            name="input"
            placeholder="Add new User..."
            className="flex-1 px-4 py-2 border border-blue-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
          <button
            type="submit"
            className="px-6 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 transition-colors cursor-pointer"
          >
            Add User
          </button>
        </form>
      </div>
    </div>
  );
};

export default Home;
