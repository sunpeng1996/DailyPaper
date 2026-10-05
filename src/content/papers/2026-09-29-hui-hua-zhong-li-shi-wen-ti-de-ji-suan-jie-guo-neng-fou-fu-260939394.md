---
title: Can Computation from Earlier Problems Help LLMs Solve New Ones?
title_zh: 会话中历史问题的计算结果能否辅助LLM解决新问题
authors:
- Jipei He
- Wenhui Tan
- Xiaoyi Yu
- Enver Sangineto
- Fiorenzo Parascandolo
- Rita Cucchiara
- Ruihua Song
affiliations:
- 中国人民大学高瓴人工智能学院
- University of Modena and Reggio Emilia
arxiv_id: '2609.39394'
url: https://arxiv.org/abs/2609.39394
pdf_url: https://arxiv.org/pdf/2609.39394
published: '2026-09-29'
collected: '2026-10-05'
category: LLM
direction: LLM推理优化 · KV cache复用
tags:
- KV cache
- Parameter-Efficient Tuning
- Reasoning
- Multi-turn Conversation
- LoRA
one_liner: 提出仅需训练12k参数的STAIR方法，复用历史KV提升多轮独立问题推理精度最高11.67pp
practical_value: '- 电商导购、客服等多轮独立咨询的Agent场景可直接复用该方案，仅训练12k参数即可提升后续推理精度，无需微调主干模型，落地成本极低

  - 推荐/广告的LLM生成模块可参考STAIR的差分读出来设计历史语义缓存读取逻辑，既复用历史计算降低 latency，又避免无关历史信息干扰当前生成

  - 可与LoRA等参数高效微调方法结合使用，在低训练成本下进一步提升电商商品咨询、营销文案生成等垂直领域多轮任务的效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM在同一会话中处理多轮独立问题时，历史计算结果既可能提升也可能降低当前任务的推理精度，现有方案要么完全重算导致算力浪费，要么直接复用历史KV易引入无关干扰，如何在冻结主干的前提下低成本复用有效历史计算、降低负向干扰是核心痛点。

### 方法关键点
- 设计STAIR架构，将历史问题生成过程的K/V存储在只读历史KV bank中，主干完全冻结，仅训练每注意力头的反射法向量，总参数量仅12288
- 采用Householder反射对当前查询重定向，通过参考读与反射读的差分值调整注意力权重，仅在prefill阶段生效，不影响后续解码逻辑
- 训练时加入与原生模型输出的KL散度约束，保证模型行为不偏离原生分布过多，避免引入不可控生成错误

### 关键实验
在3款Qwen模型、4个推理基准上对比原生带历史模型：STAIR在AIME2025基准上T2-T4的Avg@4最高提升11.67pp；与LoRA结合使用时，比单独用LoRA再提升3.89pp的Avg@4，仅增加12k训练参数；全量KV读取仅比原生模型增加0.81s延迟和6.6GiB峰值显存，开销可控。

### 核心结论
会话中历史问题的计算是可复用的资源，仅需极少量参数调整历史KV的读取逻辑，即可在不调整主干的前提下大幅提升多轮独立任务的推理精度
