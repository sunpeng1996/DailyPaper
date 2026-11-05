---
title: On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation
title_zh: 后RL能力整合阶段单/多教师On-Policy蒸馏的泛化局限性研究
authors:
- Yichen Wang
- Yufa Zhou
- Siqi Zhu
- Haozheng Luo
- Jingzhi Bao
- Zhichao Liu
- Zijun Wei
affiliations:
- University of Chicago
- Duke University
- UIUC
- Northwestern University
- ByteDance
arxiv_id: '2611.05609'
url: https://arxiv.org/abs/2611.05609
pdf_url: https://arxiv.org/pdf/2611.05609
published: '2026-11-02'
collected: '2026-11-05'
category: Training
direction: 大模型训练 · On-Policy蒸馏泛化优化
tags:
- On-Policy Distillation
- MOPD
- OOD Generalization
- Post-RL Consolidation
- Knowledge Distillation
one_liner: 揭示单/多教师On-Policy蒸馏的OOD泛化缺口，提出几何修补与基模型保留回放两种缓解方案
practical_value: '- 做电商Agent、生成式推荐的模型蒸馏时，不能仅关注分布内（IND）指标，必须补充OOD、多能力组合任务评估，避免IND满分但真实场景泛化失效

  - 若需通过蒸馏整合多域能力（如搜索语义理解+推荐个性化+客服Agent能力），优先选择MOPD而非混合RL，平均OOD遗忘可降低28.92%

  - 缓解蒸馏OOD遗忘可直接复用两种落地方案：蒸馏时混入10%左右跨域回放数据对齐基模型，或蒸馏后用Procrustes注意力修补恢复OOD性能，两种方案IND损失均小于1%'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
多教师On-Policy蒸馏（MOPD）是当前后RL阶段整合多域专家能力的主流方案，过往研究仅关注其近满分的分布内（IND）蒸馏效果，忽略了真实场景中模型必须处理超出训练分布的任务、组合多种独立能力的需求，泛化性盲区可能导致业务上线后效果不达预期。
### 方法关键点
- 实验基座采用Qwen3系列模型，覆盖两类教师设置：从同一基模型微调的自RL专家教师、外部高性能通用大模型教师
- 设计两类泛化测试范式：extrapolative generalization（同域内超出训练难度的任务）、compositional generalization（需组合多种已训练独立能力的任务）
- 提出两种可落地的优化方案：蒸馏后基于Procrustes对齐的注意力几何修补、蒸馏过程中加入基模型监督的跨域回放数据
### 关键实验结果
对比单教师OPD、多教师MOPD、混合RL、单任务RL四类方案：
1. OPD/MOPD的IND性能达到对应教师的96.04%~102.73%，但OOD性能比基模型低2.45%~16.25%
2. 组合任务场景下MOPD的IND性能比基模型高0.48%~22.46%，但组合任务OOD性能比最优教师低18.19%~24.34%
3. 同时优化教师能力与训练数据覆盖后可完全消除OOD遗忘，基模型保留回放方案在5/8的OOD benchmark上实现性能提升，IND仅下降0.18%
### 最值得记住的结论
近满分的分布内蒸馏性能完全可能掩盖严重的能力整合不足，做模型蒸馏时必须同时监控OOD与多能力组合任务的性能。
