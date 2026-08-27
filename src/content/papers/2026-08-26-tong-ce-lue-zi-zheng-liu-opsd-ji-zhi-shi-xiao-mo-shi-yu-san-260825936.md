---
title: 'One Symptom, Three Levers: A Critical Review of On-Policy Self-Distillation'
title_zh: 同策略自蒸馏（OPSD）机制、失效模式与三大调控杠杆综述
authors:
- Justin Robert
- Raheel Qader
affiliations:
- OVHai LLM
arxiv_id: '2608.25936'
url: https://arxiv.org/abs/2608.25936
pdf_url: https://arxiv.org/pdf/2608.25936
published: '2026-08-26'
collected: '2026-08-27'
category: Training
direction: 大模型自蒸馏训练 · 对齐优化
tags:
- OPSD
- Self-Distillation
- RL
- LLM Training
- Model Collapse
one_liner: 系统性梳理同策略自蒸馏的collapse失效机制，总结三大可操作调控杠杆与落地经验
practical_value: '- 做Agent/推理类任务自蒸馏调优时，不要直接给全量参考解当特权信息，优先选择中间抽象（步骤hint、错误反馈等），既能提升性能还能避免推理多样性collapse，可直接迁移到电商智能客服推理链、导购Agent决策逻辑的训练场景

  - 蒸馏信号不要采用全token均匀加权，高熵决策点用forward KL保留多样性，低熵确定点用reverse KL提升精度，该trick可复用在LLM4Rec的语义ID生成、推荐文案生成的蒸馏训练中

  - 自蒸馏循环的教师模型不要与学生同步更新，要么冻结初始教师，要么采用EMA慢更+奖励触发式刷新策略，避免循环漂移，可直接应用在电商搜索query改写、商品标题优化的自蒸馏微调流程'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
On-Policy Self-Distillation（OPSD）无需额外大模型作为教师，仅需GRPO 1/8的采样token量就能实现相当的数学推理/代码能力，是低成本小模型对齐的核心方案，但普遍存在推理多样性collapse、域外性能退化问题，现有分散的研究结论缺乏统一的调控框架，落地踩坑风险高。

### 方法关键点
- 以collapse为核心症状，拆解出三大独立可调控杠杆：①信号几何：蒸馏散度选择、token权重分配；②特权信息：教师侧输入的信息类型与剂量；③循环稳定性：教师更新规则、特权信息衰减调度
- 明确两类collapse成因：通用RL训练的熵侵蚀效应、OPSD特有的特权信息PMI偏差（教师预知答案后会抑制deliberation类推理token）
- 提出特权信息安全准则：仅学生推理时可自行重构的信息不会产生有害泄漏，全量参考解/最终答案是风险最高的输入，中间hint、错误对齐反馈的综合收益最优

### 关键结果
- 基准性能：原始OPSD在AIME25数学推理集上得分从36.7提升到43.9，单步训练耗时约为GRPO的2倍，但收敛步数显著更少
- 优化收益：采用错误对齐critique作为特权信息，比全参考解OPSD提分+5.27，比GRPO提分+16.11；高熵token选择性加权方法仅增加4.5%计算开销，即可显著缓解推理多样性下降
- 风险数据：全参考解作为特权信息会让思维模型的avg@16最高下降17%，pass@1提升的同时pass@16最多下降5.1个百分点

**最值得记住的一句话**：同策略自蒸馏的核心是让学生学会教师的推理能力，而非复制答案，信号的选择性永远比密度更重要。
