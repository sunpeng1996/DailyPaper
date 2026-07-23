---
title: 'PyroDash: Cost-Efficient Token-Level Small-Large Language Model Collaborative
  Inference'
title_zh: PyroDash：Token级大小语言模型协同推理的成本优化框架
authors:
- Niqi Lyu
- Pengtao Shi
- Wei Qiu
- Jianlin Zhong
- Sicong Xia
- Jianyao Ma
- Yicheng Ding
affiliations:
- Pyromind Dynamics Inc.
arxiv_id: '2607.20327'
url: https://arxiv.org/abs/2607.20327
pdf_url: https://arxiv.org/pdf/2607.20327
published: '2026-07-22'
collected: '2026-07-23'
category: LLM
direction: 大模型推理优化 · 大小模型协同
tags:
- SLM-LLM Collaboration
- Inference Cost Optimization
- GRPO
- Token-level Routing
- Collaborative Inference
one_liner: 通过SLM内置单切路由与成本感知GRPO训练，实现精度-成本可调的大小模型协同推理
practical_value: '- 电商/推荐场景的用户query理解、导购文案生成、商品合规校验等任务可直接复用该框架，用7B/14B级SLM兜底，仅在识别到复杂推理需求时调用大模型，大幅降低API成本，同时保证复杂场景效果

  - 可复用三阶段训练范式：先新增控制令牌嵌入，再用SFT冷启动路由行为，最后用GRPO做成本-效果对齐，无需修改大模型，适配所有闭源大模型API，工程改造成本极低

  - 可通过调整λ参数灵活适配不同业务场景的精度/成本要求：大促等流量高峰调大λ降低成本，高价值用户流量调小λ保证效果

  - 相比传统请求级路由，token级动态切流能捕获推理中途出现的复杂需求，尤其适合多轮导购Agent、长文本商品卖点生成等长推理链路场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM推理成本高，全量调用开销难以支撑大规模业务部署，SLM虽成本低但复杂推理能力不足；现有请求级路由无法应对推理中途出现的复杂需求，token级协同方案要么需要额外路由模块、多次模型切换，要么要求访问LLM logits，无法适配闭源API，且很少直接对齐实际计费的推理成本。
### 方法关键点
- 采用SLM优先的单次切流架构：SLM自主推理，生成专属控制令牌τ_off时触发切流，Collaborate Engine将用户query+已生成的推理上下文传给冻结的LLM完成后续生成，全程仅1次LLM调用，无需额外路由模块、LLM重训或logits访问
- 三阶段训练SLM路由策略：1）控制令牌嵌入学习，用锚点token均值初始化τ_off嵌入，LoRA微调后仅保留τ_off相关参数；2）切流导向SFT冷启动，混合训练独立生成与条件切流行为；3）基于GRPO的成本感知对齐，奖励函数同时平衡答案准确率与归一化到LLM单跑成本的推理开销，λ参数控制成本权重
### 关键结果
在GSM8K、Minerva、OlympiadBench等5个数学推理基准上测试，对比单独SLM、单独LLM、RouteLLM、GlimpRouter等基线：
- 优先精度（λ=0.05）：平均准确率64.04%，比单独LLM高6.36pp，成本降低20.4%
- 优先成本（λ=0.6）：平均准确率54.55%，仅比单独LLM低3.13pp，LLM token占比仅1.9%，单例平均LLM调用次数0.012，总成本从$49.36降至$1.78，降幅96.4%
最值得记住的一句话：大小模型协同的核心不是为全量请求选择某个模型，而是在推理过程中动态划分能力边界，用最少的大模型调用获取最高的整体收益。
