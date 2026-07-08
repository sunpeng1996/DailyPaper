---
title: 'From Voting to Agent Collaboration: Answer-Type-Aware LLM Pipelines for BioASQ
  14b'
title_zh: 面向BioASQ 14b的回答类型感知LLM流水线：从投票到多Agent协作
authors:
- Taeyun Roh
- Eunha Lee
- Wonjune Jang
- Sohyun Chung
- Junha Jung
- Jaewoo Kang
affiliations:
- 高丽大学
- 明知大学
- AIGEN Sciences
arxiv_id: '2607.06452'
url: https://arxiv.org/abs/2607.06452
pdf_url: https://arxiv.org/pdf/2607.06452
published: '2026-07-07'
collected: '2026-07-08'
category: MultiAgent
direction: 多Agent协作 · 垂直领域QA优化
tags:
- MultiAgent
- LLM
- CoT
- Prompt Engineering
- Ensemble
one_liner: 针对生物医学三类QA问题定制LLM推理与多Agent协作流程，获BioASQ 14b factoid子任务第一
practical_value: '- 可复用「任务路由+分场景定制策略」架构：电商场景下可对不同query类型（是非判断、实体查询、列表召回）分别设计推理流程，效果优于通用策略

  - 不确定样本的选择性Agent校验技巧：对多模型投票不一致的case才启动高成本Agent校验流程，平衡效果和算力成本，适合大流量业务落地

  - 列表类召回任务的四阶段Agent流水线（证据提取→生成→校验→监督）可直接迁移到商品/内容列表生成、属性拉取等场景，同时提升准确率和召回率

  - 检索式ICL+多模型共识过滤的设计，可用于电商实体识别、属性标准化等场景，降低输出偏差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
生物医学QA需要从分散文献中提取并跨文档整合证据，现有通用LLM推理策略存在对证据顺序敏感、冲突证据处理能力弱、易产生幻觉等问题，且不同类型问题（是非、事实、列表）的推理需求和评估标准差异极大，单一策略无法覆盖所有场景，需针对性设计流程提升答案鲁棒性和证据支撑性。

### 方法关键点
- 前置问题类型路由模块，对三类问题分别定制推理流程：是非类问题采用snippet洗牌+多LLM多次推理+多数投票，投票不一致时触发证据分类+Agent二次校验
- 事实类问题用检索式CoT ICL（基于BioBERT召回语义相似的训练样本作为示例）+多LLM全片段输入推理，结果按投票数共识过滤后排序输出
- 列表类问题采用四阶段多Agent协作架构：证据分析Agent提取候选实体与相关证据→推理Agent生成候选答案列表→校验Agent检查实体的证据支撑性、完整性、去重→监督Agent综合所有报告输出最终结果

### 关键结果数字
在BioASQ 13b数据集上完成策略选型后，在官方BioASQ 14b Task B竞赛中测试，平均成绩：是非题macro F1 0.9110，事实题MRR 0.4626，列表题F1 0.4439，其中Batch 4事实题MRR达0.5758，排名该子任务第一。

### 核心结论
针对细分任务类型定制推理+Agent协作流程，比通用大模型单轮推理的效果和鲁棒性都有显著提升
