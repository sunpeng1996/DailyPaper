---
title: Long-Context Fine-Tuning with Limited VRAM
title_zh: 有限显存下的大模型长上下文微调方法
authors:
- Vladimir Fedosov
- Aleksandr Sazhin
- Artemiy Grinenko
- Frank Woernle
affiliations:
- BMW Group
arxiv_id: '2607.15105'
url: https://arxiv.org/abs/2607.15105
pdf_url: https://arxiv.org/pdf/2607.15105
published: '2026-07-16'
collected: '2026-07-17'
category: Training
direction: 大模型训练 · 长上下文显存优化
tags:
- Long-Context Fine-Tuning
- HGA
- QLoRA
- KV Cache
- Memory Optimization
one_liner: 结合分层全局注意力与分层KV存储，在16GB显存下将Qwen3-8B微调上下文从2K扩至16K
practical_value: '- 落地LLM4Rec、电商Agent长上下文微调时，可直接复用HGA+QLoRA方案，16GB入门专业卡就能跑16K上下文微调，大幅降低硬件成本

  - 微调后的Adapter可直接兼容原有稠密注意力推理框架，无需修改推理侧代码即可上线长上下文能力，迁移成本极低

  - 做用户长行为序列建模、超长会话推荐的LLM微调时，可复用分层KV存储+分段反向传播思路，将冷KV卸到RAM/NVMe进一步扩展上下文长度

  - 部署阶段可调优路由top-k chunk数平衡效果与性能：8个chunk即可达到接近稠密注意力的效果，KV存储节省66.9%，适配高并发推荐/广告场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
QLoRA等参数高效微调方法已大幅降低模型权重、优化器的显存占用，但稠密注意力的序列相关状态仍严重限制长上下文微调的窗口上限，16GB入门专业卡甚至无法支撑4K上下文的8B模型微调，长上下文适配成为中小团队落地LLM的核心瓶颈。

### 方法关键点
- 引入分层全局注意力（HGA）：将上下文拆分为64token chunk和8token group两级，先用chunk摘要筛选相关chunk，再用group摘要筛选相关group，仅加载选中group的精确KV做注意力计算，摘要仅用于路由不参与计算
- 结合分段反向传播（TBPTT）：将长序列拆分为2K固定段，仅当前段保留梯度在VRAM中，历史段KV detach后存入RAM/NVMe，梯度不跨段传播
- 分层KV存储架构：VRAM仅存量化模型、Adapter/优化器、当前激活段、路由选中的精确KV、全量chunk摘要和热点group摘要，冷KV下沉到RAM/NVMe，显存占用与总上下文长度解耦

### 关键实验
基于Qwen3-8B 4bit QLoRA在PG19数据集测试，对比稠密注意力微调：
1. 16GB Quadro RTX 5000卡上，稠密微调最多支持2K上下文，HGA方案可支持16K上下文，峰值显存仅15.28GB
2. 2K上下文下HGA微调速度略快于稠密（217.75 vs 207.02 token/s），微调后Adapter用稠密注意力推理的PPL仅差0.034，效果几乎无损失
3. RULER长上下文检索测试中，HGA微调的Adapter召回率与稠密微调基本一致，无检索能力损失

### 核心结论
长上下文微调的瓶颈往往不是可训练参数的显存占用，而是注意力计算和序列状态的显存开销，通过分层路由+分层存储解耦总上下文长度和GPU工作集，可以在极低显存成本下获得几乎无损的长上下文微调效果。
