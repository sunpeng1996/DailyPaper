---
title: Self-Distillation with Verbal Regularization
title_zh: 带言语正则化的大语言模型自蒸馏方法
authors:
- Jiazheng Li
- Yawei Li
- Junru Lu
- Zhenyi Shen
- Di Yin
- Lin Gui
- Xing Sun
- David Rügamer
- Xinpeng Wang
- Yulan He
affiliations:
- King's College London
- LMU Munich
- Munich Center for Machine Learning
- Tencent YouTu Lab
arxiv_id: '2610.16354'
url: https://arxiv.org/abs/2610.16354
pdf_url: https://arxiv.org/pdf/2610.16354
published: '2026-10-11'
collected: '2026-10-14'
category: Training
direction: 大语言模型 · 自蒸馏训练正则优化
tags:
- Self-Distillation
- LLM Training
- Regularization
- Knowledge Distillation
- Reasoning
one_liner: 给自蒸馏教师侧加专用系统提示，缓解特权信息捷径偏差，平均提Pass@1 3.9个百分点
practical_value: '- 做LLM4Rec、电商导购Agent的自蒸馏时，无需修改模型架构或损失函数，仅给教师侧加任务专属的「鼓励验证步骤、反思推理」系统提示，即可缓解特权信息导致的输出坍缩，提升推理准确率，落地成本极低

  - 自蒸馏的提示设计优先选「多组不同侧重的短提示分给不同rollout」的方案，比单条长复合提示、拼接所有提示的效果更好，可直接复用在推荐场景query理解、商品文案生成的蒸馏流程

  - 当业务中OPSD自蒸馏出现效果下降、输出过于集中的问题时，可优先尝试教师侧加正则提示的方案，比修改损失、过滤样本的研发和算力成本低很多

  - 测评蒸馏后模型的推理可信度，可复用「截断推理链后重生成答案，对比准确率变化」的方法，适合电商导购Agent、推荐理由生成模型的推理保真度评估'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-policy自蒸馏（OPSD）无需额外教师模型，可利用特权信息（如正确答案、验证过的推理路径）提升LLM能力，但特权信息会让教师模型倾向捷径推理，输出分布熵骤降，学生继承该问题后探索能力受限，推理保真度低。现有优化方案要么修改损失函数，要么调整特权信息，接入现有管线的成本较高。

### 方法关键点
- 提出VRSD，仅给自教师侧增加训练专用的系统提示，指令教师验证中间步骤、考虑替代路径、反思推理过程后再输出，无需修改模型架构、损失函数或特权信息，可直接嵌入现有OPSD管线
- 理论上证明正则提示会对特权信息带来的对数概率偏移做仿射衰减，满足温和条件时可保留教师分布熵，缓解输出坍缩问题
- 支持两种部署模式：单提示模式所有rollout共用一条复合正则提示，多提示模式将不同侧重的正则提示分配给不同rollout，效果更优

### 关键实验
在Qwen3-4B/8B、OLMo-3-7B-Instruct三个模型，短答案评分、化学题求解、SQL生成、Python代码生成四个任务上，对比OPSD、AntiSD等基线：12组模型-任务设置中11组Pass@1超过OPSD，平均提升3.9个百分点；同时学生输出熵更高，推理忠实度（RG指标）平均提升1.3~2.1个百分点，误导推理率平均下降0.9~1.4个百分点。

**最值得记住的一句话**：大模型本身的指令跟随能力可以作为自蒸馏的正则手段，成本极低且效果显著
