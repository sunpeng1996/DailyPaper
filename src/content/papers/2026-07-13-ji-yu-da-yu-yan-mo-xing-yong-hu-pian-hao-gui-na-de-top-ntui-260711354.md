---
title: User Preference Induction with LLMs for Offline Top-N Recommendation Evaluation
title_zh: 基于大语言模型用户偏好归纳的Top-N推荐离线评估方法
authors:
- David Otero
- Javier Parapar
affiliations:
- Universidade da Coruña
- Information Retrieval Lab, CITIC
arxiv_id: '2607.11354'
url: https://arxiv.org/abs/2607.11354
pdf_url: https://arxiv.org/pdf/2607.11354
published: '2026-07-13'
collected: '2026-07-14'
category: Eval
direction: 推荐系统离线评估 · LLM-as-a-Judge
tags:
- LLM-as-a-Judge
- Offline Evaluation
- Popularity Bias
- Top-N Recommendation
- User Profiling
one_liner: 提出两阶段LLM框架扩展推荐离线评估标注，缓解缺省负样本导致的流行度偏差
practical_value: '- 离线评估可复用两阶段LLM标注流程：先从用户交互历史生成结构化偏好文本（偏好叙事+判断规则），再基于偏好补全候选集缺失标注，大幅减少人工标注成本

  - 判断用户-候选对相关性时优先采用「归纳偏好文本+原始交互记录」的prompt组合，在MovieLens场景下可实现与人类标注的NDCG@100排序一致性达1.0，同时降低评估结果与推荐流行度的相关性约20%

  - 补全标注前先对多模型召回的Top-N结果做pooling，仅针对池内候选做LLM标注，可将推理成本降低90%以上，同时保证评估结果稳定性

  - 注意边界条件：若候选池本身强头部倾斜（如仅覆盖热门商品的场景），LLM补全标注反而会加剧流行度偏差，不适用该方法'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Top-N推荐离线评估普遍采用「缺失即负例」假设，仅基于稀疏历史交互标注计算指标，会系统性高估倾向推荐热门商品的算法效果，低估能挖掘长尾优质商品的算法价值，导致算法选型偏差，亟需低成本的相关性标注扩展方案。

### 方法关键点
- 两阶段LLM标注框架：第一阶段基于用户历史交互和商品元数据生成Induced Preference Profile（IPP），包含偏好叙事（用户稳定喜好/厌恶特征）和判断规则（不同相关度的判定标准）；第二阶段以IPP+原始交互记录为上下文，对缺失标注的用户-商品对做相关性打分
- 采用pooling机制降本：仅对多个不同推荐算法输出的Top-100候选的并集做LLM标注，无需遍历全量商品空间，评估效率更高
- 对比3种prompt策略：仅IPP、仅原始交互、IPP+原始交互，验证不同上下文对标注质量的影响

### 关键结果数字
在MovieLens 32M、Goodbooks-10K两个公开数据集上，对比31种不同推荐算法的评估结果：
1. IPP+原始交互的prompt组合下，LLM标注与人类标注的NDCG@100排序一致性（Kendall τ）达1.0，MAE低至0.91
2. 采用LLM补全标注后，评估结果与推荐流行度的相关性最高下降20.95%，显著缓解流行度偏差
3. 边界验证：当候选池全为头部商品（如Goodbooks-10K仅包含1万本热门图书）时，LLM补全反而会小幅升高流行度相关性

### 核心结论
基于多模型召回池、搭配结构化偏好引导的LLM标注方案，能在保证评估可靠性的同时大幅缓解离线评估的流行度偏差，仅在候选池头部倾斜严重的场景下不适用
