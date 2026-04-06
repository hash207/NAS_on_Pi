import os
import mimetypes
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from django.conf import settings
from pathlib import Path
import re

def natural_sort_key(s):
    """Key function for natural sorting (e.g., 2 before 10)."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def file_explorer(request, path=''):
    # Define the root directory to explore. 
    root_dir = settings.BASE_DIR / 'media'
    
    # Construct the full path
    full_path = os.path.join(root_dir, path)
    
    # Security check: ensure the path is within the root_dir
    if not os.path.abspath(full_path).startswith(os.path.abspath(root_dir)):
        raise Http404("Invalid path")
    
    if os.path.isdir(full_path):
        items = []
        try:
            with os.scandir(full_path) as it:
                for entry in it:
                    item = {
                        'name': entry.name,
                        'path': os.path.join(path, entry.name).replace('\\', '/'),
                        'is_dir': entry.is_dir(),
                        'size': entry.stat().st_size if entry.is_file() else 0,
                    }
                    items.append(item)
        except PermissionError:
            pass # Handle permission errors gracefully
            
        # Sort: directories first, then items by natural alphabetical order
        items.sort(key=lambda x: (not x['is_dir'], natural_sort_key(x['name'])))
        
        # Calculate parent path
        parent_path = None
        if path:
            parent = Path(path).parent
            if parent == Path('.'):
                parent_path = ""
            else:
                parent_path = str(parent).replace('\\', '/')

        context = {
            'current_path': path,
            'parent_path': parent_path,
            'items': items,
        }
        return render(request, 'explorer/explorer.html', context)
    
    elif os.path.isfile(full_path):
        # Determine mime type
        mime_type, _ = mimetypes.guess_type(full_path)
        
        # Calculate parent path
        parent = Path(path).parent
        if parent == Path('.'):
            parent_path = ""
        else:
            parent_path = str(parent).replace('\\', '/')
        
        if mime_type and (mime_type.startswith('video') or mime_type.startswith('audio')):
            context = {
                'file_name': os.path.basename(full_path),
                'file_path': path, # We might need a way to serve this file via URL
                'mime_type': mime_type,
                'parent_path': parent_path,
            }
            return render(request, 'explorer/player.html', context)
        else:
            # For other files, maybe just download or serve raw?
            # For now, let's try to serve it.
            return FileResponse(open(full_path, 'rb'))
    else:
        raise Http404("Path not found")

def serve_file(request, path):
    """
    Helper view to serve the actual file content for the player.
    """
    root_dir = settings.BASE_DIR / 'media'
    full_path = os.path.join(root_dir, path)
    
    if not os.path.abspath(full_path).startswith(os.path.abspath(root_dir)):
        raise Http404("Invalid path")
        
    if os.path.isfile(full_path):
        return FileResponse(open(full_path, 'rb'))
    else:
        raise Http404("File not found")
