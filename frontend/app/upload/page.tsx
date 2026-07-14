"use client";

import { useState } from "react";
import { supabase } from "@/lib/supabase";

export default function UploadPage() {
  const [file, setFile] = useState<File | null>(null);
    async function handleUpload() {
  if (!file) return;

  const {
    data: { session },
  } = await supabase.auth.getSession();

  if (!session) {
    alert("Please login first.");
    return;
  }

  const filePath = `${session.user.id}/${Date.now()}-${file.name}`;

  const { error } = await supabase.storage
    .from("resumes")
    .upload(filePath, file);

  if (error) {
    alert(error.message);
    console.error(error);
    return;
  }

  alert("Resume uploaded successfully!");
}


  return (
    <main
      style={{
        display: "flex",
        flexDirection: "column",
        width: "400px",
        margin: "100px auto",
        gap: "20px",
      }}
    >
      <h1>Upload Resume</h1>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => {
          if (e.target.files?.[0]) {
            setFile(e.target.files[0]);
          }
        }}
      />

      {file && (
        <p>
          Selected: <strong>{file.name}</strong>
        </p>
      )}

     <button
       disabled={!file}
       onClick={handleUpload}
     >
      Upload Resume
     </button>

    </main>
  );
}