---
title: 'MemSFT: Mitigating Alignment Tax with an External Parametric Memory'
title_zh: MemSFT：基于外部参数化记忆缓解大模型域微调的对齐税
authors:
- Jiarui Wang
- Xiang Shi
- Jiaqi Cao
- Rubin Wei
- Xiquan Wang
- Hao Sun
- Jingzhi Wang
- Zhiqi Yang
- Qipeng Guo
- Bowen Zhou
affiliations:
- Shanghai Jiao Tong University
- Shanghai AI Laboratory
- Tsinghua University
arxiv_id: '2607.25614'
url: https://arxiv.org/abs/2607.25614
pdf_url: https://arxiv.org/pdf/2607.25614
published: '2026-07-28'
collected: '2026-07-29'
category: LLM
direction: 大模型域适配 · 参数化外部记忆
tags:
- Supervised Fine-Tuning
- Catastrophic Forgetting
- Parametric Memory
- Alignment Tax
- Dynamic Routing
one_liner: 通过可插拔外部参数化记忆与动态路由实现大模型域适配无遗忘，记忆可跨模型复用
practical_value: '- 做电商/广告领域大模型适配时可复用该架构：冻结通用大模型backbone仅训练域专属记忆，避免微调后通用推理、指令跟随能力下降，同时节省多模型规模适配的计算量

  - 动态token级路由设计可迁移到生成式推荐场景：生成通用话术时调用base能力，生成商品属性、活动规则等域专属内容时高权重调用领域记忆，平衡通用性和领域准确性

  - 相同tokenizer的模型族可复用同一域记忆的设计，可落地到业务多规格LLM部署场景：小模型供在线推荐实时生成用，大模型供离线运营文案生成用，仅需训练一次领域记忆'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大模型针对垂直领域做SFT或LoRA微调时普遍存在对齐税问题：领域性能提升的同时会出现灾难性遗忘，导致通用推理、指令跟随等能力大幅下降；现有混合训练、权重插值等缓解方案无法跳出“领域收益-通用能力损失”的trade-off，且需为每个规模的模型单独适配，计算成本极高。

### 方法关键点
- 架构完全冻结通用LLM backbone，新增独立参数化记忆模块和轻量token级路由：记忆模块通过蒸馏基于领域SFT数据构建的非参数检索教师的输出分布训练，内化领域知识与模式
- 路由模块仅用混合的通用+领域数据训练，输入base与记忆的隐状态、输出分布置信度等特征，逐token预测融合权重，动态插值两者的next-token分布
- 训练完成的领域记忆只要适配相同tokenizer与词表，即可跨同模型族不同规模的LLM复用，无需重新训练

### 关键实验
在生物、地理、法律三个垂直领域测试，对比原生backbone、全参数SFT、LoRA、Wise-FT、混合训练等baseline：
- 领域性能平均提升30+百分点的同时，通用能力平均下降<0.6%，远优于全SFT（通用能力最高下降31.4%）和LoRA（最高下降17.1%）
- 同领域记忆可在Qwen3 8B到235B全系列模型复用，适配4个不同规模模型的总计算量仅为全SFT的0.22倍

> 最值得记住的结论：将领域知识与通用能力在参数层面完全解耦，是解决大模型微调对齐税的最可行路径之一
