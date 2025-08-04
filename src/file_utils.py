import os
import shutil
import logging
from pathlib import Path


def setup_logging():
    """Setup logging configuration for file operations."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def copy_directory_recursive(source_dir: str, dest_dir: str, log_operations: bool = True) -> bool:
    """
    Recursively copy all contents from source directory to destination directory.
    
    Args:
        source_dir (str): Path to the source directory
        dest_dir (str): Path to the destination directory
        log_operations (bool): Whether to log file operations (default: True)
    
    Returns:
        bool: True if successful, False otherwise
    """
    if log_operations:
        setup_logging()
        logger = logging.getLogger(__name__)
    
    try:
        # Convert to Path objects for easier handling
        source_path = Path(source_dir)
        dest_path = Path(dest_dir)
        
        # Validate source directory exists
        if not source_path.exists():
            if log_operations:
                logger.error(f"Source directory does not exist: {source_path}")
            return False
        
        if not source_path.is_dir():
            if log_operations:
                logger.error(f"Source path is not a directory: {source_path}")
            return False
        
        # Create destination directory if it doesn't exist
        dest_path.mkdir(parents=True, exist_ok=True)
        
        # Delete all contents of destination directory first
        if log_operations:
            logger.info(f"Cleaning destination directory: {dest_path}")
        
        for item in dest_path.iterdir():
            if item.is_file():
                item.unlink()
                if log_operations:
                    logger.info(f"Deleted file: {item}")
            elif item.is_dir():
                shutil.rmtree(item)
                if log_operations:
                    logger.info(f"Deleted directory: {item}")
        
        # Copy all contents recursively
        if log_operations:
            logger.info(f"Starting recursive copy from {source_path} to {dest_path}")
        
        _copy_recursive_helper(source_path, dest_path, log_operations)
        
        if log_operations:
            logger.info(f"Successfully copied all contents from {source_path} to {dest_path}")
        
        return True
        
    except Exception as e:
        if log_operations:
            logger.error(f"Error during directory copy: {str(e)}")
        return False


def _copy_recursive_helper(source_path: Path, dest_path: Path, log_operations: bool = True):
    """
    Helper function to recursively copy files and directories.
    
    Args:
        source_path (Path): Source path
        dest_path (Path): Destination path
        log_operations (bool): Whether to log operations
    """
    if log_operations:
        logger = logging.getLogger(__name__)
    
    try:
        for item in source_path.iterdir():
            dest_item = dest_path / item.name
            
            if item.is_file():
                # Copy file
                shutil.copy2(item, dest_item)
                if log_operations:
                    logger.info(f"Copied file: {item} -> {dest_item}")
            
            elif item.is_dir():
                # Create directory and copy its contents recursively
                dest_item.mkdir(exist_ok=True)
                if log_operations:
                    logger.info(f"Created directory: {dest_item}")
                
                _copy_recursive_helper(item, dest_item, log_operations)
    
    except Exception as e:
        if log_operations:
            logger.error(f"Error copying {source_path}: {str(e)}")
        raise


def copy_static_to_public():
    """
    Convenience function to copy static directory to public directory.
    This is the specific use case mentioned in the requirements.
    """
    return copy_directory_recursive("../static", "../docs")


def write_html_to_file(html_content: str, dest_path: str, log_operations: bool = True) -> bool:
    """
    Write HTML content to a file, creating necessary directories if they don't exist.
    
    Args:
        html_content (str): The HTML content to write to the file
        dest_path (str): Path where the HTML file should be written
        log_operations (bool): Whether to log file operations (default: True)
    
    Returns:
        bool: True if successful, False otherwise
    """
    if log_operations:
        setup_logging()
        logger = logging.getLogger(__name__)
    
    try:
        # Convert to Path object for easier handling
        dest_file_path = Path(dest_path)
        
        # Validate that we have content to write
        if html_content is None:
            if log_operations:
                logger.error("HTML content cannot be None")
            return False
        
        # Create parent directories if they don't exist
        dest_file_path.parent.mkdir(parents=True, exist_ok=True)
        if log_operations:
            logger.info(f"Ensured directory exists: {dest_file_path.parent}")
        
        # Write the HTML content to the file
        with dest_file_path.open('w', encoding='utf-8') as file:
            file.write(html_content)
        
        if log_operations:
            logger.info(f"Successfully wrote HTML file: {dest_file_path}")
            logger.info(f"File size: {len(html_content)} characters")
        
        return True
        
    except PermissionError as e:
        if log_operations:
            logger.error(f"Permission denied writing to {dest_path}: {str(e)}")
        return False
    except OSError as e:
        if log_operations:
            logger.error(f"OS error writing to {dest_path}: {str(e)}")
        return False
    except Exception as e:
        if log_operations:
            logger.error(f"Unexpected error writing HTML file {dest_path}: {str(e)}")
        return False


if __name__ == "__main__":
    # Test the functions
    success = copy_static_to_public()
    if success:
        print("Successfully copied static directory to public directory")
    else:
        print("Failed to copy static directory to public directory")
