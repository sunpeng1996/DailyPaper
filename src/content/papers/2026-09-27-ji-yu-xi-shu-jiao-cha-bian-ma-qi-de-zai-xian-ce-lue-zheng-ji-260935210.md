---
title: 'Understanding On-Policy Distillation: A Mechanistic Interpretability Perspective
  via Sparse Crosscoders'
title_zh: 基于稀疏交叉编码器的在线策略蒸馏机制可解释性研究
authors:
- Zichao Yu
- Qianshuo Ye
- Xu Wang
- Difan Zou
affiliations:
- The University of Hong Kong
- University of Cambridge
- Shenzhen Loop Area Institute
arxiv_id: '2609.35210'
url: https://arxiv.org/abs/2609.35210
pdf_url: https://arxiv.org/pdf/2609.35210
published: '2026-09-27'
collected: '2026-09-30'
category: Training
direction: LLM训练 · 在线策略蒸馏可解释性
tags:
- On-policy Distillation
- Sparse Crosscoder
- Mechanistic Interpretability
- Knowledge Distillation
- SFT
one_liner: 提出swap readout方法揭示在线策略蒸馏本质是对已有共享特征的重加权而非新特征获取
practical_value: '- 做推理类Agent（如商品导购、营销文案生成Agent）的蒸馏优化时，无需追求让小模型学习教师独有的特征，优先保证小模型与教师有足够多的共享特征，可大幅提升蒸馏效率

  - OPD前的SFT warm-up无需构造复杂域外数据，直接用教师模型在目标任务上的生成rollout做微调即可，本质是提前完成特征重加权，可将教师优势恢复率从30%提升到46%

  - 若需快速对齐小模型与大模型的推理效果，可直接在特征层施加warm-up得到的重加权系数，无需重新训练模型权重，就能恢复大部分warm-up收益，适合快速迭代的业务场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-policy distillation（OPD）已成为LLM推理能力后训练的主流技术，被Qwen3、GLM-5等广泛采用，但此前仅从输出层面分析其效果，内部蒸馏机制不清晰，无法解释OPD时常失效、仅提升采样效率不拓展能力边界等现象，亟需从表征层面拆解其实际作用。

### 方法关键点
- 基于稀疏交叉编码器学习蒸馏前后学生模型、教师模型三者共享的特征字典，解决传统交叉编码器无法追踪同一模型不同训练阶段特征使用变化的问题
- 提出swap readout方法：将同一个学生检查点的激活同时输入交叉编码器的两个学生槽位，固定教师输入，可准确测量任意未见过的学生检查点的特征激活变化
- 设计特征干预实验：直接对学生模型的特征激活施加warm-up阶段得到的重加权系数，验证重加权是收益来源

### 关键结果
在3个OPD场景（教师分别为同尺寸RL微调模型、7B数学推理模型、7B同系列蒸馏模型）测试，训练集为DAPO-Math-17k，验证集为AIME 2024/2025、AMC 2023：
- OPD过程中超过98%的学生常用特征激活率变化小于20%，既不生成新特征，也不获取教师独有的特征，仅对推理转折类决策token对应的特征做小幅重加权，这些位置师生KL散度是平均水平的1.5~3.6倍
- OPD前加SFT warm-up可将教师优势恢复率从30%提升至46%；warm-up同样不生成新特征，仅提前完成OPD一半的重加权工作，同时补充OPD不会做的对话格式、推理风格类特征重加权
- 直接对无warm-up的学生施加该重加权系数，无需修改模型权重，即可让其精度接近有warm-up的学生水平

### 核心结论
在线策略蒸馏的本质是对学生和教师已有的共享特征做重加权，而非获取新特征，其效果上限由学生初始与教师的特征重叠度决定。
