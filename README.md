# YouTube Comment Labeling Application

A local Streamlit application for labeling YouTube comments based on video frames. This tool helps analyze and categorize comments with a simple, intuitive interface.

## 🎯 Features

- **CSV File Upload**: Load comments and videos data from CSV files
- **Smart Filtering**: Filter comments by video ID and optionally by frame
- **Interactive Labeling**: Assign labels (1, 2, or 3) to each comment using radio buttons
- **Progress Tracking**: See how many comments you've labeled in real-time
- **Resume Capability**: Continue from where you left off - previous labels are automatically loaded
- **Label Status Filter**: View all, only labeled, or only unlabeled comments
- **Data Export**: Save labeled data to a CSV file with all original columns plus the new label column

## 📋 Requirements

- Python 3.8 or higher
- Streamlit
- Pandas

## 🚀 Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install streamlit pandas
   ```

## 💻 How to Run

1. **Navigate to the project directory** in your terminal:
   ```bash
   cd /path/to/Python-Projects
   ```

2. **Run the Streamlit app**:
   ```bash
   streamlit run label_app.py
   ```

3. **The app will automatically open in your default browser** at `http://localhost:8501`

## 📊 CSV File Formats

### Comments CSV (File 1)
Your comments CSV file must contain at least these columns:
- `text_original`: The text of the YouTube comment
- `videoId`: The ID of the video the comment belongs to

Example:
```csv
videoId,text_original
video123,This is a great video!
video123,I learned a lot from this
video456,Nice content
```

### Videos CSV (File 2)
Your videos CSV file must contain:
- `videoId`: The video identifier
- `frame`: The frame category (1, 2, or 3)

Example:
```csv
videoId,frame
video123,1
video456,2
video789,3
```

## 📖 Usage Guide

### Step 1: Upload Files
1. Click on "Browse files" in the left sidebar under "Upload Comments CSV"
2. Select your comments CSV file
3. Click on "Browse files" under "Upload Videos CSV"
4. Select your videos CSV file

### Step 2: Select Video and Filters
1. Choose a video from the "Select Video ID" dropdown
2. (Optional) Check "Filter by Frame" to filter by specific frame numbers
3. (Optional) Use "Show comments" filter to view:
   - All comments
   - Unlabeled comments only
   - Labeled comments only

### Step 3: Label Comments
1. For each comment displayed, read the text
2. Select the appropriate label (1, 2, or 3) using the radio buttons
3. Labels are automatically stored as you select them

### Step 4: Save Your Work
1. Click the "💾 Save Labels" button at the bottom of the page
2. Your labeled data will be saved to `labeled_comments.csv` in the same directory
3. The file will include all original columns plus a new `label` column

### Step 5: Resume Labeling (Optional)
1. If you've previously saved labels, they will be automatically loaded when you restart the app
2. Previously labeled comments will show their existing labels
3. You can modify existing labels or continue labeling new comments

## 📁 Output File

The labeled data is saved to `labeled_comments.csv` in the same directory as the application. This file contains:
- All original columns from your comments CSV
- A new `label` column with your assigned labels (1, 2, or 3)

## 🔧 Tips

- **Progress Tracking**: The top of the page shows statistics including total comments, labeled count, unlabeled count, and overall progress percentage
- **Resume Work**: The app automatically loads previously saved labels from `labeled_comments.csv`, so you can continue where you left off
- **Filter Efficiently**: Use the label status filter to focus on unlabeled comments
- **Save Frequently**: Click the save button regularly to avoid losing your work

## 🐛 Troubleshooting

**Error: "Comments CSV must contain 'text_original' column"**
- Make sure your comments CSV has a column named exactly `text_original` (case-sensitive)

**Error: "Videos CSV must contain 'videoId' and 'frame' columns"**
- Ensure your videos CSV has both columns with the exact names (case-sensitive)

**No comments showing up**
- Check that the videoId in your comments CSV matches at least one videoId in your videos CSV
- Try changing the label status filter to "All"

**App not opening in browser**
- Manually navigate to http://localhost:8501
- Check if another application is using port 8501

## 📝 Example Workflow

Here's a typical workflow:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start the app
streamlit run label_app.py

# 3. In the browser:
#    - Upload comments.csv and videos.csv
#    - Select a video ID
#    - Label comments by selecting 1, 2, or 3
#    - Click "Save Labels"
#    - Continue with more videos or close the app

# 4. Find your results in labeled_comments.csv
```

## 🎓 Advanced Usage

### Working with Large Datasets
- Use the video ID filter to work on one video at a time
- Use the "Unlabeled Only" filter to focus on remaining work
- Save frequently to checkpoint your progress

### Modifying Existing Labels
- Load the app with existing `labeled_comments.csv` present
- Select the video you want to review
- Use "Labeled Only" filter to see previously labeled comments
- Change labels as needed and save again

## 📄 License

This project is part of the mkarpuz/Python-Projects repository.

## 🤝 Contributing

Feel free to submit issues or pull requests for improvements!

---

**Note**: This application runs entirely locally - no data is sent to any external servers or cloud services. All your data remains on your computer.
