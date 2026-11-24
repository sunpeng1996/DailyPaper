---
title: 'MADRec: Reliable Multi-Agent Reasoning with Evidence-Grounded Debate for Recommendation'
title_zh: MADRec：基于证据支撑辩论的可靠多智能体推理推荐系统
authors:
- Zunlong Liu
- Weijie Feng
- Jingzhi Li
- Lei Zhu
- Zhiyong Cheng
- Meng Wang
affiliations:
- 合肥工业大学
- 同济大学
arxiv_id: '2611.28604'
url: https://arxiv.org/abs/2611.28604
pdf_url: https://arxiv.org/pdf/2611.28604
published: '2026-11-21'
collected: '2026-11-24'
category: Agent
direction: 多Agent推荐 · 错误传播抑制
tags:
- MultiAgent
- LLM4Rec
- Debate
- EvidenceGrounding
- Ranking
one_liner: 提出证据支撑的多智能体辩论推荐框架，解决多Agent协作的错误传播问题
practical_value: '- 多Agent分角色设计可直接复用：拆分为交互行为Agent和内容语义Agent双视角打分，避免单Agent对单一信号的偏好偏差，适配电商/内容场景多源信号融合需求

  - 语义推理加证据校验的trick可落地：离线构建商品/内容的属性、详情、评价等结构化证据库，在线用轻量微调的DeBERTa校验语义Agent的判断和证据的一致性，调低无证据支撑的候选得分，大幅降低LLM幻觉导致的排序错误

  - 多通路排序融合方案可借鉴：辩论结束后由Judge Agent根据两路Agent的辩论表现自适应分配融合权重，比固定权重融合的NDCG提升明显，可直接套用到现有多通路精排的融合环节

  - 架构兼容性强：采用「传统召回+Agent精排」的两阶段设计，可直接在现有推荐系统的召回链路后插入该精排模块，无需重构原有召回链路，改造成本低'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多Agent推荐框架大多缺乏对中间推理结果的可靠性校验，上游Agent的错误判断会无约束向下游传播，最终拉低推荐效果；已有的辩论优化机制要么是单向反馈，要么仅做候选列表选择，无法纠正所有列表共有的候选排序错误，且语义Agent的推理易出现无证据支撑的幻觉，进一步放大错误。
### 方法关键点
- 采用两阶段 pipeline：先使用预训练的传统推荐模型（SASRec/BERT4Rec）做召回，生成Top30候选集，再通过多Agent模块做精排，兼顾 scalability 和推理可靠性
- 三大核心模块协同：1）**MAD 辩论模块**：交互Agent基于用户历史交互信号排序，语义Agent基于物品内容语义排序，多轮双向辩论互相校验，修正各自的候选排序；2）**EG-RAR 证据推理模块**：离线构建物品全属性证据库，在线将语义Agent的判断与召回证据做匹配，用微调的DeBERTaV3校验主张与证据的一致性，调整语义排序得分；3）**JRC 校准模块**：基于辩论过程的可靠性信号，自适应给两路排序结果分配权重，生成最终排序。
### 关键实验
在ML-1M、Amazon Beauty、Amazon Book三个公开数据集上，对比SASRec、ChatRec、MACF、RecPO等20+基线，相比最优非MADRec基线，Recall@10提升14.15%~32.79%，NDCG@10提升10.31%~23.19%；中间错误修正率达87.9%，错误留存率仅1.8%，对30%噪声的交互数据表现出强鲁棒性。
### 核心结论
多Agent协作的推荐效果上限，很大程度取决于中间推理的可校验性，而非单纯增加Agent数量或推理轮次。
