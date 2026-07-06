{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3529cbc3-4c1a-4246-b50c-7e7feecc939d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ All libraries imported successfully!\n"
     ]
    }
   ],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import messagebox\n",
    "import sqlite3\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "print(\"✅ All libraries imported successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3055dd7d-22a4-45c2-8380-a36599baee44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Database connected successfully!\n",
      "✅ BMI table created successfully!\n"
     ]
    }
   ],
   "source": [
    "conn = sqlite3.connect(\"bmi_records.db\")\n",
    "cursor = conn.cursor()\n",
    "\n",
    "cursor.execute(\"\"\"\n",
    "CREATE TABLE IF NOT EXISTS bmi(\n",
    "    id INTEGER PRIMARY KEY AUTOINCREMENT,\n",
    "    name TEXT,\n",
    "    weight REAL,\n",
    "    height REAL,\n",
    "    bmi REAL,\n",
    "    category TEXT\n",
    ")\n",
    "\"\"\")\n",
    "\n",
    "conn.commit()\n",
    "\n",
    "cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name='bmi'\")\n",
    "if cursor.fetchone():\n",
    "    print(\"✅ Database connected successfully!\")\n",
    "    print(\"✅ BMI table created successfully!\")\n",
    "else:\n",
    "    print(\"❌ Table creation failed.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7df65172-c1e0-4282-a077-a0ad1ff5cd73",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Functions created successfully!\n"
     ]
    }
   ],
   "source": [
    "def calculate_bmi():\n",
    "    name = name_entry.get()\n",
    "\n",
    "    try:\n",
    "        weight = float(weight_entry.get())\n",
    "        height = float(height_entry.get())\n",
    "\n",
    "        if weight <= 0 or height <= 0:\n",
    "            raise ValueError\n",
    "\n",
    "        bmi = weight / (height ** 2)\n",
    "\n",
    "        if bmi < 18.5:\n",
    "            category = \"Underweight\"\n",
    "        elif bmi < 25:\n",
    "            category = \"Normal\"\n",
    "        elif bmi < 30:\n",
    "            category = \"Overweight\"\n",
    "        else:\n",
    "            category = \"Obese\"\n",
    "\n",
    "        result.config(text=f\"Name: {name}\\nBMI: {bmi:.2f}\\nCategory: {category}\")\n",
    "\n",
    "        cursor.execute(\n",
    "            \"INSERT INTO bmi(name, weight, height, bmi, category) VALUES (?, ?, ?, ?, ?)\",\n",
    "            (name, weight, height, bmi, category)\n",
    "        )\n",
    "        conn.commit()\n",
    "\n",
    "        messagebox.showinfo(\"Success\", \"Record Saved Successfully!\")\n",
    "\n",
    "    except:\n",
    "        messagebox.showerror(\"Error\", \"Enter valid values.\")\n",
    "\n",
    "\n",
    "def show_graph():\n",
    "    cursor.execute(\"SELECT bmi FROM bmi\")\n",
    "    data = cursor.fetchall()\n",
    "\n",
    "    if len(data) == 0:\n",
    "        messagebox.showinfo(\"Info\", \"No records found.\")\n",
    "        return\n",
    "\n",
    "    values = [row[0] for row in data]\n",
    "\n",
    "    plt.figure(figsize=(7,4))\n",
    "    plt.plot(values, marker=\"o\")\n",
    "    plt.title(\"BMI History\")\n",
    "    plt.xlabel(\"Record Number\")\n",
    "    plt.ylabel(\"BMI\")\n",
    "    plt.grid(True)\n",
    "    plt.show()\n",
    "\n",
    "print(\"✅ Functions created successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd75aaa0-87c4-49b4-97d8-a681041f8fb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "root = tk.Tk()\n",
    "root.title(\"BMI Calculator\")\n",
    "root.geometry(\"400x450\")\n",
    "\n",
    "tk.Label(root,\n",
    "         text=\"BMI Calculator\",\n",
    "         font=(\"Arial\",18,\"bold\")).pack(pady=10)\n",
    "\n",
    "tk.Label(root,text=\"Name\").pack()\n",
    "name_entry = tk.Entry(root)\n",
    "name_entry.pack()\n",
    "\n",
    "tk.Label(root,text=\"Weight (kg)\").pack()\n",
    "weight_entry = tk.Entry(root)\n",
    "weight_entry.pack()\n",
    "\n",
    "tk.Label(root,text=\"Height (m)\").pack()\n",
    "height_entry = tk.Entry(root)\n",
    "height_entry.pack()\n",
    "\n",
    "tk.Button(root,\n",
    "          text=\"Calculate BMI\",\n",
    "          command=calculate_bmi).pack(pady=10)\n",
    "\n",
    "tk.Button(root,\n",
    "          text=\"Show BMI Graph\",\n",
    "          command=show_graph).pack()\n",
    "\n",
    "result = tk.Label(root,\n",
    "                  text=\"\",\n",
    "                  font=(\"Arial\",12))\n",
    "result.pack(pady=10)\n",
    "\n",
    "print(\"✅ GUI started successfully!\")\n",
    "\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc41c18d-939f-4e79-9540-c6a96236acdc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0472b047-ebb1-4899-af12-ba9b4dbeaf93",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a72c446-e18a-4713-b65c-7386ad421a25",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
