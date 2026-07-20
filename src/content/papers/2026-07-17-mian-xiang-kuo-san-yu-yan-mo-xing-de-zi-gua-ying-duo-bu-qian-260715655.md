---
title: Adaptive Multi-Step Lookahead Decoding for Diffusion Language Models
title_zh: 面向扩散语言模型的自适应多步前瞻解码框架
authors:
- Yingqian Cui
- Wei Deng
- Lantao Mei
- Hang Li
- Charu C. Aggarwal
- Hui Liu
- Yue Xing
affiliations:
- Michigan State University
- Morgan Stanley
- IBM T.J. Watson Research Center
arxiv_id: '2607.15655'
url: https://arxiv.org/abs/2607.15655
pdf_url: https://arxiv.org/pdf/2607.15655
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: 扩散大模型 · 推理解码效率优化
tags:
- Diffusion Language Model
- Lookahead Decoding
- Inference Optimization
- Parallel Decoding
- DLM
one_liner: 提出AdaLook自适应多步前瞻框架，优化扩散语言模型解码的精度-效率 trade-off
practical_value: '- 生成式推荐/广告文案生成场景若采用扩散大模型，可复用AdaLook的自适应rollout逻辑：基于候选得分方差判断是否继续前瞻，比固定步长前瞻减少30%+无效计算，同时提升生成语义一致性

  - 搜索Query改写/多轮Agent路径选择场景可迁移动态分支剪枝策略：当分支出现持续低置信度时直接剪枝，优先保留稳定分支，平衡探索成本和推理效果

  - 所有大模型生成任务的超参数调优可复用其校准规则：置信度提交阈值C可随每步生成预算N做log scale调整，仅需小校准集即可拿到接近最优的精度-效率trade-off，无需全量网格搜索'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
扩散语言模型（DLM）支持并行迭代解码，比传统自回归模型具备更高的推理效率潜力，但现有前瞻解码方法普遍采用单步浅探索，仅优化即时信息增益，容易陷入局部最优路径；直接扩展为固定深度多步前瞻又会引入大量无效计算，无法适配不同样本、不同解码阶段的状态异质性，急需更灵活的多步前瞻机制优化精度-解码步数trade-off。
### 方法关键点
- 核心框架AdaLook包含两大模块：自适应rollout延续、动态分支扩展，无额外需调优的数据集专属超参数
- 自适应rollout延续：每步前瞻后计算所有候选轨迹的累计得分方差，方差低于阈值说明候选区分度不足则继续加深rollout，否则直接选择得分最高的候选提交，避免无效深层探索
- 动态分支扩展：每步rollout后独立判断每个分支是否需要重新触发前瞻，全分支需扩展时选择最高得分分支作为下一轮前瞻起点，混合状态时剪枝不稳定分支，仅保留高置信度分支继续迭代
### 关键实验
基于LLaDA-8B-Instruct、Dream-v0-Instruct-7B两个DLM backbone，在MMLU、GSM8K、MATH500、BBH四个基准上对比ETE单步前瞻、Fast-dLLM置信度解码两个baseline：同等解码步数下，AdaLook优化版比ETE优化版精度高4.5%；MATH数据集上最高精度达43.6%，比ETE高1pct、比Fast-dLLM高1.4pct；B200 GPU上beam size=4时，单步延迟仅比ETE高7%，额外开销可忽略。
### 核心结论
扩散模型解码的前瞻探索无需固定深度，基于候选得分方差做自适应截断+分支剪枝，就能用极低的额外成本获得显著的精度-效率收益。
