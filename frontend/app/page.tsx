import Link from "next/link";

export default function Home() {
  return (
    <main
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
        gap: "20px",
      }}
    >
      <h1>HireReady AI</h1>
      <p>Your AI Career Coach</p>

      <Link href="/signup">
        Create Account
      </Link>

      <Link href="/login">
        Login
      </Link>
    </main>
  );
}