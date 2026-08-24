# S3 in-class activity — four changes, one repository

Your team has its own copy of this repository. Everyone works on the same codebase
at the same time, which is the point.

## Ground rules

1. **Everyone branches from `main` now**, at the same moment, before anyone starts typing.
   `git switch -c <your-branch-name>`
2. **Do not pull from `main` again until you are told to.** No shortcuts here — the
   whole exercise depends on all four branches starting from the same commit.
3. **Every change reaches `main` through a pull request.** Nobody pushes to `main`
   directly; your repository is configured to refuse it.
4. **When you hit a merge conflict, resolve it in your editor.** Not with GitHub's
   web "Resolve conflicts" button, and **not with an AI agent.** You will get to
   compare against both later; today you do it by hand.
5. **After every merge into `main`, run the app and click through every cafe,
   every menu, the cart and checkout.** Every time. Yes, even when the merge was clean.

Commit as you go, with messages someone else could read.

---

## Card A — Add a fourth cafe

The app ships with three cafes. Add a fourth.

- Name it **Cafe Four**, serving **Idli**, **Dosa** and **Filter Coffee**.
- It must appear on the home page and its menu page must work like the others.

## Card B — Show prices

Right now a menu is just a list of names, and a customer has no idea what anything costs.

- Give every item on every menu a price in rupees.
- Show the price next to each item on the cafe page.
- Pick sensible campus-canteen prices; there is no price list to work from.

## Card C — Cart total and remove-item

The cart lists what you picked and nothing else.

- Show a **total** at the bottom of the cart.
- Let a customer **remove a single item** from the cart without clearing the whole thing.

> Card C depends on Card B having prices to add up. Decide as a team how you want to
> handle that — it is a real question, not a trick.

## Card D — Navigation and order history

- Show the **number of items currently in the cart** in the navigation bar on every page.
- Add an **`/orders` page** listing previous completed orders, and make checkout record
  an order there instead of silently discarding the cart.

---

## Teams of three

Take **A**, **B** and **D**. Leave C.

## When all four branches are done

Open a pull request for each one. Then merge them into `main` **one at a time**,
running the app after each merge, and see what happens.
