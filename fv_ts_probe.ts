// FV TS-tier probe (safe to delete). Exercises graphify's TypeScript verify tier.
export function classify(n: number): string {
  if (n > 0) {
    return "positive";
  } else {
    return "non-positive";
  }
}
