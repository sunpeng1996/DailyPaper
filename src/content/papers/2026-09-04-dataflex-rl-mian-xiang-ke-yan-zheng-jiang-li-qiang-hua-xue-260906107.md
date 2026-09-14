---
title: 'DataFlex-RL: An Evaluation Platform for RLVR Data Policies'
title_zh: 《DataFlex-RL：面向可验证奖励强化学习的数据策略评估平台》
authors:
- Hao Liang
- Mingrui Chen
- Hengyi Feng
- Meiyi Qiang
- Wentao Zhang
affiliations:
- Peking University
- UCAS
- Institute for Advanced Algorithms Research Shanghai
- Zhongguancun Academy
arxiv_id: '2609.06107'
url: https://arxiv.org/abs/2609.06107
pdf_url: https://arxiv.org/pdf/2609.06107
published: '2026-09-04'
collected: '2026-09-14'
category: Eval
direction: RL微调优化 · 数据策略评估
tags:
- RLVR
- GRPO
- Data Policy
- Evaluation Platform
- LLM Post-Training
one_liner: 推出统一GRPO协议的RLVR数据策略评估平台，实测现有策略均未显著优于均匀采样
practical_value: '- 做Agent、生成式推荐的RL微调时，优先保障基础GRPO/PPO训练链路正确性，不要盲目上线复杂数据筛选、重加权策略，均匀采样是性价比最高的初始基线

  - 跨业务场景（比如推荐的公域/私域、多品类）评估模型效果时，必须覆盖所有训练目标域，遗漏任意核心域都会导致方法排名完全反转，产生错误选型决策

  - 做算法迭代的AB实验时，必须固定训练协议、匹配种子、统计置信区间，小于1pt的效果差异大概率是随机噪声，不具备业务落地的复现性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RLVR（可验证奖励强化学习）是当前LLM推理、Agent决策能力微调的核心方案，现有大量数据筛选、重加权、自适应域混合策略宣称能提升训练效率与效果，但这类方法往往与其他训练优化耦合，未在统一协议下开展公平对比，增益是否可复现长期存疑。
### 方法关键点
- 提出DataFlex-RL评估平台，将RLVR数据策略抽象为三类独立干预：响应选择（过滤低质样本）、损失重加权（调整样本贡献权重）、训练域混合适配（动态调整不同域样本占比），实现数据策略与GRPO训练其他模块的完全解耦
- 统一实验控制协议：固定1.5万条均分的数学/逻辑/科学训练prompt、GRPO超参（每条prompt生成5个响应、KL系数1e-3、300步优化）、12项覆盖三域的评测基准，所有对比使用匹配种子控制无关变量
### 关键结果
- 主实验在Qwen2.5-7B-base上对比13种主流数据策略，12个匹配种子下，均匀GRPO相对未训练基线精度提升7.76pt；8种选择/重加权策略相对均匀采样的95%置信区间均包含0，3种自适应混合策略相对固定等比例混合也无统计显著增益，所有策略间最大分差仅0.97pt
- 扩展到Llama-3.1-8B-base、不同规模Qwen模型结论一致，无通用最优数据策略；若评测遗漏逻辑域，方法排名与全域评测的秩相关系数为-0.33，完全反转
### 核心结论
在当前主流RLVR训练范式下，复杂数据策略带来的增益大概率小于训练噪声和评测偏差，均匀采样是最可靠的基线选择
