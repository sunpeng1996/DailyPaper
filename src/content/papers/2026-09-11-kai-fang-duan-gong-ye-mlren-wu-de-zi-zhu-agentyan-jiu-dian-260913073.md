---
title: 'Autonomous Research for Open-Ended Problems: A Case Study on Telecom Ticket
  Retrieval'
title_zh: 开放端工业ML任务的自主Agent研究：电信工单检索案例
authors:
- Junghyun Min
- Huseyin Uzunalioglu
- Mohamed Trabelsi
affiliations:
- Georgetown University
- Nokia Bell Labs
arxiv_id: '2609.13073'
url: https://arxiv.org/abs/2609.13073
pdf_url: https://arxiv.org/pdf/2609.13073
published: '2026-09-11'
collected: '2026-09-14'
category: Agent
direction: Agent 工业ML任务自主研发落地
tags:
- Autonomous Research
- LLM Agent
- Information Retrieval
- Multi-Agent
- Hyperparameter Optimization
one_liner: 通过电信工单检索案例验证自主研究Agent可低成本快速逼近人工SOTA 90%性能
practical_value: '- 电商/推荐场景的召回、排序、检索类任务调优中，可以用自主Agent批量做超参数、正负样本采样策略、预处理规则的探索，大幅降低人工重复劳动成本

  - 自主Agent落地的工程方案可直接复用：放弃Agent自管理的迭代逻辑，改用固定外层bash脚本控制、提前明确定义搜索空间、补充详细任务文档的harness架构，稳定性提升显著

  - 不要盲目增加多Agent架构、使用高价商用LLM，实测在参数/策略优化类场景下，开源LLM、单Agent的效果与商用多Agent方案无显著差异，可优先选择低成本方案

  - 自主Agent更适合做局部搜索优化，人类需要提前定义好系统架构方向（比如是否加rerank、是否做数据增强、是否用模型集成），再交给Agent做细节调优，人+Agent的协作模式投入产出比最高'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有端到端自主ML研究框架仅能适配搜索空间狭窄的benchmark任务（如语言建模、生物医学基准），无法直接落地开放端工业级ML任务——这类任务的自由度覆盖数据生成、表征方案、架构设计等多个维度，当前自主Agent的能力边界、落地成本、适用场景尚不明确。

### 方法关键点
- 以开放度极高的电信工单检索为测试场景，优化目标为Recall@1，搜索空间覆盖文档预处理规则、正负样本采样策略、模型架构与超参数三类
- 设计三层工程harness保障运行稳定性：明确任务/硬件/评价指标文档、显式定义搜索空间并拆分到对应模块、用固定bash外层循环替代不可靠的Agent自管理循环
- 对照实验覆盖三个核心变量：单Agent/多Agent框架、3款底层LLM（Claude Sonnet 5、Cursor Composer 2.5、开源GPT-OSS 120B）、是否告知人类SOTA方案的核心组件

### 关键结果
数据集包含25万真实电信工单、29.3万对应解决文档，对比基线包括BM25、人工微调MPNet、人工集成检索模型、内部人工开发的SOTA方案。最优自主Agent产出的单微调MPNet模型Recall@1达0.343，达到内部人工SOTA（0.38）的90%性能，开发周期仅10周（人工开发同类SOTA需10个月），单次实验Campaign成本仅150~200美元；不同Agent框架、LLM选型、是否告知SOTA信息对最终性能无显著影响。

最值得记住的结论：当前自主研究Agent仅擅长局部参数/策略的优化，不具备全局架构创新能力，人类定义架构方向+Agent做细节优化的协作模式是当前最优解。
