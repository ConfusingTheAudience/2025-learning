"use server";

import { db } from "@/utils/db";

export async function createUser(formData: FormData) {

  const input = formData.get("input") as string;
  await db.user.create({
    data: { name: input },
  });
}

export async function deleteUser(formData: FormData) {

  const inputId = Number(formData.get("inputId"));

  if (isNaN(inputId)) {
    console.error("Invalid ID");
    return;
  }

  await db.user.delete({
    where: { id: inputId },
  });
}
