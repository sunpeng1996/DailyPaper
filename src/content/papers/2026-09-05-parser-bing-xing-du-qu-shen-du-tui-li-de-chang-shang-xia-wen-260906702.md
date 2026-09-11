---
title: 'PARSER: Read in Parallel, Reason in Depth for Long-Context LLM Agents'
title_zh: PARSER：并行读取深度推理的长上下文LLM多Agent架构
authors:
- Kun Li
- Zexuan Qiu
- Tianhua Zhang
- Irwin King
- Helen Meng
affiliations:
- The Chinese University of Hong Kong
arxiv_id: '2609.06702'
url: https://arxiv.org/abs/2609.06702
pdf_url: https://arxiv.org/pdf/2609.06702
published: '2026-09-05'
collected: '2026-09-11'
category: Agent
direction: Agent 长上下文推理架构优化
tags:
- Long-Context Reasoning
- Multi-Agent
- Scatter-Gather
- Reinforcement Learning
- Inference Efficiency
one_liner: 提出解耦读写的散列-聚合多Agent架构，解决长上下文推理的位置偏差与高延迟问题
practical_value: '- 电商/推荐场景处理长序列（用户全生命周期行为、商品长详情/评论、商家资质文档）时，可直接复用「分块+冻结轻量子Agent并行读取」架构，将延迟从随长度线性增长转为仅和推理轮数相关，长文本场景降本提效明显

  - 多Agent落地时采用「仅训主Agent推理策略、子Agent用现成冻结小模型」的范式，无需对所有子模型做领域微调，训练成本降低90%以上，业务适配速度快

  - 多跳匹配类任务（如跨多页商品信息检索、用户需求拆解匹配多维度供给）可借鉴迭代scatter-gather模式，基于已召回证据动态调整查询，彻底解决长文本下的信息位置偏差问题，准确率提升显著'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有顺序内存Agent按块串行读取长文档，推理深度与文档遍历深度强绑定，既存在证据位置、逻辑顺序、跨块距离的敏感偏差，推理延迟又随文档长度线性增长；即使是支持百万token窗口的大模型也存在context rot问题，长上下文多跳推理准确率随长度暴跌，亟需解耦读取和推理的全新架构。

### 方法关键点
- 散列-聚合双层架构：轻量子Agent每个绑定一个文档块，并行执行查询匹配，无关查询直接返回弃权；主Agent不接触原始文档，仅负责多轮迭代推理，每轮广播查询、聚合子Agent返回的证据，生成下一轮查询直到输出答案
- 训练策略：子Agent全部使用现成冻结小模型，仅用GRPO强化学习优化主Agent的推理策略，奖励为答案精确匹配的二元值，无需复杂标注，训练成本极低
- 效率优化：延迟仅和推理轮数相关，和文档长度完全解耦，子Agent返回的大部分弃权结果会被直接过滤，大幅减少无效通信和计算

### 关键实验
在7K~896K token长度的HotpotQA（分布内）、2WikiMultiHopQA（分布外）多跳QA数据集上测试，对比MemAgent、ReMemR1等顺序Agent以及DeepSeek-V4-Pro等大窗口LLM：4B backbone的ParSer平均准确率超最强顺序基线5.7个点，896K长文本下领先12个点；9B版本超DeepSeek-V4-Pro 6.3个点，推理延迟最高降低11×，对证据位置、顺序、距离扰动的稳定性远优于所有基线。

**最值得记住的一句话：** 有效长上下文推理的核心是基于已发现证据动态迭代全文档查询，而非依赖容量有限的顺序内存更新
