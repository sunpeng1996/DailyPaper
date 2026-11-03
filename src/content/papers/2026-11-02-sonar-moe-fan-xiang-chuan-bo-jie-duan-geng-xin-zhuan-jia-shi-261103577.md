---
title: 'Sonar-MoE: In-Backward Expert Updates for Memory-Efficient Mixture-of-Experts
  Training'
title_zh: Sonar-MoE：反向传播阶段更新专家实现内存高效MoE训练
authors:
- Avni Mittal
- Avinash Anand
- Ashutosh Kumar
- Dikshant Kukreja
- Kritarth Prasad
- Chaitanya Lakhchaura
- Rishitej Reddy Vyalla
- Erik Cambria
- Zhengkui Wang
- Rajiv Ratn Shah
affiliations:
- Microsoft India
- Singapore Institute of Technology
- Indian Institute of Technology Kanpur
- Indian Institute of Technology Delhi
- Nanyang Technological University
arxiv_id: '2611.03577'
url: https://arxiv.org/abs/2611.03577
pdf_url: https://arxiv.org/pdf/2611.03577
published: '2026-11-02'
collected: '2026-11-03'
category: Training
direction: MoE训练 · 显存与效率优化
tags:
- MoE
- Training Efficiency
- Memory Optimization
- Backpropagation
- Fine-tuning
one_liner: 反向传播时即时更新批量专家张量释放梯度，MoE训练显存降19%-22%、步速提17%-23%
practical_value: '- 业务侧微调MoE基座（如生成式推荐、多Agent调度MoE）时可直接复用该方案，无需改动训练逻辑，小批量场景下即可获得20%左右显存降低与训练提速收益

  - 实现时必须给整层批量专家张量挂更新钩子，不要给单个专家分别挂钩子，可避免20%~72%的不必要训练减速

  - 该方案可与8-bit AdamW、LoRA等现有显存优化技术叠加使用，搭配8-bit AdamW可将7B级MoE微调显存压缩到30GB以内，适配消费级GPU

  - 仅在梯度积累步数A=1的场景下使用，A≥2时会改变优化逻辑且带来5%~35%的训练减速，不建议使用'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
MoE模型90%以上参数属于专家层，标准训练需保留所有专家梯度直到优化器执行，显存开销随专家数线性增长，小批量微调场景下专家梯度显存占比甚至决定模型能否单卡运行；现有全参数反向更新方案会丢失全局梯度裁剪能力，未适配MoE结构特性。
### 方法关键点
- 仅对每层的两个批量专家张量（上投影、下投影）挂载PyTorch梯度累积后钩子，梯度就绪后立刻执行AdamW更新并释放梯度，显存中最多仅保留1层专家梯度，非专家参数仍保留标准全局梯度裁剪流程
- 选择批量张量而非单个专家挂载钩子，将每层钩子调用次数从2E（E为专家数）降至2，避免大量回调的额外开销
- 仅在无梯度积累（A=1）场景下使用，更新结果与不裁剪专家梯度的标准训练位元完全一致
### 关键实验
在Alpaca数据集微调OLMoE-1B-7B、Granite-3.1-3B-A800M两个MoE模型，对比标准全局梯度裁剪训练：
- 峰值显存降低19%~22%，单步训练时长缩短17%~23%，测试集损失与基线差值<0.003，下游任务精度无显著下降
- 搭配8-bit AdamW可将OLMoE微调峰值显存压缩至30GB以内，适配32GB消费级GPU
### 核心结论
仅针对占绝大多数参数的MoE专家层做反向更新，即可获得接近全参数反向更新的显存收益，同时保留非专家参数的全局梯度裁剪能力
