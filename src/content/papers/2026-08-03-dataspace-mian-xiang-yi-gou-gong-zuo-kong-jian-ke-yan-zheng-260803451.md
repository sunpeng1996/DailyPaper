---
title: 'DataSpace: Benchmarking Data Agents for Verifiable Analytics over Heterogeneous
  Workspaces'
title_zh: DataSpace：面向异构工作空间可验证分析的数据Agent基准
authors:
- Boyan Li
- Zhuowen Liang
- Yupeng Xie
- Xiaotian Lin
- Tianqi Luo
- Xinyu Liu
- Yizhang Zhu
- Zhangyang Peng
- Yuan Li
- Zhengxuan Zhang
affiliations:
- HKUST(GZ)
- Tsinghua University
arxiv_id: '2608.03451'
url: https://arxiv.org/abs/2608.03451
pdf_url: https://arxiv.org/pdf/2608.03451
published: '2026-08-03'
collected: '2026-08-07'
category: Agent
direction: 数据Agent · 异构工作空间分析评测
tags:
- Data Agent
- Benchmark
- Multimodal
- Heterogeneous Data
- Deterministic Evaluation
one_liner: 发布跨模态跨语言可验证数据Agent基准，配套确定性表格结果评估体系
practical_value: '- 做业务数据Agent的评测体系可直接复用其确定性表格匹配逻辑：头无关列对齐、数值精度感知归一化、行顺序感知比较，避免LLM
  Judge的不稳定问题

  - 数据Agent构造可参考其失败分析结论：重点优化输出Schema匹配逻辑、跨模态证据对齐模块，这两个点占Grok 4.5失败案例的56.6%，优化性价比极高

  - 异构多源（商品库、运营文档、视频规则、财报等）数据问答的Agent架构选型可参考其实验结论：相同backbone下不同Agent harness能带来15.36pp的准确率差，优先选Grok
  Build/Claude Code类的成熟harness'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有数据Agent基准大多孤立测试结构化查询、检索或开放分析，未统一覆盖异构证据发现、完整表格输出、确定性评估三个核心需求，无法真实反映Agent在企业异构工作空间（数据库、结构化文件、长文档、多媒体共存）下的数据分析能力。

### 方法关键点
- 构建410个跨语言任务，覆盖金融、宏观经济、医疗3个领域，包含7439个共15.01GB的多模态工件，支持CSV/JSON/SQLite/Markdown/PDF/视频6种格式
- 配套DataSpace-Builder流水线：经跨语言转换、约束感知关系采样、模态路由与工件渲染、11位领域专家人工审核四阶段，生成带标准答案的评测任务
- 确定性评估器：实现头无关列对齐、类型与精度感知归一化、顺序感知行比较，无需LLM Judge即可完成表格结果的自动判分

### 关键实验结果
- 对比6个前沿多模态大模型、5个主流Agent harness：固定自研Agent harness时，Grok 4.5准确率最高为66.34%；固定MiMo-V2.5 backbone时，Grok Build准确率最高为46.34%，不同harness的准确率差达15.36pp
- 多模态证据融合、Join操作是通用性能瓶颈，所有模型的多模态任务准确率比单模态低1.8~14.0pp，Join任务准确率低9.7~19.8pp
- 失败分析显示：输出Schema匹配错误（目标理解偏差、列投影错误）占最强模型Grok 4.5失败案例的56.6%，是最主要的优化方向

### 核心结论
当前数据Agent在异构工作空间的可验证分析能力远未饱和，Agent harness架构优化的收益甚至高于大模型选型的收益
