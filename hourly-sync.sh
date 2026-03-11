#!/bin/bash
# 每小时自动同步脚本

LOG_FILE="HOURLY-AUTO-LOG.md"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')

# 检查 Git 变更
CHANGES=$(git status --porcelain | wc -l)

if [ $CHANGES -gt 0 ]; then
    # 自动提交
    git add -A
    git commit -m "auto: 每小时同步 $TIMESTAMP"
    git push
    
    # 更新日志
    echo "" >> $LOG_FILE
    echo "## ⏰ $TIMESTAMP" >> $LOG_FILE
    echo "" >> $LOG_FILE
    echo "**自动提交：** 完成" >> $LOG_FILE
    echo "**变更文件：** $CHANGES 个" >> $LOG_FILE
    echo "" >> $LOG_FILE
    
    echo "✅ 自动提交完成"
else
    echo "⏸️  无变更，跳过提交"
fi
