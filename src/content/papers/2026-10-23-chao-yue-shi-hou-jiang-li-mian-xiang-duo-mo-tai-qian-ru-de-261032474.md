---
title: 'Beyond Post-Hoc Rewards: Privileged Reasoning Exploration for Multimodal Embeddings'
title_zh: 超越事后奖励：面向多模态嵌入的特权推理探索框架
authors:
- Tianyu Yang
- Yijun Tian
- Lars Benedikt Kaesberg
- Jan Philip Wahle
- Bela Gipp
- Terry Ruas
- Daniel Kurzawe
affiliations:
- University of Göttingen
- University of Notre Dame
- State and University Library of Göttingen
arxiv_id: '2610.32474'
url: https://arxiv.org/abs/2610.32474
pdf_url: https://arxiv.org/pdf/2610.32474
published: '2026-10-23'
collected: '2026-10-26'
category: Multimodal
direction: 多模态嵌入 · 特权信息学习
tags:
- Multimodal Embedding
- Privileged Information
- MLLM
- Chain-of-Thought
- Retrieval
one_liner: 提出PILOT特权推理框架，利用训练时正负样本引导推理探索，推理仅依赖输入，显著提升多模态嵌入效果
practical_value: '- 电商多模态商品召回/图文搜索场景可复用盲对比后验设计：训练时用正负样本对引导模型生成带判别性的推理链，推理时无需额外上下文，完全不增加线上延迟

  - 生成式推荐/多模态RAG系统训练可复用先验-后验协同进化框架：用GRPO优化双推理分支，基于重要性加权仅迁移高回报且可被先验复现的推理轨迹，避免无效蒸馏引入的偏差

  - 训练带推理的MLLM嵌入模型时，可引入正确性验证过滤机制：仅保留能正确区分正负样本的推理链作为监督数据，大幅降低噪声对训练的干扰'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有推理增强的多模态嵌入方法仅从输入本身生成推理链，正负样本的关系仅被用作事后奖励，无法主动引导模型探索能区分正负样本的高判别性推理轨迹，存在严重探索瓶颈：大量能提升检索效果的推理链无法被采样到，事后奖励只能强化已采样的次优轨迹，最终导致嵌入的区分度不足。

### 方法关键点
- 提出PILOT框架，将推理链建模为隐变量，设置双推理模式：训练时的后验模式可访问打乱顺序、无标签的正负样本对（盲对比设计，强制模型自主比较语义差异），推理时的先验模式仅依赖原始输入，完全符合线上部署要求。
- 先用更强的标注MLLM合成双模式推理链，仅保留能正确识别正样本的后验推理链作为监督数据，通过SFT+对比损失联合初始化双模式的参数。
- 基于重要性加权变分目标实现先验-后验协同进化：用GRPO分别优化两个模式的推理能力，仅将同时满足高检索回报、可被先验模式复现两个条件的后验推理链，通过加权SFT迁移到先验模式，避免强制蒸馏引入的偏移。

### 关键实验
在包含78个任务的MMEB-V2基准上，对比同类推理增强基线UME-R1，2B参数版本整体得分提升3.2，7B版本提升3.3；其中视觉文档检索任务增益最大，分别达到6.1和6.4，2B版本的视觉文档检索表现甚至超过7B参数的UME-R1基线。

### 核心结论
检索监督的价值不仅是作为事后奖励评估推理质量，更应该用来引导训练阶段的推理探索方向。
