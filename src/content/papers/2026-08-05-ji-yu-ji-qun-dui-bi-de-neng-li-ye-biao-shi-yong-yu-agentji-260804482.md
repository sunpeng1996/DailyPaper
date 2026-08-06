---
title: 'Skills Know Their Neighbors: Cluster-Contrastive Capability Pages for Skill
  Retrieval'
title_zh: 基于集群对比的能力页表示用于Agent技能检索
authors:
- Zifei Wang
- Wei Wen
- Qiang Ji
- Ruizhi Qiao
affiliations:
- Tencent IMA Product Center
- Tencent Youtu Lab
arxiv_id: '2608.04482'
url: https://arxiv.org/abs/2608.04482
pdf_url: https://arxiv.org/pdf/2608.04482
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent技能检索 · 集群对比表示
tags:
- Skill Retrieval
- LLM Agent
- Contrastive Representation
- Offline Compilation
- Routing
one_liner: 离线构建带正负边界的技能能力页表示，无需修改线上模型即可全链路提升Agent技能检索效果
practical_value: '- 技能/工具库检索场景可直接复用三字段表示：正触发T+（适用场景）、负边界T-（明确不适用的易混淆场景）、核心区分点B，无需改动线上检索模型即可快速提效，尤其适合电商客服Agent、智能运营工具库等易出现功能混淆的场景

  - 可采用双视图部署方案：检索索引仅用T+、B和原始文档，避免负样本污染向量相似度，路由阶段再展示T-做候选间对比，平衡召回准确率和排序区分度

  - 离线编译可复用聚类+对比生成的流水线：先对存量技能/商品/工具做语义聚类，再调用大模型批量生成区分性字段，新增内容仅需重编译对应集群，工程代价低

  - 可迁移到电商同款/相似品召回区分场景：给商品补充正适用人群/场景、负易混淆款区分说明，降低相似款误召回率，不需要改动现有召回排序模型'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Agent技能检索误差不完全来自检索模型能力不足：功能完全不同的相似技能（如不同公式的医学计算器、生成/读取图表工具）的文档表述高度重合，仅优化编码器或排序模型无法弥补文档本身缺失的区分信息，存在天然的误差下界。
### 方法关键点
- 定义三字段Capability Page结构：正触发`T+`（技能适用的查询场景）、负边界`T-`（明确不适用的易混淆技能边界）、核心区分点`B`（技能独有的核心规则）
- 离线集群对比编译：先对全量技能做语义聚类，再调用大模型对比同集群内技能批量生成三个字段，无需人工标注
- 双视图部署：召回索引仅用`T+`、`B`和原始文档，避免负描述污染向量相似度；路由阶段给决策模型展示`T-`做候选对比，提升排序准确率
### 关键实验
- 基于26262个技能的SRA-Bench测试，5种主流检索器（BM25、BGE-M3、Qwen3-Embedding系列）的Recall@10平均提升2.94点，BM25最高提升7.63点
- 端到端执行阶段，加入`T-`字段后4款不同量级执行器的任务成功率平均提升3.62点
- 中文SSL-SkillDiscovery数据集上，固定编码器无需微调即可达到73.07% MRR@50，比原始描述基线提升6.57点
### 核心结论
技能检索的瓶颈不止在检索模型，优化被检索的文本表示往往能以极低的线上改造成本获得远超模型迭代的收益。
