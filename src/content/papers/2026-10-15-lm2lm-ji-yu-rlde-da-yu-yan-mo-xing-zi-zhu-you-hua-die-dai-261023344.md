---
title: Language Models Learn to Improve Language Models
title_zh: LM2LM：基于RL的大语言模型自主优化迭代框架
authors:
- Minhua Lin
- Zijun Wang
- Zewen Liu
- Zhaotian Weng
- Bing He
- Zhan Shi
- Benoit Dumoulin
- Xiang Zhang
- Suhang Wang
- Hanqing Lu
affiliations:
- The Pennsylvania State University
- UC Santa Cruz
- Emory University
- UC Santa Barbara
- Amazon
arxiv_id: '2610.23344'
url: https://arxiv.org/abs/2610.23344
pdf_url: https://arxiv.org/pdf/2610.23344
published: '2026-10-15'
collected: '2026-10-23'
category: Agent
direction: Agent 自动化AI研究与自进化
tags:
- RL
- World Model
- AutoResearch
- Self-Improvement
- DAPO
one_liner: 提出基于研究世界模型的RL框架LM2LM，低成本训练LLM生成高效模型优化方案
practical_value: '- 可借鉴RWM+On-Policy校准思路：在推荐/广告策略迭代等高试错成本场景，用离线预估模型作为RL低成本奖励信号，仅定期将高打分策略做AB实验校准，大幅降低试错开销

  - 奖励设计trick可复用：RL训练时加入有效性校验惩罚、重复方案降级、多样性加权奖励，避免生成无效/同质化的策略/文案/召回规则，提升探索效率

  - 跨场景迁移结论可参考：基于历史实验记录训练的RL策略，泛化能力显著优于单纯ICL，适合多业务线推荐系统的统一迭代优化'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent用于自动化模型研发时，RL训练依赖大量真实模型训练反馈，单轮训练GPU成本可达上千万；而用替代预估反馈又会随策略偏移出现严重高估，导致RL优化方向与真实收益脱节，难以落地。

### 方法关键点
- 采用RL训练Proposer生成LLM架构/训练优化方案，用冻结的研究世界模型（RWM）基于历史实验记录做上下文推理，预估方案收益作为RL奖励，仅需LLM调用成本，远低于真实训练
- 多维度奖励设计：对预估收益做任务级归一化+截断，加入无效方案惩罚、重复方案降级、多样性探索加权，引导高效探索
- On-Policy校准机制：定期选取当前Proposer输出的RWM高分方案做真实训练，将结果加入RWM上下文，解决策略偏移导致的预估偏差，避免奖励高估

### 关键结果
实验覆盖8个自回归/扩散模型家族，对比零样本/ICL版GPT-6-sol、SFT、RFT等基线：LM2LM微调的Qwen3.8-27B在自回归任务上Avg@4收益达17.06e-3 BPB，比带300条上下文的GPT-6-sol-ICL高177%，数据生成成本低33%；在扩散任务上负收益提案占比仅7.6%，同时可泛化到训练未见过的模型家族。

**核心结论**：世界模型低成本预估+少量高价值真实实验校准的RL范式，可大幅降低高试错成本场景的Agent迭代开销。
