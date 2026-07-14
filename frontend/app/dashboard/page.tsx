"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";

export default function DashboardPage() {
  const router = useRouter();

  useEffect(() => {
  async function checkUser() {
    const {
      data: { session },
    } = await supabase.auth.getSession();

    console.log("SESSION:", session);

    if (!session) {
      console.log("No session found");
      router.push("/login");
    } else {
      console.log("User:", session.user.email);
    }
  }

  checkUser();
}, [router]);

  return (
    <main
    style={{
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      height: "100vh",
      flexDirection: "column",
      gap: "20px",
    }}
  >
    <h1>🎉 Welcome to HireReady AI</h1>

    <p>You are logged in.</p>

    <button onClick={() => router.push("/upload")}>
      Upload Resume
    </button>

    <button
      onClick={async () => {
        await supabase.auth.signOut();
        router.push("/login");
      }}
    >
      Logout
    </button>
  </main>
  );
}