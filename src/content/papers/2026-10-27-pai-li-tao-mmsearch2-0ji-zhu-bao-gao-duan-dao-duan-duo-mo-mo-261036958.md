---
title: 'PailitaoMMSearch2.0 Technical Report: Scaling Generative Retrieval to Unified
  End-to-End Multimodal Search'
title_zh: 拍立淘MMSearch2.0技术报告：端到端多模态生成式检索规模化落地
authors:
- Xiaohan Ye
- Zihan Gong
- Jingqian Zhao
- Lianyu Du
- Yunmeng Shu
- Xu Chen
- Zesheng Zhou
- Renchun You
- Bocheng Chen
- Jinsong Lan
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2610.36958'
url: https://arxiv.org/abs/2610.36958
pdf_url: https://arxiv.org/pdf/2610.36958
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · 多模态商品检索
tags:
- Generative Retrieval
- Multimodal Search
- Semantic ID
- Reinforcement Learning
- E-commerce
one_liner: 淘宝推出统一端到端多模态生成式检索系统，在拍立淘落地获GMV+8.94%等核心收益
practical_value: '- 数据生产侧可复用可组合工具集的设计，按冷启动/流量迭代/持续生产三个阶段配置粗筛、query生成、质量控制等模块，大幅降低新意图新场景的标注成本

  - 多阶段训练框架可直接迁移到生成式检索场景：先做电商域CPT对齐商品语义和SID空间，再做多意图混合推理预算SFT，最后用Sample-Beam RL对齐训练与线上beam解码逻辑，消除训练serving
  gap

  - 场景部署时可通过「模型参数量+推理预算」组合出多档质量-成本运营点，不需要单独训练意图专属模型，适配不同latency、算力约束的业务场景，例如0.8B无推理模式适用于高吞吐召回，4B高推理模式适用于低时延容忍的复杂搜索

  - RL优化时采用意图均衡采样，避免高流量意图主导训练损失，兼顾小众长尾意图的检索效果，适用于所有多意图混合的搜索推荐场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有工业界生成式检索多与特定场景绑定，存在三大痛点：监督绑定（依赖单一入口交互日志，无法覆盖未上线意图）、意图绑定（单模型仅支持单检索关系，需额外路由模块提升系统复杂度）、资源绑定（推理配置适配单一SLO无法跨场景复用），无法适配多模态搜索下用户开放式图文查询、异构购物意图、不同资源约束的场景需求。

### 方法关键点
- 数据规模化：设计包含粗筛、精筛、query生成/修复、CoT生成、质量控制5个模块的可组合工具集，按需组合为冷启动合成、真实流量迭代、持续生产三类工作流，覆盖全生命周期数据需求
- 意图规模化：三阶段训练框架，首先通过持续预训练（CPT）让VLM适配电商商品知识与Semantic ID输出空间；然后做多意图混合推理预算SFT，让单模型同时支持相似、编辑、匹配三类检索意图与无/低/高三档推理预算；最后做意图均衡的统一RL，引入Sample-Beam rollout机制，推理轨迹采样、SID部分beam解码，对齐线上serving逻辑
- 场景规模化：通过0.8B/2B/4B三档参数量+三档推理预算组合出多档质量-成本运营点，无需额外意图分类路由，适配不同业务的资源约束

### 关键结果
训练数据包含61M代理冷启动数据+10M真实流量精炼数据，离线对比VLM改写+全文检索、内部多召回排序管线两套baseline，2B低推理预算配置将宏观Excellent Rate提升2.9~5.6个点，平均latency降低64.4%~92.4%；线上A/B测试在拍立淘多模态搜索场景获IPV+17.90%、交易+27.04%、GMV+8.94%的统计显著提升。

### 核心结论
生成式检索的规模化落地需要从数据生产、模型训练、部署调度全链路解耦场景绑定，而不是仅优化检索模型本身
