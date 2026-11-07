---
title: Generalizable AI-Generated Image Detection with Embedding-Space Explanations
title_zh: 具备嵌入空间可解释性的通用AI生成图像检测方法
authors:
- Nikos Giakoumoglou
- Paschalis Giakoumoglou
- Tania Stathaki
- Symeon Papadopoulos
affiliations:
- Imperial College London
- Information Technologies Institute, CERTH
arxiv_id: '2611.04111'
url: https://arxiv.org/abs/2611.04111
pdf_url: https://arxiv.org/pdf/2611.04111
published: '2026-11-03'
collected: '2026-11-07'
category: Multimodal
direction: 多模态AIGC检测 · 可解释性优化
tags:
- AIGC Detection
- DINOv3
- VLM
- Explainable AI
- Embedding Space
one_liner: 提出锁死DINOv3检测器+轻量VLM的FOX框架，实现高泛化性的可解释AI生成图像检测
practical_value: '- 可复用「冻结核心任务单模态骨干+仅训轻量跨模态映射层」架构，在不改动现有成熟AIGC检测、商品合规检测模型的前提下，新增可解释性输出能力

  - 联合嵌入空间对齐思路可迁移到电商场景：将商品图视觉特征映射到固定文本语义空间生成合规性判定理由，降低人工审核成本

  - 不拟合特定生成器指纹的泛化训练思路，可用于应对平台上不断迭代的AIGC作图工具生成的违规内容，减少模型迭代频率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
当前AI生成图、指令驱动编辑的AI修改图真实度极高，无明显拼接痕迹难以检测；多数AIGC检测器泛化性差，且联合训练分类+语言生成的可解释方案会损失纯视觉检测器的跨生成器泛化优势，黑盒结果难以落地。
### 方法关键点
FOX框架设计为：1）先训练并完全锁死基于DINOv3的纯视觉AIGC专用检测器，保证检测精度与泛化性不受后续任务影响；2）新增轻量联合嵌入预测器，将锁死的视觉特征映射到冻结文本编码器的语义空间，引导轻量VLM生成检测解释，全程不修改检测器权重。
### 关键结果
在14个未见过的生成器上平均AUC达97.4，XPlainVerse数据集BERTScore为69.8，LOKI数据集BERTScore为56.1，兼顾检测性能与可解释性。
