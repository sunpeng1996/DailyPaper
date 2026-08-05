---
title: 'Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility'
title_zh: 推理大模型测试时缩放：推理范式、评估体系与可复现性规范
authors:
- Mohsen Hariri
- Weicong Chen
- Nahal Shahini
- Vikash Singh
- Kai Ye
- Amirhossein Samandar
- Debargha Ganguly
- Sreehari Sankar
- Yanyan Zhang
- Shouren Wang
affiliations:
- Case Western Reserve University
arxiv_id: '2608.04001'
url: https://arxiv.org/abs/2608.04001
pdf_url: https://arxiv.org/pdf/2608.04001
published: '2026-08-04'
collected: '2026-08-05'
category: Reasoning
direction: 大语言模型推理 · 测试时缩放
tags:
- Test-Time Scaling
- LLM Reasoning
- Inference Optimization
- Evaluation Protocol
- Reproducibility
one_liner: 将推理LLM测试时缩放划分为三类范式，提出统一评估框架与可复现规范，开源200万+推理轨迹
practical_value: '- 业务中部署推理类Agent（如电商客服、导购、售后问题解答）时，可按场景需求选型测试时缩放范式：低延迟要求的实时交互场景用单轨迹顺序缩放，高准确率要求的复杂咨询场景用叶子级缩放+验证器过滤/多数投票，复杂活动规则计算等深度推理场景用前缀级搜索+KV
  cache共享降低开销

  - 做LLM推理效果对比时，严格对齐总计算成本（生成token成本+评估器调用成本），同时完整上报推理协议（解码温度、采样数、聚合规则、停止策略），避免因预算不对齐导致的效果误判

  - 线上推理系统迭代时参考可复现规范：固定随机种子与请求的映射规则，留存核心请求的完整推理轨迹与元数据，上线前评估效果置信区间，避免单轮随机波动误导迭代决策'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前推理LLM的测试时缩放技术（含Chain-of-Thought、自一致性、思维树等）种类繁杂，不同方法的统计特性、计算开销、失败模式差异显著，现有研究常将不同范式混为一谈，仅上报单一准确率而不披露推理协议，导致跨研究结果无法横向对比，行业缺乏统一的形式化定义、评估体系与可复现标准。
### 方法关键点
- 将测试时缩放形式化为自回归模型隐式前缀树上的带预算推理任务，划分为三类可组合的结构范式：单轨迹顺序缩放（仅维护一条活跃推理路径，适配低延迟场景）、叶子级缩放（生成多份完整候选后通过投票/重排聚合，适配高准确率场景）、前缀级缩放（基于未完成前缀的得分分配计算资源，适配复杂推理场景）
- 提出系统性评估原则：将完整推理系统（基座模型、提示词、解码器、聚合规则、停止策略、评估器、计算预算）作为评估对象，区分端到端性能与候选库质量诊断，设计统一的发现-稳定性剖面，可覆盖pass@k、Maj@k等所有常见重复采样指标
- 明确可复现性要求：区分精确回放与分布可复现两类场景，要求上报效果时同时披露推理协议、计算成本拆分、效果置信区间，配套开源覆盖多类推理任务的200万+条推理轨迹数据集。
### 关键实验结果
在常识推理、符号推理、竞赛数学三类基准上评测主流开源推理模型，验证同计算预算下不同范式的性能差异：叶子级缩放的自一致性投票相比单轨迹基线准确率提升12%~18%，前缀级搜索相比同预算叶子级缩放计算效率提升30%以上；开源数据集包含20亿+token的完整推理轨迹，附带验证器得分、token级信号等标注。
### 核心结论
推理模型的性能是基座权重、推理协议与计算预算共同作用的结果，脱离推理协议和计算成本上报的准确率结论不具备参考价值。
