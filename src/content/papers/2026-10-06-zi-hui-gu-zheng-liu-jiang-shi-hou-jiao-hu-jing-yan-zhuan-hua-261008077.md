---
title: 'Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight'
title_zh: 自回顾蒸馏：将事后交互经验转化为事前预判能力
authors:
- Haoxiang Zhang
- Qinglin Chen
- Hiroaki Hayashi
- Zhuofeng Li
- Siming Zhang
- Jiaxin Zhang
- Jixuan Chen
- Fang Wu
- Pan Lu
- Silvio Savarese
affiliations:
- Salesforce AI Research
- UC San Diego
- Texas A&M University
- Stanford University
arxiv_id: '2610.08077'
url: https://arxiv.org/abs/2610.08077
pdf_url: https://arxiv.org/pdf/2610.08077
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: Agent 自回顾蒸馏训练优化
tags:
- Self-Retrospection Distillation
- RLVR
- Agent Training
- Sparse Reward
- Prospective Learning
one_liner: 提出自回顾蒸馏辅助目标，在奖励无差异场景下仍可从Agent交互轨迹提取有效学习信号
practical_value: '- 电商导购、搜索推荐类Agent做RL训练时，常遇到全成功/全失败的奖励无差异批次（占比37%~98%），可叠加SRD辅助损失，从失败轨迹蒸馏预判坑点、成功轨迹蒸馏所需知识，无需丢弃无差异批次，大幅降低采样成本

  - 现有GRPO、OPSD等Agent训练框架可无侵入接入SRD，仅需额外加权重为0.01的轻量辅助损失，无需修改推理逻辑，即可在多步交互场景（如多轮导购、复杂query拆解）获得最高24.2pp的效果提升

  - 工程落地优先选择仅蒸馏PITFALL（失败坑点）通道，比同时蒸馏知识+坑点的rollout耗时低10%左右，效果更稳定，不会出现性能退化；推理阶段无需显式生成预判内容，无额外推理延迟

  - 推荐系统的LLM排序、生成式推荐模块训练时，若用户反馈稀疏，可借鉴SRD思路，将点击/转化后的事后反馈蒸馏为事前对用户需求的预判，缓解样本浪费问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
基于可验证奖励的强化学习（RLVR）是当前LLM Agent的主流训练范式，但当同一任务的多轮采样轨迹奖励完全一致（全成功/全失败，尤其常见于长周期任务、弱模型阶段）时，组间相对奖励优势为0，轨迹携带的大量结构化信息被完全浪费；现有自蒸馏方法也仅用事后信息优化动作策略，未挖掘事前预判的学习价值。
### 方法关键点
- 提出前瞻性学习范式：将交互完成后获得的结构化事后信息（成功经验/失败坑点）作为监督信号，训练Agent在交互前仅用任务上下文就能预判对应信息，预判内容无需在推理时显式生成
- 落地为自回顾蒸馏（SRD）辅助损失：同一模型同时作为学生和带停止梯度的教师，学生基于预交互上下文生成预判序列，教师基于完整轨迹事后信息监督学生的token级分布对齐，成功轨迹对应知识预判、失败轨迹对应坑点预判
- 可无缝接入GRPO、OPSD、RLSD等现有训练目标，仅需添加权重为0.01的SRD辅助损失，无额外推理开销
### 关键结果
在数学、代码、搜索、WebShop/ALFWorld交互任务等10个工具推理、长周期Agent基准上验证：
- SRD为各类基线带来最高24.2pp的绝对性能提升；当98%的采样组为全失败无奖励差异时，纯RLVR训练最终成功率为0%，添加SRD后成功率达60.6%
- 仅蒸馏PITFALL（失败坑点）通道比同时蒸馏知识+坑点的rollout耗时低10%左右，效果更稳定，无性能退化
### 核心结论
奖励只决定轨迹提供什么类型的监督，而非是否能提供监督，无奖励差异的轨迹依然可以用来训练Agent的事前预判能力，大幅降低采样浪费。
