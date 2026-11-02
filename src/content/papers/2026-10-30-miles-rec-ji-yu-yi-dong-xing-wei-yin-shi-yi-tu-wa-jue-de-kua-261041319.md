---
title: 'MILES-Rec: Uncovering Implicit Intents from Mobility Behaviors for Cross-Domain
  POI Recommendation'
title_zh: MILES-Rec：基于移动行为隐式意图挖掘的跨域POI推荐框架
authors:
- Yi Zou
- Wei Luo
- Xuewen Zhang
- Zhuang Yan
- Pengjie Wang
affiliations:
- Alibaba Group, AMAP
arxiv_id: '2610.41319'
url: https://arxiv.org/abs/2610.41319
pdf_url: https://arxiv.org/pdf/2610.41319
published: '2026-10-30'
collected: '2026-11-02'
category: RecSys
direction: 跨域POI推荐 · LLM隐式意图推理
tags:
- Cross-domain Recommendation
- POI Recommendation
- Implicit Intent Mining
- LLM4Rec
- GRPO
one_liner: 提出两阶段LLM训练框架，从用户移动行为生成优先级查询实现跨域POI推荐
practical_value: '- 跨域推荐可复用「用户行为→自然语言查询→目标域召回」的语义桥架构，解决源域与目标域无直接item重叠的冷启动问题，比如到店电商可从用户导航/搜索行为推断线下消费意图

  - 列表式生成优化可借鉴双层credit分配机制：全局列表奖励优化覆盖率、冗余度，局部token级奖励优化单个查询/物料的相关性，适配搜索推荐的列表式产出场景

  - 小模型垂直场景落地可复用「SFT先学结构化推理逻辑+GRPO用业务反馈调优业务目标」的两阶段范式，4B小模型经优化后POI召回效果可超过通用大模型

  - 冷启动场景可复用特征组合策略：稀疏行为场景下补充用户静态属性可有效提升意图推理准确率，降低行为数据不足的负面影响'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
地图应用的移动行为（导航、路线规划等）与本地服务POI分属两个独立域，传统POI推荐仅预测用户下一个空间目的地，忽略移动行为附带的衍生消费需求（如前往公园的用户需要周边亲子餐饮、停车场等服务），且跨域下源域移动行为与目标域POI无直接item重叠，稀疏行为场景下难以建模用户隐式消费意图，通用LLM无法直接适配该跨域推理场景。
### 方法关键点
- 两阶段训练范式：第一阶段做渐进式推理SFT，构造1.9万条经人工校验的Chain-of-Thought演示，拆解为情境理解、意图扩展、查询优先级排序三个步骤，引导LLM从用户静态属性+移动历史生成带优先级的服务查询
- 意图对齐GRPO优化：构造包含查询相关性、服务覆盖率、冗余惩罚、长度惩罚的复合奖励函数，设计双层credit分配机制：全局列表级优势优化整体结构与覆盖度，局部查询级优势针对性优化单个查询的相关性
- 配套数据集与评估：构建MILES-Bench真实用户数据集，覆盖10个城市的富/稀疏行为用户，包含200万POI检索池，配套POI检索效用、服务意图对齐、语义需求对齐三类评估指标
### 关键结果
在MILES-Bench上对比GPT-4o、DeepSeek-v4等通用大模型，以及GLoSS、Rec-R1等推荐基线：27B版本在富行为测试集上语义需求对齐（SDA）达72.19%，4B版本Hit@50达3.4%，较SFT阶段提升126%；GRPO优化在4个不同参数规模的基线上均带来一致性效果提升，4B小模型效果超过多数通用大模型。
> 最值得记住：跨域推荐场景下，用可解释的自然语言查询作为源域行为到目标域推荐的语义桥，配合业务反馈的RL优化，可在小参数规模下实现优于通用大模型的业务效果。
