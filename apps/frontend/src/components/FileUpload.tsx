import React, { useState, useRef } from "react";
import { Button } from "./ui/button";
import { requestUploadFiles } from "../utils/http-client";

interface FileUploadProps {
  onUploadSuccess?: (response: any) => void;
  onUploadError?: (error: string) => void;
}

export const FileUpload: React.FC<FileUploadProps> = ({
  onUploadSuccess,
  onUploadError,
}) => {
  const [files, setFiles] = useState<File[]>([]);
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileSelect = (selectedFiles: FileList | null) => {
    if (!selectedFiles) return;
    const validFiles = Array.from(selectedFiles).filter(
      (file) => file.type === "text/plain" || file.type === "application/pdf"
    );
    setFiles((prev) => [...prev, ...validFiles]);
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    handleFileSelect(e.dataTransfer.files);
  };

  const handleImportClick = () => {
    fileInputRef.current?.click();
  };

  const handleSubmit = async () => {
    if (files.length === 0) return;
    const formData = new FormData();
    files.forEach((file) => formData.append("files", file));

    try {
      const response = await requestUploadFiles(formData);
      onUploadSuccess?.(response);
      setFiles([]);
    } catch (error: any) {
      onUploadError?.(error.message || "Upload failed");
    }
  };

  const removeFile = (index: number) => {
    setFiles((prev) => prev.filter((_, i) => i !== index));
  };

  return (
    <div className="size-full flex flex-col justify-start items-center border-solid border-2 rounded-2xl p-2">
      <div
        className={`drop-zone ${isDragging ? "dragging" : ""}`}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        style={{
          border: "2px dashed #ccc",
          padding: "20px",
          textAlign: "center",
          marginBottom: "10px",
        }}
      >
        Drag and drop files here or click Import
      </div>
      <Button variant={"default"} onClick={handleImportClick} className="hover:bg-gray-500">
        Import Files
      </Button>
      <input
        ref={fileInputRef}
        type="file"
        multiple
        accept=".txt,.pdf"
        style={{ display: "none" }}
        onChange={(e) => handleFileSelect(e.target.files)}
      />
      {files.length > 0 && (
        <div className="file-list" style={{ marginTop: "10px" }}>
          <h4>Selected Files:</h4>
          <ul>
            {files.map((file, index) => (
              <li key={index}>
                {file.name} ({(file.size / 1024).toFixed(2)} KB)
                <Button onClick={() => removeFile(index)} size="sm">
                  Remove
                </Button>
              </li>
            ))}
          </ul>
        </div>
      )}
      <Button onClick={handleSubmit} disabled={files.length === 0}>
        Submit to Backend
      </Button>
    </div>
  );
};

export default FileUpload;
