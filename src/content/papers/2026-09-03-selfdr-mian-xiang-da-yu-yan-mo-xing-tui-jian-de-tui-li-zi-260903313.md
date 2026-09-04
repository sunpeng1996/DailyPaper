---
title: 'SelfDR: Self-Distillation from Reasoning for LLM-Based Recommendation'
title_zh: SelfDR：面向大语言模型推荐的推理自蒸馏框架
authors:
- Chumeng Jiang
- Jiayin Wang
- Xinjie Lin
- Zhiqiang Guo
- Hengliang Luo
- Min Zhang
affiliations:
- Tsinghua University
- Meituan
- Quan Cheng Laboratory
arxiv_id: '2609.03313'
url: https://arxiv.org/abs/2609.03313
pdf_url: https://arxiv.org/pdf/2609.03313
published: '2026-09-03'
collected: '2026-09-04'
category: GenRec
direction: 生成式推荐 · 推理自蒸馏
tags:
- LLM4Rec
- Self-Distillation
- Reasoning
- Efficiency
- GRPO
one_liner: 通过自蒸馏将LLM推理能力迁移到直接推荐模型，兼顾推荐效果与推理效率
practical_value: '- 可复用GRPO训练业务专属reasoner的思路，用下游推荐效果作为奖励信号，无需依赖外部大模型生成推理样本，降本同时适配业务特性

  - 动态权重蒸馏trick可直接落地：根据师生模型对正样本的排名差自适应调整蒸馏损失权重，避免低质量teacher信号干扰训练

  - 推理阶段完全不需要生成推理链，延迟和普通直接推荐模型一致，无需修改现有线上SLA要求即可上线

  - 跨域泛化效果优于普通微调模型，可复用该范式做跨域冷启动场景的模型增强，降低域内数据需求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM推荐引入推理链后效果提升明显，但推理阶段需要生成大量中间推理token，延迟是直接推荐的6~8倍，无法满足线上推荐低延迟要求；传统知识蒸馏依赖外部更强的大模型作为teacher，不仅调用成本高，还存在师生能力gap导致推理知识无法有效迁移的问题。

### 方法关键点
- 两阶段同基座训练：第一阶段用GRPO训练和推荐模型同基座的reasoner，以下游推荐准确率作为奖励，生成适配任务的推理理由，同时对理由中与商品标题重叠的内容做掩码避免信息泄露，输入带理由的模型作为teacher；
- 自蒸馏对齐：student与teacher共享基座，student输入不含推理理由，对齐teacher的输出logits，采用反向KL作为蒸馏损失，聚焦teacher高置信度的分布区域；
- 动态加权策略：根据teacher对正样本的排名、师生对正样本的排名差自适应调整蒸馏损失权重，当teacher表现差于student时自动降低权重，过滤噪音信号。

### 关键结果
在Clothing、Home、ML1M三个公开数据集上对比14个基线（传统重排、无推理LLM推荐、多步/单步推理LLM推荐），ML1M数据集HR@1达0.0845，较次优基线提升12.2%；推理延迟与无推理的SOFT基线持平，较推理类基线低6~8倍；同基座训练的reasoner效果优于GPT-4o-mini、Claude-3-Haiku等外部大模型，对应teacher的HR@1较GPT-4o-mini高32.7%。

**最值得记住的话**：无需依赖外部大模型作为teacher，同基座的推理增强自蒸馏就能同时拿到推理的效果增益和直接推荐的低延迟。
