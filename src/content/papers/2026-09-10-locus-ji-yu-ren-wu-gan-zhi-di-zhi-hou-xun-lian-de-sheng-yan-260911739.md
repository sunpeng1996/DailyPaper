---
title: 'LOCUS: Task-Aware Low-Rank Post-Training for Token-Efficient Language Generation'
title_zh: LOCUS：基于任务感知低秩后训练的省token语言生成方法
authors:
- Dongfang Zhao
affiliations:
- University of Washington
arxiv_id: '2609.11739'
url: https://arxiv.org/abs/2609.11739
pdf_url: https://arxiv.org/pdf/2609.11739
published: '2026-09-10'
collected: '2026-09-11'
category: LLM
direction: LLM训练优化 · 低秩适配省token
tags:
- LoRA
- DPO
- Parameter-Efficient-Fine-Tuning
- Token-Efficiency
- Preference-Alignment
one_liner: 通过选择任务感知LoRA子空间，在效用无损前提下最多削减近40%输出token，仅更新0.3%以内参数
practical_value: '- 电商客服、商品文案生成场景可直接复用LOCUS思路，不改DPO/SFT目标，仅通过调整LoRA配置（秩、目标模块、训练步长）压缩输出token长度，降低推理成本同时不影响回答质量

  - 推荐系统中LLM做query改写、用户意图理解的场景，可参考其约束选择流程，固定1pp以内的效用容忍阈值，自动筛选最短输出的LoRA配置，降低KV cache占用、提升服务并发

  - 多Agent部署场景可复用其LoRA合并部署方案，单frozen底座挂载多任务短输出adapter，既降低部署显存开销，又避免prompt加「简洁回答」带来的分布偏移问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM偏好对齐（如DPO）普遍存在冗余输出问题，生成token越长推理成本越高、KV cache占用越大，而现有加长度惩罚、加简洁prompt的方法要么降低回答质量，要么鲁棒性差，亟需不修改原有对齐目标前提下压缩输出长度的方案。

### 方法关键点
- 冻结预训练底座，仅更新LoRA参数，不修改原生偏好对齐（DPO/DrDPO/SamPO）目标，无额外长度正则或prompt修改
- 构造LoRA候选网格，变量包含秩r、缩放系数α、目标模块、适配层数、训练步长
- 基于验证集做约束选择：先筛选效用不低于基线-1pp的候选，再选其中输出token最短的配置，有条件可加二次验证集确认避免过拟合
- 部署时可将LoRA权重合并到底座，无额外推理开销

### 关键结果
在Anthropic HH-RLHF数据集上测试，对比全参数DPO/DrDPO、SamPO基线：Pythia-2.8B上最多减少39.84%输出token，Qwen2.5-3B上最多减少17.58%输出token，参数更新量仅0.24%~0.28%，偏好精度损失不超过0.13pp；跨任务测试在Orca指令数据集上甚至实现80%token削减同时偏好精度提升13.67pp。

LoRA不只是节省训练成本的参数高效方法，其适配子空间本身可作为调控模型生成行为的设计变量，在不改训练目标的前提下实现输出长度等属性的优化。
