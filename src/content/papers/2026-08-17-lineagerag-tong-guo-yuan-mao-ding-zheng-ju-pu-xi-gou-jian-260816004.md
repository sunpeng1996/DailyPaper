---
title: 'LineageRAG: Harnessing GraphRAG by Constructing Evidence Lineages with Source
  Grounding'
title_zh: LineageRAG：通过源锚定证据谱系构建优化GraphRAG性能
authors:
- Linyao Zheng
- Xuhang Shi
- Zhifang Mao
- Sai Zhou
- Shuaixian An
- Xiuquan Hou
- Jinze Li
affiliations:
- 北京邮电大学XiaoLab
- 西安交通大学
arxiv_id: '2608.16004'
url: https://arxiv.org/abs/2608.16004
pdf_url: https://arxiv.org/pdf/2608.16004
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: GraphRAG · 多跳检索与问答优化
tags:
- GraphRAG
- RAG
- Multi-hop Reasoning
- Evidence Grounding
- Query Decomposition
one_liner: 提出保留证据需求全链路溯源的LineageRAG，大幅提升多跳场景GraphRAG的检索与问答效果
practical_value: '- 电商搜索多跳query（如「适合敏感肌的防晒喷雾」）场景，可借鉴证据需求拆解思路，拆分用户隐式子需求后分别检索再融合，提升召回覆盖

  - 电商客服Agent、商品详情页RAG问答模块，可复用需求-检索-源锚定全链路追踪方案，提升回复准确率同时支持回答溯源

  - 多轮推荐Agent的上下文管理，可借鉴证据谱系的provenance记录机制，避免召回冗余信息，提升上下文利用效率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有GraphRAG处理多跳查询时，证据发现与源锚定的关联是隐式的，易出现证据链断裂、子需求覆盖不全的问题，最终导致检索召回和回答准确率不足，尤其在复杂多跳场景下性能瓶颈明显。
### 方法关键点
- 证据需求诱导：推理阶段调用LLM将原始查询拆解为最多5个有序的证据需求，每个需求分配唯一ID，明确其需要验证的事实、输入输出变量，ID在全链路保持不变
- 需求条件化谱系扩展：针对每个证据需求独立在语料图上执行Personalized PageRank检索，合并候选池时保留每个候选对应的需求ID、检索排名等 provenance 溯源信息
- 带源锚定的谱系补全：基于溯源信息做集合级候选选择，优先选取覆盖未满足需求的互补段落，再从选中段落中提取每个需求对应的原文锚定片段，实现需求到源文本的显式关联
### 关键实验
在HotpotQA、2WikiMultiHopQA、MuSiQue三个多跳QA基准数据集上，对比HippoRAG 2、PropRAG、G-reasoner等主流GraphRAG基线，平均R@5提升3.51个百分点，EM提升5.96个百分点，F1提升5.22个百分点；其中源锚定环节单独贡献6.20个EM、5.65个F1的提升，单query仅增加880token的查询侧计算开销。
### 核心结论
多跳场景下，显式保留子需求到检索结果的溯源关联，比单纯优化单维度召回排序的收益更高。
