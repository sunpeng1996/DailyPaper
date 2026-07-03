---
title: Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention
  in Vision-Language-Action Models
title_zh: 视觉-语言-动作（VLA）模型的常识与世界知识留存能力度量
authors:
- Nikita Kachaev
- Andrey Moskalenko
- Matvey Skripkin
- Nikita Kurlaev
- Daria Pugacheva
- Albina Burlova
- Mikhail Kolosov
- Denis Shepelev
- Andrey Kuznetsov
- Elena Tutubalina
affiliations:
- CogAI Lab
- FusionBrain Lab
- HSE University
- Lomonosov MSU
- NUST MISIS
arxiv_id: '2606.19297'
url: https://arxiv.org/abs/2606.19297
pdf_url: https://arxiv.org/pdf/2606.19297
published: '2026-06-16'
collected: '2026-07-03'
category: Eval
direction: 具身Agent · 知识留存评估
tags:
- VLA
- Embodied Agent
- Knowledge Retention
- Model Evaluation
- Layer Probing
one_liner: 提出轻量VLA评估协议Act2Answer，消除控制混淆度量其常识与知识留存，实现分层探测定位知识分布
practical_value: '- 开发电商具身导购Agent、仓储作业Agent时，可复用Act2Answer「动作映射答案」的评估思路，避免控制能力混淆知识能力的评估偏差

  - 微调多模态具身Agent时，新增VQA co-training任务可以显著提升预训练知识留存率，减少微调后的知识遗忘

  - 做多模态Agent知识增强时，可参考分层探测结论，仅对中间层做LoRA轻量微调，不需要修改上层动作头，兼顾知识保留和动作性能'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
VLA模型通常由预训练VLM在机器人数据上微调得到，但微调后常识、事实知识的留存程度不明确，原有知识敏感任务的失败原因会混淆「知识缺失」和「底层控制泛化差」两个独立问题，无法准确定位根因。
### 方法关键点
1. 提出Act2Answer轻量评估协议，将VLM知识基准适配为VLA可执行的桌面任务，Agent通过单步物体放置动作选择候选答案，得到消除控制变量混淆的动作grounded成功率；
2. 构建覆盖多类常识、世界知识的测试套件，新增分层意图探测方法，定位答案相关信息在VLM backbone和动作头的分布；
3. 完成7个SOTA VLA模型、9个VLM基线的大规模测试。
### 关键结果
VLA在简单概念任务表现稳定，但复杂语义类任务性能相比源VLM存在明显差距；加入VQA共训的VLA知识留存率显著更高；答案相关信号在VLA中间层达到峰值，上层动作头处信号明显衰减。
