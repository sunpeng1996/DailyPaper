---
title: Shared Context Candidate Scoring with Jointly Adapted Readout Networks
title_zh: 基于联合适配读出网络的共享上下文候选打分系统
authors:
- Jingyang Du
- Yiben Fu
- Yang Shen
affiliations:
- 中央民族大学新闻与传播学院
- 清华大学新闻与传播学院
- 清华大学人工智能学院
arxiv_id: '2611.04218'
url: https://arxiv.org/abs/2611.04218
pdf_url: https://arxiv.org/pdf/2611.04218
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: LLM推理优化 · 上下文复用
tags:
- Context_Reuse
- PEFT
- KV_Cache
- Candidate_Scoring
- Inference_Optimization
one_liner: 冻结大模型主干复用文档上下文状态，联合适配轻量模块实现多请求场景精度延迟平衡
practical_value: '- 共享上下文场景（如同商品多属性查询、同用户历史多推荐任务）可复用文档前缀KV+中间层特征，单文档多请求场景能大幅降低延迟，适配电商商品问答、多意图推荐批量打分需求

  - 冻结大模型backbone仅联合适配adapter+小decoder+读出网络的方案，仅训练约88M参数即可大幅提升下游任务精度，无需全量微调，适合业务快速迭代

  - 延迟收益仅在同上下文多请求场景成立，单请求场景反而存在额外开销，业务落地前需先评估请求的上下文复用率，避免盲目上线'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
同一份上下文（如文档、用户行为序列）被多次查询时，重复调用大模型会产生大量冗余计算，现有前缀缓存方案仅优化推理效率，没有针对下游候选打分任务适配读出逻辑，往往存在明显精度损失，亟需兼顾多请求场景精度与推理效率的落地方案。

### 方法关键点
- 冻结Qwen3.8-27B全量主干，一次编码生成两类可复用资源：混合前缀状态（含KV cache、卷积/循环层状态）、第32/64层的token级特征库，缓存粒度为64 token，未对齐部分请求时重放
- 每路查询单独走全量冻结主干得到表示后，经过残差adapter（隐层维度128）+4层decoder处理，decoder交叉注意力混合两层特征库的信息
- 最终打分由仿射指针得分+候选感知的文档注意力读出得分融合得到，训练时仅更新adapter、decoder、特征投影层、读出网络，总参数量约88.66M

### 关键结果
精度评估覆盖ARC-Challenge、ANLI-R3、MMLU-Pro分层子集、CMMLU分层子集共5112条样本，联合适配后四基准宏观精度从66.46%提升到74.32%，仅比原生27B低1.36pp，比AnyJev 32B低2.36pp；延迟测试在4096 token文档+50个查询的场景下，冷请求中位延迟2.237s，仅为原生27B的41.5%、批量AnyJev的3.93%，单查询场景冷请求比原生27B慢约38%。

最值得记住的一句话：共享上下文多请求场景的效率优化需平衡缓存复用、轻量适配的精度收益与单请求开销，上下文复用率足够高时可通过极小训练成本换取数倍延迟下降。
