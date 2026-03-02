"""
Firebase configuration module for state management across music generation pipeline.
Uses Firestore for distributed state tracking and error recovery.
"""

import os
import logging
from typing import Dict, Any, Optional
from datetime import datetime
import sys

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

class FirebaseManager:
    """Manages Firebase connection with comprehensive error handling."""
    
    def __init__(self, service_account_path: Optional[str] = None):
        """
        Initialize Firebase Admin SDK with multiple fallback strategies.
        
        Args:
            service_account_path: Path to service account JSON file.
                If None, tries environment variable, then defaults to local file.
        """
        self.db