import tkinter as tk
from tkinter import messagebox

class MailApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mail Application")

        # Create UI components
        self.login_button = tk.Button(self, text="Login", command=self.show_login_screen)
        self.inbox_button = tk.Button(self, text="Inbox", command=self.show_inbox)
        self.compose_button = tk.Button(self, text="Compose", command=self.show_compose)
        self.search_button = tk.Button(self, text="Search", command=self.show_search_screen)
        self.folders_button = tk.Button(self, text="Folders", command=self.show_folders_screen)

        # Pack UI components
        self.login_button.pack()
        self.inbox_button.pack()
        self.compose_button.pack()
        self.search_button.pack()
        self.folders_button.pack()

        # Hide inbox, compose, search, and folders buttons initially
        self.inbox_button.pack_forget()
        self.compose_button.pack_forget()
        self.search_button.pack_forget()
        self.folders_button.pack_forget()

        # Variables to store email data
        self.emails = []

    def show_login_screen(self):
        # Create login screen
        login_screen = tk.Toplevel(self)
        login_screen.title("Login")

        email_label = tk.Label(login_screen, text="Email:")
        email_entry = tk.Entry(login_screen)
        password_label = tk.Label(login_screen, text="Password:")
        password_entry = tk.Entry(login_screen, show="*")
        login_button = tk.Button(login_screen, text="Login", command=lambda: self.login(email_entry.get(), password_entry.get()))

        # Pack login screen components
        email_label.pack()
        email_entry.pack()
        password_label.pack()
        password_entry.pack()
        login_button.pack()

    def login(self, email, password):
        # Perform authentication logic
        if email == "user@example.com" and password == "password":
            messagebox.showinfo("Login", "Login successful!")
            self.show_inbox_button()
        else:
            messagebox.showerror("Login", "Invalid email or password")

    def show_inbox_button(self):
        self.login_button.pack_forget()
        self.inbox_button.pack()
        self.compose_button.pack()
        self.search_button.pack()
        self.folders_button.pack()

    def show_inbox(self):
        # Clear any existing email widgets
        self.clear_email_widgets()

        # Logic to fetch inbox emails
        self.emails = self.fetch_inbox_emails()

        # Create inbox screen
        inbox_screen = tk.Toplevel(self)
        inbox_screen.title("Inbox")

        # Create email widgets for each email
        for email in self.emails:
            email_frame = tk.Frame(inbox_screen)
            sender_label = tk.Label(email_frame, text="From: " + email.sender)
            subject_label = tk.Label(email_frame, text="Subject: " + email.subject)
            content_label = tk.Label(email_frame, text=email.content)
            reply_button = tk.Button(email_frame, text="Reply", command=lambda email=email: self.reply_email(email))

            # Pack email widgets
            sender_label.pack(anchor="w")
            subject_label.pack(anchor="w")
            content_label.pack(anchor="w")
            reply_button.pack(anchor="e")

            email_frame.pack(padx=10, pady=10)

    def fetch_inbox_emails(self):
        # Logic to fetch and return inbox emails
        return [
            Email("sender1@example.com", "Hello", "This is the first email"),
            Email("sender2@example.com", "Greetings", "This is the second email"),
            Email("sender3@example.com", "Important Notice", "This is the third email"),
        ]

    def reply_email(self, email):
        # Create reply mail screen with pre-filled recipient and subject
        reply_screen = tk.Toplevel(self)
        reply_screen.title("Reply")

        recipient_label = tk.Label(reply_screen, text="Recipient:")
        recipient_entry = tk.Entry(reply_screen)
        recipient_entry.insert(tk.END, email.sender)
        subject_label = tk.Label(reply_screen, text="Subject:")
        subject_entry = tk.Entry(reply_screen)
        subject_entry.insert(tk.END, "Re: " + email.subject)
        content_label = tk.Label(reply_screen, text="Content:")
        content_entry = tk.Text(reply_screen)
        reply_button = tk.Button(reply_screen, text="Send", command=lambda: self.send_mail(recipient_entry.get(), subject_entry.get(), content_entry.get("1.0", tk.END)))

        # Pack reply mail screen components
        recipient_label.pack()
        recipient_entry.pack()
        subject_label.pack()
        subject_entry.pack()
        content_label.pack()
        content_entry.pack()
        reply_button.pack()

    def show_compose(self):
        # Create compose mail screen
        compose_screen = tk.Toplevel(self)
        compose_screen.title("Compose Mail")

        recipient_label = tk.Label(compose_screen, text="Recipient:")
        recipient_entry = tk.Entry(compose_screen)
        subject_label = tk.Label(compose_screen, text="Subject:")
        subject_entry = tk.Entry(compose_screen)
        content_label = tk.Label(compose_screen, text="Content:")
        content_entry = tk.Text(compose_screen)
        send_button = tk.Button(compose_screen, text="Send", command=lambda: self.send_mail(recipient_entry.get(), subject_entry.get(), content_entry.get("1.0", tk.END)))

        # Pack compose mail screen components
        recipient_label.pack()
        recipient_entry.pack()
        subject_label.pack()
        subject_entry.pack()
        content_label.pack()
        content_entry.pack()
        send_button.pack()

    def send_mail(self, recipient, subject, content):
        # Logic to send the composed email
        messagebox.showinfo("Compose Mail", "Mail sent successfully!")

    def show_search_screen(self):
        # Create search screen
        search_screen = tk.Toplevel(self)
        search_screen.title("Search")

        search_label = tk.Label(search_screen, text="Search:")
        search_entry = tk.Entry(search_screen)
        search_button = tk.Button(search_screen, text="Search", command=lambda: self.search_emails(search_entry.get()))

        # Pack search screen components
        search_label.pack()
        search_entry.pack()
        search_button.pack()

    def search_emails(self, keyword):
        # Logic to search and display emails based on the given keyword
        messagebox.showinfo("Search", f"Searching emails for: {keyword}")

    def show_folders_screen(self):
        # Create folders screen
        folders_screen = tk.Toplevel(self)
        folders_screen.title("Folders")

        # Logic to fetch and display folders
        folders = self.fetch_folders()

        # Create folder widgets
        for folder in folders:
            folder_label = tk.Label(folders_screen, text=folder)
            folder_label.pack()

    def fetch_folders(self):
        # Logic to fetch and return folder names
        return ["Inbox", "Sent", "Drafts", "Spam", "Trash"]

    def clear_email_widgets(self):
        # Clear email widgets from the inbox screen
        for widget in self.winfo_children():
            if isinstance(widget, tk.Toplevel) and widget.winfo_exists():
                widget.destroy()

class Email:
    def __init__(self, sender, subject, content):
        self.sender = sender
        self.subject = subject
        self.content = content

if __name__ == "__main__":
    app = MailApplication()
    app.mainloop()