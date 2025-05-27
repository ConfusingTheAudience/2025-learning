# NextJS with Prisma
Prisma implementation to NextJS and basic functionality

<br />
<br />

## Commands to begin
```bash
1. npx create-next-app@latest [foldername]
```
```bash
2. cd [foldername] (if we aren't inside)
```
```bash
3. npm i -D prisma
```
```bash
4. npx prisma init --datasource-provider [sqlite] (sqlite or other db)
```
```diff
+ 5. Add model to prisma/schema.prisma
```
```bash
6. npx prisma migrate dev --name init
```
```diff
+ 7. Create utils/db.ts with code inside it

 import { PrismaClient } from "../generated/prisma";
 export const db = new PrismaClient();
```
```diff
+ 8. Start usage of prisma in page.ts
```

<br />

## Prisma most useful commands
```bash
npx prisma format - to format code
```
```bash
npx prisma studio - to open studio for db
```
```bash
npx prisma migrate dev --name [what-we-did] - to any changes made after first migrate in schema.prisma
```

## Prisma snippets
**schema.prisma - model**
```prisma
model User {
  id          Int        @id @default(autoincrement())
  name        String
  email       String?
  createdAt   DateTime   @default(now())
  updatedAt   DateTime   @updatedAt
}
```
**Add record/s**
```prisma
const user = await prisma.user.create({
    data: {
      name: 'Ariadne',
      email: 'ariadne@prisma.io',
    },
})
```
```prisma
const createManyUsers = await prisma.user.createMany({
    data: [
      { name: 'Bob', email: 'bob@prisma.io' },
      { name: 'Yewande', email: 'yewande@prisma.io' },
      { name: 'Angelique', email: 'angelique@prisma.io' },
    ]
})
```
**Add record by form**
```prisma
async function createUser(formData: FormData) {
    "use server";

    const inputName = formData.get("inputName") as string;
    await db.user.create({
      data: { name: inputName },
    });
  }
```
**Get record/s**
```prisma
const users = await prisma.user.findMany()
```
```prisma
const user = await prisma.user.findUnique({
  where: {
    email: 'ariadne@prisma.io',
  },
})
```
**Update record/s**
```prisma
const updateUser = await prisma.user.update({
  where: {
    email: 'viola@prisma.io',
  },
  data: {
    name: 'Viola the Magnificent',
  },
})
```
```prisma
const updateUsers = await prisma.user.updateMany({
  where: {
    email: {
      contains: 'prisma.io',
    },
  },
  data: {
    role: 'ADMIN',
  },
})
```
**Delete record/s**
```prisma
const deleteUser = await prisma.user.delete({
  where: {
    email: 'bert@prisma.io',
  },
})
```
```prisma
const deleteUsers = await prisma.user.deleteMany({
  where: {
    email: {
      contains: 'prisma.io',
    },
  },
})
```
**Delete all records**
```prisma
const deleteUsers = await prisma.user.deleteMany({})
```

<br />

**Optional chain to add at the bottom of new PrismaClient**
```prisma
main()
  .then(async () => {
    await prisma.$disconnect();
  })
  .catch(async (e) => {
    console.error(e);
    await prisma.$disconnect();
    process.exit(1);
  });
```

## Information
useful to remember
<br />

`name of input is important! <input name="myData">`
<br />

`two ways of get data from form: <form action={functionToUse}> or <button formAction={functionToUse}`
<br />

`I can use formAction in a button, but it has to be in a <form>`
<br />

`formAction from <button> overwrites the action from <form>`
<br />

`You can have multiple buttons in one <form>, each with a different formAction`
<br />

`On server we need to use "use server"; after every start of function (like in the example with Add record by form)`
<br />
