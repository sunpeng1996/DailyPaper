---
title: 'DecisionRank: On-Policy Distillation for Decision-Model Rerankers'
title_zh: DecisionRank：面向决策型重排器的同策略蒸馏方法
authors:
- Yanran Wu
- Dian Yu
- Chongyang Bai
- Jieyi Zhang
- Rui Liu
- Tianyi Chen
- Shike Mei
- Hang Cui
- Frank Shyu
- Sandeep Pandey
affiliations:
- Meta
- Purdue University
arxiv_id: '2610.42128'
url: https://arxiv.org/abs/2610.42128
pdf_url: https://arxiv.org/pdf/2610.42128
published: '2026-10-30'
collected: '2026-11-02'
category: RecSys
direction: 搜索推荐重排 · 大模型知识蒸馏
tags:
- Reranking
- Knowledge Distillation
- On-Policy Learning
- Decision Model
- Inference Efficiency
one_liner: 提出item空间同策略蒸馏，将生成式大模型重排能力迁移到单token决策重排器，兼顾效果与效率
practical_value: '- 跨模型蒸馏可直接复用item空间对齐思路，无需对齐师生词汇表，适合业务场景下用任意大尺寸生成式重排模型当教师，蒸馏小尺寸线上可部署的重排模型

  - 重排器训练可组合离线RankNet损失与同策略蒸馏损失，前者提供稳定的全局排序约束，后者修正学生训练过程中的排序偏差，无需额外标注数据即可稳定提升重排效果

  - 线上高QPS重排场景可直接采用单token logits排序的推理范式，相比自回归生成排序的方案延迟降低10~25倍，完全满足电商搜索/推荐重排的性能要求

  - 同策略蒸馏无需做学生自回归rollout，仅用学生当前得分排序构造前缀、单次教师前向即可得到全部监督信号，训练成本远低于传统同策略蒸馏方案，落地门槛低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
生成式listwise重排器（如RankGPT）排序效果优异，但自回归逐token生成排序序列的模式延迟极高，完全无法适配电商/搜索等场景的高QPS重排需求。现有单token决策重排器仅用教师生成的离线静态排序做监督，无法适配学生训练过程中的预测演化，也无法利用教师的序列条件排序偏好，效果上限低；传统token级同策略蒸馏依赖自回归rollout，和单token重排的结构存在天然 mismatch，难以直接复用。

### 方法关键点
- 学生采用单token重排范式：一次前向输出每个候选对应ID的first-token logits作为排序得分，直接排序无自回归步骤，推理效率极高
- Item空间对齐：无需师生共享词汇表，仅对同一候选的选择分布做对齐，支持跨不同模型家族的蒸馏
- 同策略蒸馏损失构造：用学生当前得分排序构造top-K前缀，教师单次teacher-forced前向得到每一步剩余候选的条件分布，与学生同一步剩余候选上归一化的得分分布做reverse KL对齐，直接监督推理用的first-token得分
- 联合训练：离线RankNet损失做全局排序约束，同策略蒸馏损失做动态反馈修正，权重λ=0.1时效果最优

### 关键实验
在TREC DL19-23、BEIR、BRIGHT、R2MED四类覆盖通用、推理型检索的基准上测试，对比RankZephyr、DirectRank、Jev等主流重排器：1.7B/4B/8B参数的DecisionRank全部超过27B参数的生成式教师；8B版本比同结构listwise重排器在TREC DL快24.5倍、BRIGHT快16.7倍，nDCG@10分别高1.42/0.99个点；比纯离线RankNet训练在四个数据集稳定提升0.5~0.9个nDCG@10点。

单token决策重排器结合item空间同策略蒸馏，可以用不到1/10的参数和1/20的延迟，超过大尺寸生成式重排器的效果，是工业级高QPS重排场景的高性价比方案。
