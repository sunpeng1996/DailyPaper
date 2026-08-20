---
title: 'Think-to-Personalize: Unifying Reasoning and Retrieval for User-Centric Personalized
  Dense Retrieval'
title_zh: Think-to-Personalize：统一推理与检索的用户中心化个性化稠密召回框架
authors:
- Angqing Jiang
- Gaoming Zhang
- Jianchun Song
- Kena Qi
- Dayao Chen
- Wei Lin
- Defu Lian
affiliations:
- 中国科学技术大学
- 美团
arxiv_id: '2608.18855'
url: https://arxiv.org/abs/2608.18855
pdf_url: https://arxiv.org/pdf/2608.18855
published: '2026-08-19'
collected: '2026-08-20'
category: RecSys
direction: 个性化稠密召回 · LLM推理检索对齐
tags:
- Dense Retrieval
- LLM4Rec
- Personalization
- RL Alignment
- E-commerce Search
one_liner: 提出融合LLM显式用户意图推理与稠密召回的端到端TTP框架，在电商搜索场景获明确线上增益
practical_value: '- 可直接复用推理-检索统一架构：将用户历史+当前query输入LLM生成意图增强query后再编码召回，解决短/歧义query的意图gap，效果优于拆分的改写+检索两阶段pipeline

  - 两阶段训练范式可落地：第一阶段用大模型生成的增强query做SFT+InfoNCE损失冷启动，第二阶段用GRPO做RL对齐，奖励函数结合格式、长度、检索增益，用冻结的SFT模型做奖励锚点避免reward
  hacking

  - 线上部署优化方案可参考：T+1预计算高频用户-泛query对的个性化embedding做缓存，缓存miss时用蒸馏的小参数encoder-only模型实时推理，额外latency仅0.15ms

  - 用户历史截断技巧：用reranker筛选和当前query最相关的Top10条历史行为，平衡效果和效率，过长历史反而引入噪声降低召回效果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索场景用户query普遍稀疏、歧义大，仅依赖字面语义的query中心化稠密召回存在明显意图gap，无法匹配用户真实个性化需求；现有个性化召回方案要么依赖隐式行为序列建模，缺乏显式推理能力难以消解噪声历史的干扰，要么采用改写+检索的拆分pipeline，无法将生成的意图和下游召回目标对齐，同时大多数LLM embedding方案仅把LLM作为静态编码器，浪费了其内置的推理能力。

### 方法关键点
- 端到端统一架构：输入拼接指令、用户历史行为序列、当前query，LLM先生成`<think>`包裹的意图增强query，再输出`<embed>`特殊token，取该token的最后隐层作为query embedding，和item embedding做语义匹配
- 两阶段训练策略：SFT阶段用Qwen3-32B生成的高质量意图增强query做监督，联合生成损失和InfoNCE对比损失完成冷启动；RL阶段采用GRPO做策略优化，奖励函数结合格式合规、长度惩罚、检索增益，同时引入动态正例选择，仅取RL生成的高奖励样本做对比学习，避免噪声干扰
- 低延迟部署方案：T+1预计算活跃用户-泛query对的个性化embedding缓存，同时将3B大模型蒸馏为305M的encoder-only小模型处理缓存miss请求，兼顾效果和性能

### 关键结果
在美团自有数据集上，TTP比最优基线MAPs的Recall@20提升1.76%、Recall@100提升1.99%；在歧义query数据集上Recall@20比base Qwen-Embedding提升7.47%；线上A/B测试作为新增召回通道，带来订单量+0.46%的提升，额外端到端延迟仅0.15ms。

**最值得记住的一句话**：个性化检索的核心是弥合用户字面query和真实意图的gap，显式用户行为推理与召回目标端到端对齐的效果，显著优于拆分的改写+检索两阶段pipeline。
