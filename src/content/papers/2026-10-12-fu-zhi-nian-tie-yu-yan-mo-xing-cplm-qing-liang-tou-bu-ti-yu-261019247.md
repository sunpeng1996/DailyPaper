---
title: Copy-Paste Language Models
title_zh: 复制粘贴语言模型（CPLM）：轻量头部提升LLM训练与长上下文性能
authors:
- Nathan Godey
- Yoav Artzi
affiliations:
- Cornell University
arxiv_id: '2610.19247'
url: https://arxiv.org/abs/2610.19247
pdf_url: https://arxiv.org/pdf/2610.19247
published: '2026-10-12'
collected: '2026-10-17'
category: LLM
direction: LLM架构优化 · LM头瓶颈缓解
tags:
- Copy-Paste Head
- LM Head Bottleneck
- Long Context LLM
- Gradient Optimization
- Efficient LLM
one_liner: 给传统LLM新增轻量复制粘贴头部，缓解LM头梯度瓶颈，提升训练效率与长上下文性能
practical_value: '- 可在业务侧7B/1.7B级小LLM（用于Agent调度、商品文案生成、RAG问答等场景）上新增CP头，仅增加0.5%参数、3%计算开销，即可提升长上下文属性抽取、用户会话信息召回、FAQ问答的准确率

  - 长上下文推理场景（如用户全周期行为序列理解、超长商品详情页解析）可直接复用滑动窗口CPLM方案，在12×更低内存开销下达到全注意力模型性能，大幅降低推理部署成本

  - RAG场景可复用CP头的预计算key机制，仅存储CP头key即可完成文档检索，相比存储全量KV缓存内存开销降低50×，适配大规模商品库/知识库的低成本RAG落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Transformer LLM看似通过自注意力实现上下文复制，但实际受低秩LM头的双重瓶颈限制：正向传播时无法表达复杂输出分布，反向传播时压缩梯度信号导致训练信号损失，最终复制能力受限，训练效率、长上下文性能均有明显优化空间。
### 方法关键点
- 在传统LM头旁新增轻量Copy-Paste（CP）头，通过注意力打分指向上下文历史位置，聚合对应token生成复制候选分布
- 新增<copy>特殊token作为CP头的门控信号，由LM头预测是否触发复制；新增<sink>特殊key，无合适复制对象时自动回退到LM头输出
- 无额外辅助损失，仅用标准next-token交叉熵端到端训练，CP头仅新增2个投影矩阵，参数和计算开销可忽略
### 关键结果
在135M~1.7B参数、全注意力/滑动窗口/混合架构等多种backbone上预训练，对比同参数量vanilla LM：训练收敛速度提升1.25~2×，OOD文档perplexity降低0.5~1.5，零-shot下游任务准确率提升0.4~0.9个点；SFT后数学/代码/指令跟随任务准确率提升1~5个点，1.7B滑动窗口CPLM仅用1/12内存就达到全注意力模型性能；超长上下文（4×训练长度）检索准确率远高于基线，RAG场景仅用CP头key就保留90%以上检索精度，内存开销降低50×。
### 核心结论
LM头的梯度瓶颈是限制LLM复制、长上下文能力的核心因素之一，仅新增一个轻量旁路CP头就能以极低开销大幅提升多场景性能
