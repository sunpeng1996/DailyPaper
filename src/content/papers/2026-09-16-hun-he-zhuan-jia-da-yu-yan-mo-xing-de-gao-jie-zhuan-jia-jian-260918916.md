---
title: Higher-order pruning of experts in mixture-of-experts language models
title_zh: 混合专家大语言模型的高阶专家剪枝方法HOPE
authors:
- Alex M. Tseng
- Prannay Kaul
- Luca Zancato
- Wei Xia
- Stefano Soatto
affiliations:
- AWS Agentic AI
- AI Fundamental Research
arxiv_id: '2609.18916'
url: https://arxiv.org/abs/2609.18916
pdf_url: https://arxiv.org/pdf/2609.18916
published: '2026-09-16'
collected: '2026-09-17'
category: Training
direction: 大模型压缩 · MoE高阶专家剪枝
tags:
- MoE
- Expert Pruning
- Model Compression
- LLM Inference
- Agent LLM
one_liner: 引入专家交互二阶信息的MoE剪枝方法，高剪枝率下Agent任务性能显著优于现有SOTA
practical_value: '- 业务侧如果使用MoE大模型部署电商Agent（智能客服、商品文案生成、推荐理由生成、用户意图理解），可直接复用HOPE做40%-50%比例的专家剪枝，省下的显存可分配给KV
  cache提升上下文长度、并发量，Agent类任务的性能掉点远低于现有REAP方法，最高可少降6.1%

  - 做业务定制的MoE剪枝时，不要仅依赖单专家的激活频率、输出范数等一阶特征，可加入专家共激活的交互特征，对复杂推理类任务（比如多轮用户意图理解、营销活动方案生成）的效果保留提升明显

  - HOPE的工程落地成本极低，仅需在现有REAP的剪枝校准流程上增加共激活矩阵统计与二次规划求解步骤，无需额外微调剪后模型即可上线，校准时间仅比REAP高6%-7%'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
MoE大语言模型已成为SOTA大模型的主流架构，但全部专家需常驻GPU内存，与KV cache抢占显存，严重限制部署的并发量、上下文长度与Agent工具调用能力。现有一阶专家剪枝方法独立评估单专家重要性，忽略专家天然的协作特性，高剪枝率（40%-50%，也是落地收益最高的区间）下会大量破坏专家协同结构，导致性能暴跌。
### 方法关键点
- 推导HOPE二阶剪枝目标，可证明最小化剪枝误差上界，将专家两两共激活的交互信息纳入决策，构造每层E×E交互矩阵F：对角线对应单专家重要性，非对角线对应专家对的协同贡献
- 证明SOTA一阶剪枝方法REAP是HOPE忽略交互项的特例
- 工程实现仅需在剪枝校准的前向传播时额外统计专家共激活数据，通过二次规划松弛求解每层剪枝集合，每层QP求解仅需1-2秒，额外开销可忽略，无需后续微调
### 关键实验
在3款公开MoE模型（最大122B参数）、2类校准集、6种剪枝率、涵盖数学、代码、Agent任务的多基准上对比REAP、EAN、MAN等4个SOTA基线：
- 全场景平均排名2.07为最优，50%高剪枝率下平均排名1.58，优于次优REAP的2.42，Agent编码任务相对REAP最高提升6.1%
- 全场景头对头对比基线胜率73%，仅在1/54的场景下排名末位
### 核心结论
MoE专家剪枝需优先保留协同结构而非仅选择单专家重要性最高的个体，高剪枝率下二阶交互信息的收益尤其显著。
