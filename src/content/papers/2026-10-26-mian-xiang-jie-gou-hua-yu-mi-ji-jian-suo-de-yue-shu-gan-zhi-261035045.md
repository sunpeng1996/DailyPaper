---
title: 'CA-HNM: Constraint-Aware Hard Negative Mining for Dense Retrieval with Structured
  Domain Models'
title_zh: 面向结构化域密集检索的约束感知难负例挖掘框架CA-HNM
authors:
- Ngoc Luyen Le
- Marie-Hélène Abel
- Bertrand Laforge
affiliations:
- Gamaizer
- Université de technologie de Compiègne
- CNRS
- Sorbonne Université
arxiv_id: '2610.35045'
url: https://arxiv.org/abs/2610.35045
pdf_url: https://arxiv.org/pdf/2610.35045
published: '2026-10-26'
collected: '2026-10-27'
category: RecSys
direction: 密集召回 · 难负例挖掘
tags:
- Dense Retrieval
- Hard Negative Mining
- Contrastive Learning
- Dual Encoder
- Knowledge Graph
one_liner: 将领域结构化约束融入难负例筛选，无需改动推理端双编码器即可提升密集检索效果
practical_value: '- 电商/内容召回双编码器训练可直接复用框架逻辑：先取BM25+稠密召回TopK候选，再用商品类目/属性互斥/知识图谱规则过滤隐形正例，仅保留确实不兼容的难负例，避免假负例导致的模型偏移

  - 若使用Triplet Loss训练召回模型，优先搭配约束感知难负例，实验显示该组合下效果提升更稳定，NDCG@10最高可比仅按召回排序选负例的方案提升9个百分点

  - 负例池混合策略可直接落地：将随机负例、BM25负例、稠密召回负例、约束感知负例组合使用，效果优于单一负例源，且完全不改动推理链路，落地成本极低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有密集检索的难负例筛选仅依赖检索排序或向量相似度，无法区分高相似候选中的隐形正例（如用户搜「初级SQL」时返回的「高级SQL优化」），易引入假负例导致模型训练偏差；而结构化领域知识（类目、属性、层级、关联关系）可提供额外的兼容性判断信号，且仅需在训练阶段使用，不影响推理效率，适合工业界落地。
### 方法关键点
- 候选池构造：合并BM25和稠密召回的TopK结果，先剔除标注正例得到初始候选集
- 约束判断：基于领域结构化模型（知识图谱、类目体系等）构建查询目标的局部上下文，用确定性规则判断候选兼容性，标记关系、范围、目标、层级四类不匹配
- 负例选择：支持两种模式，Pure模式仅选约束不匹配的难负例，按违规类型轮询采样避免单一类型占比过高；Mixed模式将约束感知负例与常规负例混合使用
- 训练：用筛选后的负例微调标准双编码器，结构化信息仅参与离线负例构造，不改动模型结构和推理逻辑
### 关键实验
在MOOCCubeX和Course-Skill Atlas两个教育领域数据集上，对比随机负例、稠密召回负例、排序匹配负例三种baseline，CA-HNM-Pure在8组数据集+编码器+损失的配置中有6组NDCG@10更高，搭配Triplet Loss时最多比baseline高0.091；Mixed模式比不含约束负例的混合池NDCG@10最高高0.0076。

最值得记住的一句话：约束感知难负例的效果增益高度依赖训练损失，Triplet Loss下的提升稳定性远高于多负例排序损失，且全程不侵入推理链路，落地成本极低。
