---
title: 'Multi-Step Tool-Calling over Korean Open Public APIs: A Benchmark and a Data-Synthesis
  Recipe'
title_zh: 面向韩国公开API的多步工具调用基准与数据合成框架
authors:
- Dain Kim
- Eungi Cho
- Kyumin Kim
- Shinyeong Noh
- Kyuseong Lim
affiliations:
- LG CNS
arxiv_id: '2609.05395'
url: https://arxiv.org/abs/2609.05395
pdf_url: https://arxiv.org/pdf/2609.05395
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: Agent工具调用 · 数据合成与基准
tags:
- Tool-Calling
- Agent Benchmark
- Data Synthesis
- GRPO
- Open-source LLM
one_liner: 提出韩语公开API多步工具调用基准KOPA-BENCH与执行感知动态图合成框架EDGE，提升小模型工具调用表现
practical_value: '- 做内部工具调用Agent训练数据时，可复用EDGE的执行校验动态图思路：先基于工具签名生成候选依赖，再通过真实调用剪枝无效链路，大幅降低合成数据错误率

  - 多步工具调用训练优先选择GRPO而非单纯SFT，相同数据量下GRPO可多探索有效轨迹，pass@4提升可达11pp，适合电商客服/运营Agent这类需要多步查数据的场景

  - 处理高基数API返回结果时，可借鉴junction typing方案，按返回数量分SEQ/FAN/DRV三类处理，避免多返回值导致的工具调用链路中断，适配电商商品/订单/库存多记录查询场景

  - 工具调用Agent评测可复用三维度评估方案（RESPONSE/ENVIRONMENT/ACTION），同时覆盖答案正确性、系统状态一致性、调用效率，避免仅校验动作匹配的误判'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
数据主权要求下公共机构需要部署本地化开源LLM Agent调用政府公开API完成多步任务，但现有开源模型在多步工具调用、高基数API返回处理上表现差，且无对应场景基准，同时现有工具调用合成数据未做真实执行校验，无效链路多，无法支撑小模型训练。

### 方法关键点
- 构建KOPA-BENCH基准：覆盖6个领域10个韩国公开API平台，共145个真实多步任务，平均每个任务需要5次工具调用，59%支持并行执行，采用RESPONSE/ENVIRONMENT/ACTION三维度评测
- 提出EDGE数据合成框架：Phase A构建工具依赖动态图，先基于签名匹配生成候选边，再通过真实API调用校验，用Thompson采样平衡探索利用，剪枝执行失败的依赖边；Phase B基于返回值基数做junction typing，将多返回值链路拆分为SEQ/FAN/DRV三类，合成合法多步轨迹，配套自动生成对应自然语言query和标注
- 训练策略：基于合成的1781条有效数据，用GRPO微调开源小模型，采用二进制奖励函数基于结果和状态维度打分

### 关键结果
对比多个开源/闭源模型，Qwen3.5-4B微调后KOPA-BENCH pass@1提升13pp至0.31，Qwen3.5-9B提升10pp至0.43，接近同系列27B模型的0.45水平，同时域外BFCL基准多轮指标提升5.87pp；消融实验显示相同数据下GRPO比SFT pass@4高11pp，执行校验可将边执行成功率提升12.5pp。

### 核心结论
工具调用训练数据的执行真实性比标注数量更重要，小模型通过真实执行校验的合成数据微调，可达到数倍参数规模大模型的工具调用表现
