---
title: Improving Item Discoverability in e-Commerce Search via Related Intent Generation
title_zh: 基于相关意图生成的电商搜索商品可发现性提升方案
authors:
- Ji Xin
- Xiao Xiao
- Ishan Bhatt
- Vinesh Gudla
- Trace Levinson
- Raochuan Fan
- Shishir Kumar Prasad
- Prakash Putta
- Tejaswi Tenneti
affiliations:
- Instacart
arxiv_id: '2607.27172'
url: https://arxiv.org/abs/2607.27172
pdf_url: https://arxiv.org/pdf/2607.27172
published: '2026-07-29'
collected: '2026-07-30'
category: QueryRec
direction: 电商搜索优化 · 隐式意图生成
tags:
- QueryExpansion
- LoRA
- KnowledgeDistillation
- E-commerceSearch
- LLM-as-Judge
one_liner: 通过头查询缓存大模型输出、尾查询LoRA微调SLM蒸馏的两级架构，低成本实现电商搜索隐式意图扩展
practical_value: '- 头长尾流量拆分的降本架构可直接复用：头部高流量query离线调用大模型生成结果缓存，长尾query用LoRA微调SLM蒸馏大模型能力，推理成本仅为大模型的30%，适配大规模生产环境

  - 双维度评估框架可直接复用：采用「会话购买数据构建离线业务指标+人类对齐的LLM-as-Judge」的评估方案，解决传统NDCG等精准度指标惩罚发现性结果的问题

  - 三类隐式意图（替代/互补/场景关联）的拆分可直接落地到电商搜索的相关推荐模块，生成的intent词直接对接现有召回引擎，无需重构检索链路，改造成本极低

  - 蒸馏训练时加入部分剥离元数据的样本，避免小模型在线推理时因缺少离线特征导致效果跳水，这个工程trick可大幅降低上线后的效果风险'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统电商搜索优先保障精准匹配，仅覆盖用户显性意图，无法满足替代品、互补品、场景关联商品的发现需求，既限制用户体验和营收增长，也导致长尾商品曝光不足；同时全流量调用大模型推理成本过高，无法规模化落地。
### 方法关键点
- 两级混合架构：头部10k高流量query（覆盖60%搜索流量）离线调用GPT-3.5生成结构化的展示标题+对应intent搜索词，缓存后直接调用；长尾query采用GPT-5.1作为教师模型，蒸馏训练LoRA微调的Qwen3-30B SLM实时生成结果。
- 明确三类隐式意图定义：替代品、互补品、场景关联，生成的intent词直接对接现有检索引擎召回结果，无需修改现有检索链路。
- 蒸馏训练时加入部分剥离元数据的样本，避免小模型在线推理时因缺少离线特征导致效果下降，解码温度调优为1.0平衡多样性和相关性。
### 关键实验结果
- 基于会话购买数据构建离线评测集（移除精确匹配商品），头部query上微调SLM的F1达0.184，优于现有生产基线的0.173；长尾query上SLM的F1达0.179，略优于教师GPT-5.1的0.168。
- LLM-as-Judge与人类标注的对齐F1最高达0.84，SLM的推理成本仅为教师大模型的30%，整体query覆盖率从60%提升至80%。
### 核心结论
生成式意图扩展可在不重构现有检索链路的前提下，同时实现用户体验提升、营收增长和长尾商品曝光的三方增益，头长尾拆分的蒸馏架构是生成式能力落地的高性价比方案
