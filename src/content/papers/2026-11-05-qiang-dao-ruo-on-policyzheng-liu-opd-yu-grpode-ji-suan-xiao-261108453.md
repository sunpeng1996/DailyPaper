---
title: Unpacking the Compute Efficiency of Strong-to-Weak OPD against GRPO
title_zh: 强到弱On-Policy蒸馏(OPD)与GRPO的计算效率拆解研究
authors:
- Zeyu Leo Liu
- Yang Li
- Bo Pang
- Emre Can Acikgoz
- Xuan-Phi Nguyen
- Anurag Koul
- Srijan Bansal
- Erik Nijkamp
- Shafiq Joty
- Semih Yavuz
affiliations:
- Salesforce AI Research
- UIUC
arxiv_id: '2611.08453'
url: https://arxiv.org/abs/2611.08453
pdf_url: https://arxiv.org/pdf/2611.08453
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: LLM后训练 · 蒸馏与RL训练效率优化
tags:
- OPD
- GRPO
- Knowledge Distillation
- Compute Efficiency
- LLM Training
- Multi-Teacher Distillation
one_liner: 系统对比OPD与GRPO的FLOPs效率，明确仅自GRPO教师+多教师融合场景下OPD具备显著效率优势
practical_value: '- 做Agent/生成式推荐微调时不要盲目用外部大模型做OPD：同等FLOPs预算下GRPO效果更优，还能避免OPD常见的响应长度膨胀、重复输出等退化问题

  - 多场景统一模型迭代可采用「单域训GRPO专家+多教师OPD融合」范式：融合2/4个域专家仅需额外5.2%/8.0%的专家训练FLOPs，总算力比联合GRPO训练低30%~42%，效果更优

  - 蒸馏前可先计算学生与教师的初始top-k token重叠率，优先选择同底座、同域GRPO微调后的checkpoint作为教师，比强外部大模型的蒸馏效率高数十倍

  - 算力受限场景快速迭代模型：用学生自身的GRPO checkpoint做OPD，仅需1/50的蒸馏阶段FLOPs即可恢复同等GRPO效果，适合小版本快速上线'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
此前大量OPD研究声称其比GRPO训练效率更高，但均采用GPU小时、训练步数等易受实现/硬件干扰的指标，没有基于FLOPs的公平对比，无法明确OPD的真实适用场景，存在工程选型误导风险。
### 方法关键点
- 统一以累计训练FLOPs作为效率衡量标准，所有实验对齐学生初始化、prompt、rollout组大小、超参数
- 覆盖三类教师设置：外部预训练大模型、GRPO微调后的外部大模型、学生自身的GRPO checkpoint（自GRPO教师）
- 新增多域融合场景测试，对比多教师OPD与联合GRPO训练的全链路效率
### 关键实验
覆盖数学、代码、知识问答、指令跟随4个域，baseline为对齐超参的GRPO：
1. 外部教师场景下，OPD在所有测试域的FLOPs效率均低于GRPO，还普遍存在响应长度膨胀、输出退化问题
2. 自GRPO教师场景下，OPD仅用1/50的FLOPs即可恢复对应GRPO checkpoint的效果，该结论跨模型大小、域、底座均成立
3. 多域融合场景下，多教师OPD融合2/4个域的GRPO专家仅需额外5.2%/8.0%的专家训练FLOPs，总FLOPs比联合GRPO训练低42%/31.6%，效果更优
### 核心结论
OPD不是GRPO的通用替代品，其核心价值是用极低算力成本将多个同底座单域GRPO专家融合为一个多域通用模型。
