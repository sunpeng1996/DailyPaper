---
title: 'OneQuery: Unified Sequence-to-Structure Generation for Multilingual E-commerce
  Query Understanding'
title_zh: OneQuery：面向多语言电商Query理解的统一序列到结构生成框架
authors:
- Mingyu Zhang
- Jiejie Qin
- Jianhui Ji
- Rong Xiao
- Meishan Zhang
- Xiaoyi Zeng
affiliations:
- Xiamen University
- Alibaba Group
- Harbin Institute of Technology Shenzhen
arxiv_id: '2611.33653'
url: https://arxiv.org/abs/2611.33653
pdf_url: https://arxiv.org/pdf/2611.33653
published: '2026-11-25'
collected: '2026-11-26'
category: QueryRec
direction: 生成式Query理解 · 多语言电商场景
tags:
- Query_Understanding
- Multilingual_Ecommerce
- Sequence_to_Structure
- Reinforcement_Learning
- LLM4Search
one_liner: 将多语言电商Query理解的4个子任务统一为Schema引导的生成任务，三阶段训练实现效果与运维效率双提升
practical_value: '- 多任务融合架构选型：可将上下游链路的Query理解类子任务（语种识别、纠错、翻译、标签抽取）统一为Schema约束的JSON生成任务，避免多模型串联的误差累积，降低运维成本

  - 低标注成本训练方案：可用迭代字段补全策略，从单任务部分标注数据合成全字段训练样本，搭配少量人工标注数据即可完成多任务SFT，大幅降低标注成本

  - RL对齐优化技巧：多任务RL对齐时可采用GRPO替代PPO降低算力开销，针对不同子任务设计差异化奖励（如纠错用编辑距离奖励，翻译/标签用严格Exact Match奖励），并按子任务依赖关系分配权重，提升优化效果

  - 线上部署trick：大模型统一Query理解系统可采用「头Query预生成缓存 + 尾Query小蒸馏模型实时推理」的架构，兼顾效果与latency要求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多语言电商搜索场景下，传统Query理解采用多独立模型串联架构，存在上游误差向下游传导、子任务依赖未充分利用、多模型迭代运维成本高的痛点；同时全字段标注的多任务训练数据稀缺，通用大模型Few-Shot效果远达不到工业落地要求。

### 方法关键点
- 范式重构：将语种识别、拼写纠错、翻译、Query标签抽取4个子任务统一为Schema约束的JSON结构生成任务，共享参数建模子任务依赖，避免误差累积
- 三阶段训练：1）单任务联合SFT，用独立指令分别训练4个子任务的基础能力；2）用迭代字段补全策略合成360万伪标注全字段样本，搭配31万人工标注数据完成统一多任务SFT；3）基于GRPO做任务感知多目标RL对齐，按子任务依赖分配奖励权重，纠错采用编辑距离奖励，其余子任务采用严格Exact Match奖励
- 部署策略：头Query离线预生成结果缓存，尾Query用蒸馏的0.3B小模型实时推理，满足线上latency要求

### 关键结果
离线19087条标注多语言Query测试集上，14B版本相比传统流水线：语种识别Acc提升1.51pt，翻译ROUGE-2提升2.3pt，拼写纠错F1提升1.49pt，Query标签抽取F1提升2.38pt；效果显著优于Qwen3.8-Max、GPT-5.6 Luna等通用大模型Few-Shot结果。线上AliExpress A/B测试实现L2P提升0.5%，人工相关性评分提升0.8pt。

### 核心结论
电商域多任务Query理解场景下，领域专属小模型的统一生成范式，效果远好于通用大模型Few-Shot，同时能大幅降低系统运维成本
