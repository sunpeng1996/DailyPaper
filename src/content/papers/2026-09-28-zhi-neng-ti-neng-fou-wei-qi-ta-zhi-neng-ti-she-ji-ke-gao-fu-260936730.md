---
title: Can Agents Design Libraries for Agents?
title_zh: 智能体能否为其他智能体设计可高效复用的代码库？
authors:
- Gabriel Orlanski
- Alex L. Zhang
- Avi Trost
- Vincent Sunn Chen
- Frederic Sala
- Aws Albarghouthi
- Ludwig Schmidt
affiliations:
- University of Wisconsin–Madison
- Massachusetts Institute of Technology
- Snorkel AI
- Stanford University
arxiv_id: '2609.36730'
url: https://arxiv.org/abs/2609.36730
pdf_url: https://arxiv.org/pdf/2609.36730
published: '2026-09-28'
collected: '2026-10-01'
category: Agent
direction: 智能体工具构建 · 代码库设计评估
tags:
- Agent
- Benchmark
- Code Generation
- LLM
- Tool Design
one_liner: 提出LibraryDesignBench基准，评估智能体设计的代码库对下游智能体的易用性
practical_value: '- 做Agent工具链/模块评估时，可复用「上游产出物质量由下游使用效果打分」的范式，替代仅验证单步正确性的方案，比如评估RAG召回模块时直接参考下游回答的准确率和token用量

  - 给Agent设计内部工具/SDK/API时，可借鉴文中干预手段：先写下游用例、提供可运行示例、用子Agent提前测试可用性，能降低下游Agent的冗余代码量和推理成本

  - 优化Agent工具调用能力时，优先解决接口刚性/易用性问题，文中数据显示64%的冗余代码由接口难用导致，远高于能力缺失的14%影响，投入产出比更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前智能体代码生成场景下，大量重复实现相同功能而非复用已有代码，导致后续智能体需要处理的代码库持续膨胀。传统代码库评估仅验证功能正确性，无法衡量其对下游智能体的易用性，缺乏针对智能体设计代码库能力的标准化评估基准。

### 方法关键点
- 两阶段评估范式：Design Phase被测智能体仅基于功能需求实现完整代码库，接口与抽象完全开放；Evaluation Phase使用3个不同模型族的下游智能体调用该库解决编程问题，综合下游代码的正确性和简洁度衡量库的质量
- 打分规则：最终得分=测试通过率平方×简洁度，简洁度取代码行数、Cyclomatic Complexity、Cognitive Complexity、Halstead Volume四项指标与人类生产级库参考实现的比值平均值，单指标比值上限为1
- 基准覆盖4种编程语言，包含15个代码库设计任务、242个专家验证的下游编程问题，所有问题可在无库场景下独立实现

### 关键实验
对比10款前沿编码Agent的代码库设计能力，Opus 5.5得分最高为48.9，比人类生产级库基线的46.6高2.3分；抽样审计显示64%的下游冗余代码来自Agent设计的库接口刚性或难用，仅14%来自能力缺失；给设计Agent增加Agent优先的设计引导、下游用例示例、子Agent预测试的干预后，得分提升2.3分，接近生产级库水平。

### 核心结论
为Agent设计工具或库的核心痛点并非能力缺失，而是接口易用性不足，评估工具的实际价值必须以下游Agent的真实使用效果为核心标准。
