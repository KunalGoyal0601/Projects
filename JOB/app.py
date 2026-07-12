# app.py
# Simple Tkinter GUI for Resume-Based Job Recommendation System

import os
import tkinter as tk
from tkinter import filedialog, messagebox

from resume_parser import extract_text
from skill_extractor import extract_skills
from recommender import (
    load_dataset,
    build_tfidf_matrix,
    get_recommendations,
    get_missing_skills,
)
from classifier import train_classifier, predict_job_role


DATASET_PATH = os.path.join(os.path.dirname(__file__), "dataset.csv")


class ResumeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Job Recommender")
        self.root.geometry("950x650")

        self.selected_file = ""
        self.resume_text = ""

        self.load_models()
        self.create_widgets()

    def load_models(self):
        """Load dataset and train the machine learning models."""
        self.jobs_df = load_dataset(DATASET_PATH)
        self.vectorizer, self.tfidf_matrix = build_tfidf_matrix(self.jobs_df)
        self.classifier, self.label_encoder = train_classifier(self.jobs_df)

    def create_widgets(self):
        """Create all Tkinter widgets."""
        title = tk.Label(
            self.root,
            text="Resume-Based Job Recommendation System",
            font=("Arial", 18, "bold"),
        )
        title.pack(pady=10)

        top_frame = tk.Frame(self.root)
        top_frame.pack(fill="x", padx=20)

        self.file_label = tk.Label(top_frame, text="No resume selected", anchor="w")
        self.file_label.pack(side="left", fill="x", expand=True)

        browse_button = tk.Button(top_frame, text="Browse Resume", command=self.browse_file)
        browse_button.pack(side="left", padx=5)

        analyze_button = tk.Button(top_frame, text="Analyze", command=self.analyze_resume)
        analyze_button.pack(side="left", padx=5)

        clear_button = tk.Button(top_frame, text="Clear", command=self.clear_output)
        clear_button.pack(side="left", padx=5)

        self.status_label = tk.Label(
            self.root,
            text="Models loaded. Select a PDF or DOCX resume.",
            fg="green",
        )
        self.status_label.pack(pady=5)

        output_frame = tk.Frame(self.root)
        output_frame.pack(fill="both", expand=True, padx=20, pady=10)

        left_frame = tk.Frame(output_frame)
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))

        right_frame = tk.Frame(output_frame)
        right_frame.pack(side="left", fill="both", expand=True, padx=(5, 0))

        self.skills_box = self.create_text_section(left_frame, "Extracted Skills")
        self.role_box = self.create_text_section(left_frame, "Predicted Job Role")
        self.jobs_box = self.create_text_section(right_frame, "Recommended Jobs")
        self.missing_box = self.create_text_section(right_frame, "Missing Skills")

    def create_text_section(self, parent, heading):
        """Create one label and one text box."""
        label = tk.Label(parent, text=heading, font=("Arial", 11, "bold"))
        label.pack(anchor="w", pady=(5, 0))

        text_box = tk.Text(parent, height=10, wrap="word")
        text_box.pack(fill="both", expand=True, pady=(2, 8))
        text_box.config(state="disabled")

        return text_box

    def browse_file(self):
        """Open file dialog and save selected resume path."""
        file_path = filedialog.askopenfilename(
            title="Select Resume",
            filetypes=[
                ("Resume files", "*.pdf *.docx"),
                ("PDF files", "*.pdf"),
                ("Word files", "*.docx"),
            ],
        )

        if file_path:
            self.selected_file = file_path
            self.file_label.config(text=os.path.basename(file_path))
            self.status_label.config(text="Resume selected. Click Analyze.", fg="blue")

    def analyze_resume(self):
        """Extract resume text and show ML results."""
        if not self.selected_file:
            messagebox.showwarning("No file selected", "Please select a resume first.")
            return

        try:
            self.status_label.config(text="Analyzing resume...", fg="orange")
            self.root.update_idletasks()

            self.resume_text = extract_text(self.selected_file)
            skills = extract_skills(self.resume_text)

            recommended_jobs = get_recommendations(
                self.resume_text,
                self.jobs_df,
                self.vectorizer,
                self.tfidf_matrix,
                top_n=5,
            )

            role, confidence = predict_job_role(
                self.resume_text,
                self.classifier,
                self.label_encoder,
            )

            self.show_results(skills, recommended_jobs, role, confidence)
            self.status_label.config(text="Analysis complete.", fg="green")

        except Exception as error:
            messagebox.showerror("Error", str(error))
            self.status_label.config(text="Analysis failed.", fg="red")

    def show_results(self, skills, recommended_jobs, role, confidence):
        """Put the final output into the text boxes."""
        skills_text = "No skills found."
        if skills:
            skills_text = "\n".join(skills)

        role_text = f"Predicted role: {role}\nMatch score: {confidence:.2f}%"

        jobs_lines = []
        missing_lines = []

        for index, job in recommended_jobs.iterrows():
            number = index + 1
            title = job["Job Title"]
            job_role = job["Job Role"]
            score = job["similarity_pct"]

            jobs_lines.append(f"{number}. {title}")
            jobs_lines.append(f"   Role: {job_role}")
            jobs_lines.append(f"   Match score: {score}%")
            jobs_lines.append("")

            missing = get_missing_skills(skills, job["Skills"])
            missing_lines.append(f"{number}. {title}")

            if missing:
                missing_lines.append("   Missing: " + ", ".join(missing))
            else:
                missing_lines.append("   No missing skills found.")

            missing_lines.append("")

        self.write_text(self.skills_box, skills_text)
        self.write_text(self.role_box, role_text)
        self.write_text(self.jobs_box, "\n".join(jobs_lines))
        self.write_text(self.missing_box, "\n".join(missing_lines))

    def write_text(self, text_box, text):
        """Write text into a disabled Text widget."""
        text_box.config(state="normal")
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)
        text_box.config(state="disabled")

    def clear_output(self):
        """Clear selected file and all output boxes."""
        self.selected_file = ""
        self.resume_text = ""
        self.file_label.config(text="No resume selected")
        self.status_label.config(text="Select a PDF or DOCX resume.", fg="black")

        self.write_text(self.skills_box, "")
        self.write_text(self.role_box, "")
        self.write_text(self.jobs_box, "")
        self.write_text(self.missing_box, "")


if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeApp(root)
    root.mainloop()
