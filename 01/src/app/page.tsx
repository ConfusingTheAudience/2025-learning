import { db } from "@/utils/db";
import React from "react";

const Home = async () => {
  const data = await db.user.findMany({
    select: {
      id: true,
      name: true,
    },
  });

  async function createUser(formData: FormData) {
    "use server";

    const input = formData.get("input") as string;
    await db.user.create({
      data: { name: input },
    });
  }

  async function deleteUser(formData: FormData) {
    "use server";

    const inputId = Number(formData.get("inputId"));

    if (isNaN(inputId)) {
      console.error("Invalid ID");
      return;
    }

    await db.user.delete({
      where: { id: inputId },
    });
  }

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

        <div className="space-y-3">
          {data.map((user) => (
            <div
              key={user.id}
              className="flex justify-between items-center mt-5 px-4 py-2 bg-blue-100 rounded-md shadow-sm"
            >
              <p className="text-blue-900 font-medium">{user.name}</p>
              <form>
                <input type="hidden" name="inputId" value={user.id} />
                <button
                  type="submit"
                  className="text-sm px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600 transition-colors cursor-pointer"
                  formAction={deleteUser}
                >
                  DELETE
                </button>
              </form>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Home;
