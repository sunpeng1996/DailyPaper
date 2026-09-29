---
title: 'SMAT: Simple and Efficient Merge-Aware Training'
title_zh: SMAT：简单高效的合并感知训练方法
authors:
- Yanggan Gu
- Yuanyi Wang
- Zhen Li
- Shuo Cai
- Yuhang Liu
- Junzhuo Li
- Zihao Wang
- Hongxia Yang
affiliations:
- The Hong Kong Polytechnic University
- The Hong Kong University of Science and Technology (Guangzhou)
- The Chinese University of Hong Kong
- PolyU-Daya Bay Technology and Innovation Research Institute
- InfiX.ai
arxiv_id: '2609.33437'
url: https://arxiv.org/abs/2609.33437
pdf_url: https://arxiv.org/pdf/2609.33437
published: '2026-09-26'
collected: '2026-09-29'
category: Training
direction: 合并感知训练 · 多专家模型融合
tags:
- Model Merging
- Merge Aware Training
- LLM Training
- Efficient Training
- Multi Expert Fusion
one_liner: 通过模拟三类通用合并操作，实现仅<2%训练开销的合并感知训练，提升多专家合并后性能
practical_value: '- 电商/推荐场景下训练多垂直领域LLM专家（如query理解、文案生成、客服意图识别）时，可直接采用SMAT训练范式，无需额外数据即可提升后续多专家合并的性能，训练开销仅增加不到2%

  - 工程侧可直接复用SMAT的三个优化trick：周期性调度、核融合、参数存储切换，在现有训练pipeline中极低成本实现合并感知正则，几乎不影响原有训练速度

  - 模拟其他专家更新的扰动思路可迁移至多LoRA Adapter合并场景，无需依赖其他Adapter的数据即可降低多Adapter合并后的性能衰减，适合多业务LoRA统一部署的场景

  - 可复用SMAT的性能平衡思路：无需为了合并效果过度牺牲单专家性能，SMAT的训练目标可同时保留单专家效果和合并后效果，适配业务对单领域+多领域部署的双重需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多专家模型合并无需联合重训即可整合不同领域能力，是降低大模型部署成本的核心手段，但标准单专家微调仅优化自身任务损失，合并后易出现参数冲突导致性能大幅下降；现有合并感知训练方法未覆盖通用合并操作，且普遍存在训练开销高、落地成本高的问题。

### 方法关键点
- 将主流合并方法（Task Arithmetic、TIES、DARE等）统一抽象为三类操作：Scale重加权自身任务向量、Mask随机丢弃部分参数坐标、Perturb加均匀噪声模拟其他专家的更新，训练时联合优化单专家损失和模拟合并参数的期望损失。
- 工程侧做了三层优化：周期性调度（每4步仅1步跑模拟合并损失，其余跑单专家损失，每步仅1次前向+反向传播）、Triton核融合三类模拟操作减少内存访问、参数存储切换用独立缓存存模拟参数避免重复拷贝。
- 超参设置极简：Scale系数从均匀分布采样，Mask仅作用于Transformer注意力和MLP线性层，丢弃概率默认0.5，扰动用固定RMS的均匀噪声。

### 关键结果
在Llama-3.2-1B、Llama-3.1-8B、CLIP ViT-B/32、CLIP ViT-L/14四个backbone上测试，覆盖5种主流合并方法，SMAT比各场景最强基线的合并后平均得分高1.07~2.16分，训练时间开销不到标准微调的2%；Llama-3.2-1B场景下比OrthoReg训练快82%的同时，合并得分高1.12分。

### 核心结论
无需额外数据、无需修改合并逻辑，仅在单专家训练时增加极低开销的模拟合并正则，即可大幅提升多专家合并后的性能，是落地成本极低的多模型融合提效方案。
