---
title: Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented
  VLA Policies
title_zh: 记忆增强VLA策略的时间捷径缺陷：误将时钟流逝当任务进度
authors:
- Chubin Zhang
- Bo An
affiliations:
- Nanyang Technological University
arxiv_id: '2611.14488'
url: https://arxiv.org/abs/2611.14488
pdf_url: https://arxiv.org/pdf/2611.14488
published: '2026-11-09'
collected: '2026-11-12'
category: Agent
direction: 具身Agent记忆优化 · 时间捷径缺陷修复
tags:
- VLA
- Memory Augmentation
- Temporal Shortcut
- Embodied Agent
- RoboMME
one_liner: 发现记忆增强VLA的时间捷径缺陷，提出事件索引记忆方案无需重训即可修复过半性能损失
practical_value: '- 开发带记忆的电商导购Agent、用户行为序列建模模块时，避免直接用时间步作为记忆索引，防止无操作时段被误算为任务进度

  - 现有基于时间采样的记忆系统出现时间捷径问题时，无需全量重训，切换为事件驱动的记忆索引即可快速修复过半性能损失

  - 构建用户行为召回/多步转化预测模型时，可过滤无意义空行为（如无点击停留）的记忆槽位占用，避免干扰计数类任务判断'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
记忆增强VLA普遍采用按时间均匀采样帧、打时间戳的记忆填充逻辑，空事件（如暂停、无意义动作）发生时时间仍在流逝，无法区分等待和工作状态，导致任务判断错误。
### 方法关键点
在RoboMME计数任务中插入空事件定位根因：训练演示样本节奏稳定，模型学到「时间流逝=任务进度」的时间捷径；对比移除时间编码、注入暂停训练、事件索引记忆三种修复方案。
### 关键结果
空事件会让两类计数任务成功率分别从47/50降至16/50、44/50降至10/50；移除时间编码无法解决问题，注入暂停训练会损伤计数能力，事件索引记忆无需重训即可恢复过半性能损失
