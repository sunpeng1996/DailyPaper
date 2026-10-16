---
title: 'STP-GUI: Spatially-Aware Token Pruning for Efficient Web-GUI Agents'
title_zh: STP-GUI：面向Web-GUI智能体的空间感知Token剪枝方法
authors:
- Shuo Wang
- Sifan Zhou
- Xiaobo Wang
- Tianyu Fu
- Chenxu Zhao
- Anyang Su
- Hanning Wang
- Ping Jiang
- Minghui Wu
affiliations:
- Mininglamp
- Southeast University
- Shenzhen University of Advanced Technology
arxiv_id: '2610.20390'
url: https://arxiv.org/abs/2610.20390
pdf_url: https://arxiv.org/pdf/2610.20390
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: GUI Agent · 视觉Token剪枝效率优化
tags:
- GUI Agent
- Token Pruning
- VLM
- Spatial Awareness
- Policy Learning
one_liner: 冻结VLM骨干训练轻量选择器，实现空间连续窗口级视觉Token剪枝，低保留率下兼顾GUI Agent性能与推理效率
practical_value: '- 做电商/后台操作类GUI Agent落地时，无需微调整个VLM，仅训练2M参数的轻量剪枝选择器即可大幅降低推理延迟，训练成本极低

  - 针对电商页面/APP界面小交互元素密集的场景，放弃逐token剪枝，改用非重叠空间窗口级选择，可避免元素结构碎片化，在保留75%+性能的前提下压减79%的视觉token量

  - 无标注场景下可直接用全token模型的输出作为剪枝选择器的监督信号，无需额外标注UI元素边界框，适合业务快速迭代

  - 推理阶段直接按窗口分数贪心选择即可，无需修改VLM原有推理逻辑，对现有部署架构侵入性极低，H20下3帧输入场景可直接降31% latency、57% FLOPs'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
VLM-based Web-GUI Agent依赖高分辨率截图识别按钮、图标等小交互元素，单张1080P截图生成2k+视觉token，多轮历史叠加后总token量易超10k，成为推理延迟瓶颈。现有针对自然图像设计的逐token剪枝方法会打散GUI元素的局部连续结构，导致性能暴跌，无法适配GUI场景。

### 方法关键点
- 粒度解耦设计：先通过轻量指令对齐模块输出逐token的任务相关度分数，再聚合到W×W非重叠空间窗口，以窗口为单位选择保留token，避免元素碎片化
- 训练逻辑：仅优化2M参数的选择器，全程冻结VLM骨干；用Plackett-Luce分布采样窗口，基于PPO策略训练，支持两种奖励：标注的ground-truth动作奖励、全token模型输出一致性奖励，无标注也可训练
- 推理逻辑：固定token保留比例，按窗口分数贪心选择，无需修改VLM推理逻辑

### 关键实验
在Online-Mind2Web（300个真实网站任务）、AitW移动端GUI数据集上对比HiPrune、PDrop、FlashVLM等主流剪枝方案：21% token保留率下，保留77.7%的全token性能，推理延迟降31%、FLOPs降57%，内存占用仅982MB（比FlashVLM低9倍）；50%保留率下保留93.8%全token性能，跨移动端GUI场景收益一致。

### 核心结论
GUI界面的视觉token剪枝，保留局部空间连续性比筛选零散的高相关度token重要得多。
