---
title: 'PACE: A Unified Condense-and-Extract Paradigm for Fast VLM Inference'
title_zh: PACE：基于统一压缩提取范式的视觉语言模型快速推理框架
authors:
- Junjie Liu
- Shengyuan Ye
- Xu Chen
affiliations:
- Sun Yat-sen University
- Guangdong Power Grid Co., Ltd. Power Dispatch Control Center
- Shenzhen Loop Area Institute
arxiv_id: '2608.27206'
url: https://arxiv.org/abs/2608.27206
pdf_url: https://arxiv.org/pdf/2608.27206
published: '2026-08-27'
collected: '2026-08-28'
category: Multimodal
direction: 多模态大模型 · VLM推理加速
tags:
- VLM
- Inference Acceleration
- Token Pruning
- Training-free
- Multimodal
one_liner: 提出训练免修改的PACE压缩提取范式，同时优化VLM视觉编码与LLM预填充，实现高分辨率场景下3倍首包推理加速
practical_value: '- 多模态商品理解、AI测款等场景的VLM部署可直接复用预编码自适应压缩+后编码双注意力剪枝的两阶段范式，训练免改即可降低高分辨率商品图的推理延迟3倍以上

  - 自适应像素压缩（APC）的设计可直接复用至多模态输入预处理：用浅层ViT块轻量预览全局信息密度+局部细节对比度，动态调整输入分辨率，在降本同时保留商品文字、规格等细粒度信息

  - 动态双注意力剪枝（DDAE）的置信度加权融合思路可迁移至多模态特征选择场景：同时结合语义相关性（LLM侧）和视觉显著性（ViT侧）信号筛选关键特征，避免单一信号导致的信息丢失'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
VLM在高分辨率图文、文档、视频等场景推理时，视觉token数量随分辨率提升指数级增长，现有视觉token剪枝方法仅在视觉编码器后执行操作，既未解决编码器本身的高延迟瓶颈，又在严格token预算下难以同时保留全局上下文和细粒度细节，导致OCR、图表理解、文档问答等细节敏感任务精度大幅下降，严重限制高分辨率VLM的工业落地。

### 方法关键点
- 压缩阶段：自适应像素压缩器（APC）先用ViT第一层做轻量特征预览，计算全局信息密度和局部细节对比度，自适应下采样冗余输入，降低编码器计算量同时保留全局布局和关键视觉线索
- 提取阶段：动态双注意力提取器（DDAE）融合ViT自注意力（视觉显著性）和LLM浅层跨模态注意力（语义相关性）信号，按两个注意力分布的标准差动态分配融合权重，筛选Top-K关键视觉token输入LLM
- 整个框架训练免改、即插即用，可兼容现有主流VLM架构

### 关键实验结果
在Qwen2.5-VL-7B上测试，对比FastV、SparseVLM、VisionZip等6种主流剪枝基线，覆盖9个多模态benchmark（含OCRBench、DocVQA等细粒度敏感任务）：仅保留10%视觉token时，保留原模型93.8%的精度，首包生成时间（TTFT）加速3.1×；仅保留5%token时精度仍达原模型的84.3%；将APC模块接入现有剪枝方法，可提升OCR、文档理解类任务精度10~18个百分点。

### 核心结论
VLM推理加速不能仅优化LLM侧的token剪枝，从输入像素阶段做自适应压缩、再结合多模态信号协同剪枝，可在精度损失极小的前提下实现更高的加速比。
