"""
YouTube Comment Labeling Application
======================================

A local Streamlit application for labeling YouTube comments based on video frames.

This app allows you to:
1. Upload two CSV files (comments and videos)
2. Filter comments by videoId and frame
3. Label each comment with a numeric value (1, 2, or 3)
4. Save the labeled data to a CSV file
5. Resume previous labeling sessions

Author: Created for mkarpuz/Python-Projects
Date: 2025
"""

import streamlit as st
import pandas as pd
import os
from typing import Optional

# Page configuration
st.set_page_config(
    page_title="YouTube Comment Labeler",
    page_icon="🏷️",
    layout="wide"
)

# Constants
LABEL_OPTIONS = [1, 2, 3]
OUTPUT_FILE = "labeled_comments.csv"


def load_csv_file(uploaded_file) -> Optional[pd.DataFrame]:
    """
    Load a CSV file from Streamlit file uploader.
    
    Args:
        uploaded_file: Streamlit UploadedFile object
    
    Returns:
        DataFrame if successful, None otherwise
    """
    try:
        df = pd.read_csv(uploaded_file)
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None


def load_existing_labels() -> Optional[pd.DataFrame]:
    """
    Load existing labeled data if the output file exists.
    
    Returns:
        DataFrame with existing labels or None if file doesn't exist
    """
    if os.path.exists(OUTPUT_FILE):
        try:
            df = pd.read_csv(OUTPUT_FILE)
            return df
        except Exception as e:
            st.warning(f"Could not load existing labels: {e}")
            return None
    return None


def save_labeled_data(df: pd.DataFrame) -> bool:
    """
    Save the labeled data to a CSV file.
    
    Args:
        df: DataFrame containing labeled comments
    
    Returns:
        True if successful, False otherwise
    """
    try:
        df.to_csv(OUTPUT_FILE, index=False)
        return True
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return False


def get_video_ids(videos_df: pd.DataFrame) -> list:
    """
    Extract unique video IDs from the videos DataFrame.
    
    Args:
        videos_df: DataFrame containing video information
    
    Returns:
        List of unique video IDs
    """
    if 'videoId' in videos_df.columns:
        return sorted(videos_df['videoId'].unique().tolist())
    return []


def get_frames(videos_df: pd.DataFrame) -> list:
    """
    Extract unique frames from the videos DataFrame.
    
    Args:
        videos_df: DataFrame containing video information
    
    Returns:
        List of unique frames
    """
    if 'frame' in videos_df.columns:
        return sorted(videos_df['frame'].unique().tolist())
    return []


def filter_comments(comments_df: pd.DataFrame, video_id: str, 
                   videos_df: Optional[pd.DataFrame] = None, 
                   frame: Optional[int] = None) -> pd.DataFrame:
    """
    Filter comments by video ID and optionally by frame.
    
    Args:
        comments_df: DataFrame containing comments
        video_id: Video ID to filter by
        videos_df: DataFrame containing video information (optional)
        frame: Frame number to filter by (optional)
    
    Returns:
        Filtered DataFrame
    """
    # Filter by video ID
    filtered = comments_df[comments_df['videoId'] == video_id].copy()
    
    # If frame filter is specified and videos_df is provided
    if frame is not None and videos_df is not None:
        # Get video IDs that match the selected frame
        matching_videos = videos_df[videos_df['frame'] == frame]['videoId'].unique()
        # Further filter comments to only those videos
        filtered = filtered[filtered['videoId'].isin(matching_videos)]
    
    return filtered


def merge_with_existing_labels(comments_df: pd.DataFrame, 
                               existing_labels: Optional[pd.DataFrame]) -> pd.DataFrame:
    """
    Merge current comments with existing labels if available.
    
    Args:
        comments_df: DataFrame containing comments to label
        existing_labels: DataFrame containing previously labeled data
    
    Returns:
        Merged DataFrame with existing labels
    """
    if existing_labels is None or existing_labels.empty:
        # Add empty label column
        comments_df['label'] = None
        return comments_df
    
    # Create a unique identifier for merging (assuming we can use all original columns)
    # For simplicity, we'll try to match on text_original and videoId if both exist
    if 'text_original' in comments_df.columns and 'text_original' in existing_labels.columns:
        # Merge on text_original and videoId to preserve existing labels
        result = comments_df.merge(
            existing_labels[['text_original', 'videoId', 'label']],
            on=['text_original', 'videoId'],
            how='left',
            suffixes=('', '_existing')
        )
        return result
    else:
        comments_df['label'] = None
        return comments_df


def main():
    """Main application function."""
    
    # Title and description
    st.title("🏷️ YouTube Comment Labeling Tool")
    st.markdown("""
    This application helps you label YouTube comments based on video frames.
    
    **Instructions:**
    1. Upload your Comments CSV (must contain `text_original` and `videoId` columns)
    2. Upload your Videos CSV (must contain `videoId` and `frame` columns)
    3. Select a video to label comments for
    4. Label each comment with a value (1, 2, or 3)
    5. Save your progress
    """)
    
    # Sidebar for file uploads and filters
    st.sidebar.header("📁 Data Upload & Filters")
    
    # File uploaders
    comments_file = st.sidebar.file_uploader(
        "Upload Comments CSV",
        type=['csv'],
        help="CSV file containing YouTube comments with 'text_original' and 'videoId' columns"
    )
    
    videos_file = st.sidebar.file_uploader(
        "Upload Videos CSV",
        type=['csv'],
        help="CSV file containing video IDs and frames"
    )
    
    # Load existing labels if available
    existing_labels = load_existing_labels()
    if existing_labels is not None:
        st.sidebar.success(f"✅ Loaded {len(existing_labels)} existing labels")
    
    # Main content area
    if comments_file is not None and videos_file is not None:
        # Load the CSV files
        comments_df = load_csv_file(comments_file)
        videos_df = load_csv_file(videos_file)
        
        if comments_df is not None and videos_df is not None:
            # Validate required columns
            if 'text_original' not in comments_df.columns:
                st.error("❌ Comments CSV must contain 'text_original' column")
                return
            
            if 'videoId' not in comments_df.columns:
                st.error("❌ Comments CSV must contain 'videoId' column")
                return
            
            if 'videoId' not in videos_df.columns or 'frame' not in videos_df.columns:
                st.error("❌ Videos CSV must contain 'videoId' and 'frame' columns")
                return
            
            # Display data info
            st.sidebar.markdown("---")
            st.sidebar.subheader("📊 Data Info")
            st.sidebar.write(f"Total comments: {len(comments_df)}")
            st.sidebar.write(f"Total videos: {len(videos_df)}")
            
            # Get unique video IDs
            video_ids = get_video_ids(videos_df)
            
            if not video_ids:
                st.error("No video IDs found in the videos CSV")
                return
            
            # Video selection
            st.sidebar.markdown("---")
            st.sidebar.subheader("🎬 Video Selection")
            selected_video = st.sidebar.selectbox(
                "Select Video ID",
                options=video_ids,
                help="Choose a video to label its comments"
            )
            
            # Frame filter (optional)
            frames = get_frames(videos_df)
            use_frame_filter = st.sidebar.checkbox("Filter by Frame", value=False)
            selected_frame = None
            
            if use_frame_filter and frames:
                selected_frame = st.sidebar.selectbox(
                    "Select Frame",
                    options=frames,
                    help="Filter videos by frame number"
                )
            
            # Filter for labeled/unlabeled comments
            st.sidebar.markdown("---")
            st.sidebar.subheader("🔍 Label Status Filter")
            label_filter = st.sidebar.radio(
                "Show comments:",
                options=["All", "Unlabeled Only", "Labeled Only"],
                index=0
            )
            
            # Filter comments
            filtered_comments = filter_comments(
                comments_df, 
                selected_video, 
                videos_df if use_frame_filter else None,
                selected_frame
            )
            
            # Merge with existing labels
            filtered_comments = merge_with_existing_labels(filtered_comments, existing_labels)
            
            # Apply label status filter
            if label_filter == "Unlabeled Only":
                filtered_comments = filtered_comments[filtered_comments['label'].isna()]
            elif label_filter == "Labeled Only":
                filtered_comments = filtered_comments[filtered_comments['label'].notna()]
            
            # Display statistics
            st.markdown("---")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Comments", len(filtered_comments))
            
            with col2:
                labeled_count = filtered_comments['label'].notna().sum()
                st.metric("Labeled", labeled_count)
            
            with col3:
                unlabeled_count = filtered_comments['label'].isna().sum()
                st.metric("Unlabeled", unlabeled_count)
            
            with col4:
                if len(filtered_comments) > 0:
                    progress_pct = (labeled_count / len(filtered_comments)) * 100
                    st.metric("Progress", f"{progress_pct:.1f}%")
                else:
                    st.metric("Progress", "0%")
            
            # Labeling interface
            if len(filtered_comments) == 0:
                st.info("ℹ️ No comments found for the selected filters")
            else:
                st.markdown("---")
                st.subheader("📝 Label Comments")
                
                # Initialize session state for labels if not exists
                if 'labels' not in st.session_state:
                    st.session_state.labels = {}
                
                # Display each comment with labeling option
                for idx, row in filtered_comments.iterrows():
                    with st.container():
                        st.markdown(f"**Comment #{idx}**")
                        st.text_area(
                            label="Comment Text",
                            value=row['text_original'],
                            height=100,
                            disabled=True,
                            key=f"text_{idx}"
                        )
                        
                        # Get existing label or default
                        existing_label = row.get('label', None)
                        if pd.notna(existing_label):
                            existing_label = int(existing_label)
                            default_index = LABEL_OPTIONS.index(existing_label)
                        else:
                            default_index = 0
                        
                        # Label selection
                        label = st.radio(
                            "Select Label:",
                            options=LABEL_OPTIONS,
                            index=default_index,
                            horizontal=True,
                            key=f"label_{idx}"
                        )
                        
                        # Store label in session state
                        st.session_state.labels[idx] = label
                        
                        # Update the dataframe
                        filtered_comments.at[idx, 'label'] = label
                        
                        st.markdown("---")
                
                # Save button
                st.markdown("### 💾 Save Labeled Data")
                col1, col2 = st.columns([1, 4])
                
                with col1:
                    if st.button("💾 Save Labels", type="primary"):
                        # Prepare data for saving
                        # Merge labeled data with all previously labeled data
                        if existing_labels is not None:
                            # Remove rows from existing_labels that match current filtered_comments
                            # to avoid duplicates
                            mask = ~(
                                existing_labels['text_original'].isin(filtered_comments['text_original']) &
                                existing_labels['videoId'].isin(filtered_comments['videoId'])
                            )
                            other_labels = existing_labels[mask]
                            
                            # Combine with newly labeled data
                            all_labeled = pd.concat([other_labels, filtered_comments], ignore_index=True)
                        else:
                            all_labeled = filtered_comments
                        
                        # Remove rows without labels
                        all_labeled = all_labeled[all_labeled['label'].notna()]
                        
                        # Save to file
                        if save_labeled_data(all_labeled):
                            st.success(f"✅ Successfully saved {len(all_labeled)} labeled comments to '{OUTPUT_FILE}'")
                        else:
                            st.error("❌ Failed to save labeled data")
                
                with col2:
                    st.info(f"Labels will be saved to: {OUTPUT_FILE}")
    
    else:
        # Show instructions when files are not uploaded
        st.info("👆 Please upload both CSV files using the sidebar to begin labeling")
        
        # Show example data formats
        st.markdown("### 📋 Expected CSV Formats")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Comments CSV Example:**")
            st.code("""videoId,text_original
video123,This is a great video!
video123,I learned a lot
video456,Nice content""")
        
        with col2:
            st.markdown("**Videos CSV Example:**")
            st.code("""videoId,frame
video123,1
video456,2
video789,3""")


if __name__ == "__main__":
    main()
