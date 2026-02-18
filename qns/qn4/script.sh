THRESHOLD=90
PARTITION="/"
TARGET_DIR="/mnt/backup_drive"


USAGE=$(df -h $PARTITION | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$USAGE" -ge "$THRESHOLD" ]; then
    echo "Disk usage is high ($USAGE%). Moving files..."
    
    find /var/log -type f -size +100M -printf '%s %p\n' | sort -nr | head -n 5 | awk '{print $2}' | while read file; do
        tar -czf "$TARGET_DIR/$(basename $file).tar.gz" "$file" && rm "$file"
    done
fi
