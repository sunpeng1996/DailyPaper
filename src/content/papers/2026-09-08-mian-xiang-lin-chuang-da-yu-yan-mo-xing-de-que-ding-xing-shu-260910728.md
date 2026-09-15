---
title: Towards a Deterministic Math Solver for Clinical Language Models
title_zh: 面向临床大语言模型的确定性数学求解器
authors:
- Felipe Ocampo Osorio
- Sebastián Andrés Cajas Ordoñez
- Maximin Lange
- Rafi Al Attrach
- Sahil Kapadia
- Zakaria Laouabdia Sellami
- Angelo Antonio Talio
- Leo Anthony Celi
affiliations:
- MIT Critical Data
- UNC Chapel-Hill
- University of Pavia
- Humanitas University
arxiv_id: '2609.10728'
url: https://arxiv.org/abs/2609.10728
pdf_url: https://arxiv.org/pdf/2609.10728
published: '2026-09-08'
collected: '2026-09-15'
category: Agent
direction: Agent 工具调用 确定性算术推理优化
tags:
- Tool Calling
- Program Aided Reasoning
- Clinical LLM
- Deterministic Computation
- Arithmetic Reasoning
one_liner: 受控对比临床计算中LLM直接算术、手写库、代码执行三种方案，给出选型建议
practical_value: '- 做涉及数值计算的Agent（如电商优惠核算、广告ROI计算类Agent）时，可复用论文的受限代码执行器设计：独立子进程运行，仅开放math/date等必要标准库，设置256MB内存、5s运行时间上限，规避安全风险同时保证计算确定性。

  - 架构选型参考：高频固化计算逻辑用手写验证过的工具库保证100%准确率，低频长尾计算用大模型生成代码执行兜底，混合架构准确率远高于单一方案，比如论文中Gold-first混合方案在32B模型下准确率达91.07%，比单独用Program-Solve高0.54pp。

  - 小模型选型提示：7B级开源模型生成代码执行的准确率不一定优于直接算术（Qwen2.5-7B仅高3.29pp且置信区间过零，Mistral-7B反而低7.62pp），7B级模型做数值计算优先用直接推理，32B+模型可加代码执行链路提效。

  - 评估方法复用：涉及多类计算任务的效果评估，采用cluster bootstrap按任务类型重采样计算置信区间，避免样本分布不均导致的结果偏差，适合电商多场景下的算法效果校验。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM算术计算可靠性差，用于高准确率要求的计算场景（如临床计算器、电商优惠核算、广告预算计算）时，单个数值错误就会导致完全错误的决策；传统方案为每个计算逻辑手写验证函数，维护成本高且无法覆盖长尾需求。

### 方法关键点
- 提出Program-Solve方案：LLM无需直接计算，根据给定公式、变量和上下文生成专属Python代码，由受限本地执行器运行得到确定性结果，执行器无计算器相关硬编码逻辑。
- 执行器做严格安全限制：每个程序运行在独立子进程，仅开放math/datetime等标准库，禁用eval/exec等危险操作，设置资源和运行时间上限。
- 受控对比设计：所有对比方案匹配公式、变量、上下文输入条件，排除输入差异对结果的干扰，对比三种路径：LLM直接算术、手写22个计算器的硬编码库、Program-Solve代码执行。

### 关键结果
- 测试数据集为MedCalc-Bench Verified，共1100个测试用例，覆盖55种临床计算器；测试模型包括Qwen2.5-7B、Qwen2.5-32B-AWQ等4个开源模型。
- 相同输入条件下，7B模型用Program-Solve比直接算术仅高3.29pp（95%置信区间[-3.49,10.38]，无统计显著性）；32B模型用Program-Solve比直接算术高7.05pp（95%置信区间[0.47,14.60]，显著提升）。
- 手写硬编码库在覆盖的22个计算器上准确率100%，但仅覆盖40%用例，整体准确率40%；Gold-first混合方案（库覆盖的用库，其余用Program-Solve）在32B模型下整体准确率达91.07%。

**最值得记住的一句话**：高准确率计算场景的最优架构是「已验证的硬编码工具库覆盖高频场景，大模型代码执行覆盖长尾场景，两者结合平衡准确率和覆盖度」。
