---
title: Local Support Learning
title_zh: 局部支撑学习：无需旧数据的大模型灾难性遗忘缓解框架
authors:
- Assaf Ben-Kish
- Akarsh Kumar
- James Glass
- Raja Giryes
affiliations:
- Tel Aviv University
- MIT CSAIL
arxiv_id: '2610.02126'
url: https://arxiv.org/abs/2610.02126
pdf_url: https://arxiv.org/pdf/2610.02126
published: '2026-10-01'
collected: '2026-10-02'
category: Training
direction: 大模型训练 · 灾难性遗忘缓解
tags:
- Catastrophic Forgetting
- LoRA
- GMM
- Parameter Efficient Fine-tuning
- LLM
one_liner: 通过双GMM门控让适配器仅作用于当前分布激活，无需旧数据缓解大模型灾难性遗忘
practical_value: '- 做电商垂直领域LLM微调（客服、导购Agent、商品文案生成）时，可复用LSL的GMM门控逻辑，避免微调垂直数据后丢失通用推理、对话能力，无需存储预训练原始数据

  - 多阶段能力迭代场景（先后微调营销话术、售后答疑、选品推荐能力）可直接复用LSL的多适配器+门控架构，各阶段能力互不干扰，遗忘率比直接叠加LoRA低44%

  - 推理延迟容忍度>20%的线上场景，可直接替换现有LoRA微调流程，仅增加13.8MB额外内存，即可保留98%以上的预训练基础能力

  - 做用户/内容语义表征增量训练时，可借鉴局部更新思路，仅让新特征的更新作用于对应分布的输入，避免旧特征表征退化'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大模型多阶段微调时普遍存在灾难性遗忘问题，现有方法要么需要存储海量旧训练数据（对于预训练级数据量完全不可行），要么仅限制权重更新的空间正交性，无法从根源避免更新对非当前分布输入的干扰，导致新任务学习和旧能力保留的 trade-off 难以平衡。

### 方法关键点
- 核心思路：让每个微调阶段的权重适配器（支持LoRA等主流参数高效微调结构）仅作用于当前训练分布的输入激活，对其他分布输入完全不生效
- 双GMM门控设计：Φ_pos拟合当前微调数据的激活分布，Φ_neg拟合少量通用预训练数据的分布，通过比较两个GMM的似然判断是否激活对应适配器，无需任何旧阶段的训练数据
- 新增时间平滑模块，对门控输出做指数滑动平均，减少单token判断的波动，进一步降低旧任务的门控误触发率
- 每层独立门控：推理时每个矩阵层独立做门控判断，比单token全局门控的新任务适配能力提升23%-50%

### 关键结果
在Qwen2.5-7B-Instruct上实验，对比LoRA、OP-LoRA、LwF三类基线，在网络安全指令微调、低资源翻译、化学指令微调三个下游任务上：LSL的新任务性能和基线持平，预训练能力（数学、代码、指令遵循）保留率达98.8%，比LoRA高44%；多阶段微调时三个下游任务的性能保留率比LoRA高5%-11%，超参（学习率、Adapter rank、batch size）对保留率无明显影响，额外内存开销仅13.8MB，推理延迟比LoRA高21%。

### 核心结论
缓解大模型灾难性遗忘的核心不是限制权重更新的大小，而是让更新仅作用于它本该影响的输入分布区域
