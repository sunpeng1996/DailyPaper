---
title: 'PaperCompiler: Faithful Paper-to-Code Generation via Repository-Level Specification
  Compilation'
title_zh: PaperCompiler：基于仓库级规范编译的可信论文转代码生成框架
authors:
- Yunhao Liu
- Hong Phuc Pham
- Jaehong Yoon
affiliations:
- NTU Singapore
arxiv_id: '2609.02272'
url: https://arxiv.org/abs/2609.02272
pdf_url: https://arxiv.org/pdf/2609.02272
published: '2026-09-01'
collected: '2026-09-03'
category: Agent
direction: Agent 代码生成 · 多阶段规范约束
tags:
- Paper2Code
- Agent
- LLM4Code
- Repository Generation
- Specification Compilation
one_liner: 将论文实现证据编译为显式仓库级规范，大幅提升生成代码与原方法的保真度
practical_value: '- 做算法落地/复现类Agent任务（如顶会推荐/广告算法落地、基线复现）时，可借鉴「先将需求/论文证据编译为结构化规范，明确每个模块的所有权、不可降级要求、跨文件依赖」的思路，避免中间阶段信息丢失导致最终结果偏离需求

  - 生成多模块复杂系统（如推荐召回/排序链路、广告策略引擎）时，可引入「拓扑顺序生成+已提交公共接口不可修改」的约束，大幅降低跨模块API不兼容、语义不一致的问题

  - 评估复杂Agent生成结果的保真度时，优先采用「和官方实现对比的参考式评估」，比仅看表面符合度的无参考评估更易发现核心逻辑的简化与缺失'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有论文转代码Agent多以自由格式的规划、摘要作为阶段间传递的中间信息，下游编码环节易丢失、误读论文核心实现约束，导致算法逻辑被简化、跨模块语义不一致，生成代码与原方法保真度低，严重影响科研复现与算法落地效率。

### 方法关键点
- **论文Grounding**：提取实现蓝图与原文证据库，标记每个实现细节的来源、状态（论文明确支持/推断/未解决/外部依赖），对公式、算法、prompt模板等敏感信息直接留存原文，避免提前压缩丢失信息；
- **规范编译**：将沉淀的证据整理为不可降级的实现要求，分配每个要求对应的实现文件与接口，构建仓库级所有权图、跨文件依赖关系，最终生成每个文件的执行契约（接口定义、依赖、不可简化约束）；
- **约束引导生成**：按依赖拓扑顺序生成代码，已生成文件的公共接口、schema、输出语义不可修改，仅开放论文未明确规定的工程细节的实现自由度。

### 关键结果
在Paper2CodeBench的90篇ICLR/ICML/NeurIPS 2024论文上测试，对比PaperCoder、AutoP2C等SOTA基线，参考式保真度相对提升13.8%（3.64→4.15），高严重级错误率从13.2%降至6.1%，无参考评估、P2C-Ex评估分别提升4.7%、4.3%。

### 核心结论
可靠的复杂系统生成不仅需要更强的LLM，更需要对原始需求信息的表示、传播、消费过程进行显式约束，避免中间阶段的信息损耗和语义漂移。
