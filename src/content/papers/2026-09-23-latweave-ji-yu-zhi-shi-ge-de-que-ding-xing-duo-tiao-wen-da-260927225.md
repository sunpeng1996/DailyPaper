---
title: 'Meet, Compare, or Abstain: LatWeave for Deterministic Multi-Hop Question Answering
  on Knowledge Lattices'
title_zh: LatWeave：基于知识格的确定性多跳问答框架
authors:
- Yuze Ren
- Shaoheng Fan
- Tao Wang
- Yabo Yan
- Han Han
affiliations:
- ZenSmart Technology (Beijing) Co., Ltd.
arxiv_id: '2609.27225'
url: https://arxiv.org/abs/2609.27225
pdf_url: https://arxiv.org/pdf/2609.27225
published: '2026-09-23'
collected: '2026-09-24'
category: Reasoning
direction: 确定性推理 · 知识格多跳问答
tags:
- Multi-hop QA
- Knowledge Lattice
- Deterministic Reasoning
- Structural Abstention
- RAG
one_liner: 将LLM限制在知识构建与查询规划侧，通过三种格算子实现零LLM、可审计的确定性多跳问答
practical_value: '- 电商/广告场景的规则化召回/审核可复用该架构：将商品/用户的结构化属性映射为多维知识格，用`meet`算子做多条件组合召回，全程可审计、零幻觉，在线执行p95时延<50ms，比RAG+LLM生成结果更稳定可靠

  - Agent的工具调用逻辑可拆分LLM角色：仅用LLM做用户query到结构化执行计划的语义解析，实际执行路径用确定性算子完成，既利用LLM的语义理解能力，又避免执行阶段的幻觉、不可控问题

  - 需拒答的业务场景可复用结构化拒答机制：不需要依赖LLM置信度阈值调优，当约束冲突/无匹配数据时直接确定性拒答，IIRC数据集上拒答准确率0.971、漏答率0.029，远优于传统置信度阈值方案'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多跳QA系统（包括原生LLM、RAG、KBQA）存在两大核心痛点：一是回答生成依赖概率计算，幻觉无法根除，证据链无法实现机制级审计；二是无匹配信息时仍强行输出答案，缺乏可靠的拒答能力，两类问题根源均为推理路径是概率黑盒，无法逐条复现验证。
### 方法关键点
- 架构拆分LLM权责：仅离线阶段用LLM从文本抽取带来源标注的结构化谓词，构建多维知识格；在线阶段仅用LLM将自然语言query解析为结构化执行计划，回答路径全程零LLM调用、零任务训练
- 定义三种确定性格算子：`meet` 做多维度约束交集匹配返回完整候选集，`compare` 实现格序下的比较、极值选择等操作，`abstain` 在约束冲突/无匹配结果时直接确定性拒答，所有操作均可逐条复现
- 构建阶段降噪：通过滑动窗口抽取、哈希去重、维度白名单归一化，将LLM抽取的不确定性完全隔绝在知识构建阶段，不流入在线回答路径
### 关键实验
在6个公开基准测试：1）知识完备的MetaQA数据集（39093条测试），任意跳数any-hit达0.9975，与全监督KBQA效果持平，3跳性能几乎无衰减；2）模板化多跳的2WikiMultihopQA数据集，EM达0.865，远高于同条件下GraphRAG的0.514、HippoRAG 2的0.650；3）信息不完备的IIRC数据集，结构化拒答准确率0.971，漏答率仅0.029；4）开放域多跳的HotpotQA、MuSiQue等数据集性能下降，归因于上游文本抽取覆盖率不足、多跳query解析误差，与格算子本身无关。
### 核心结论
确定性推理不需要替代LLM，而是可以把回答路径从概率黑盒升级为可审计的白盒，在规则明确、数据结构化的场景下兼顾LLM的语义理解能力与确定性系统的可靠性、低时延优势
