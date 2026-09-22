---
title: 'BI-Agent and BI-Bench: Towards Automating End-to-End Business Intelligence'
title_zh: BI-Agent与BI-Bench：实现端到端商业智能流程自动化
authors:
- Chuxuan Hu
- Yeye He
- Penny Zhou
- Wee Hyong Tok
- Daniel Kang
- Surajit Chaudhuri
affiliations:
- UIUC
- Microsoft Research
- Microsoft
arxiv_id: '2609.20886'
url: https://arxiv.org/abs/2609.20886
pdf_url: https://arxiv.org/pdf/2609.20886
published: '2026-09-15'
collected: '2026-09-22'
category: Agent
direction: BI Agent 工具增强与领域后训练优化
tags:
- LLM Agent
- Business Intelligence
- Benchmark
- Tool Augmentation
- Post-training
one_liner: 构建首个端到端BI基准BI-Bench，提出工具增强+领域后训练的BI-Agent大幅提升任务准确率
practical_value: '- 电商/运营类多表ad-hoc分析场景可复用BI-Agent的工具设计思路：将领域专用的多表检索、跨表关联、非标准表格式转换逻辑封装为LLM可调用工具，大幅降低LLM直接处理复杂结构化数据的出错率

  - 小模型领域适配可复用本文的训练轨迹合成方案：基于真实业务Schema自动合成查询、生成标准答案，再用大模型生成成功执行轨迹做SFT+RL，无需大量人工标注即可快速提升小模型的领域工具调用、代码生成能力

  - 领域Agent benchmark构建可借鉴BI-Bench思路：从真实业务已落地产出（如电商运营看板、分析报表）提取真实query和标准答案，避免合成query与实际业务需求脱节'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统BI流程需人工完成表检索、数据转换、跨表关联、分析建模全步骤，非技术用户门槛极高；现有NL2SQL类基准仅关注最终查询生成环节，未覆盖端到端BI全流程的真实挑战，前沿LLM在真实BI场景下准确率不足50%，无法直接落地。
### 方法关键点
- 构建BI-Bench基准：从公开爬取的3K+真实Power BI项目中，人工筛选标注100组真实业务query与对应标准答案，覆盖销售、金融等多领域，包含多表关联、非结构化原始表等真实场景挑战。
- BI-Agent架构：采用工具增强的Agent编排框架，封装3种领域专用工具：表搜索工具筛选query相关表、转换工具自动完成pivot/unpivot等表结构归一化、关联工具自动预测多表join关系，搭配通用代码执行工具完成分析。
- 领域后训练方案：基于真实BI项目Schema自动合成训练任务，生成7K+带标注的多步工具调用轨迹，先后用SFT、GRPO强化学习（带可验证结果奖励）优化小模型的BI任务处理能力。
### 关键结果
在BI-Bench上对比24款模型与SOTA NL2SQL系统：1. 工具增强的BI-Agent比原生LLM准确率最高提升40pct，平均提升10pct以上；2. 经过SFT+RL后训练的8B参数Qwen3版本BI-Agent，效果追平大尺寸前沿模型，推理成本降低50倍；3. 现有SOTA NL2SQL系统在BI-Bench上准确率仅6%~26%，远低于BI-Agent表现。

> 值得记住：复杂领域Agent的性能提升，来自工具层的领域专用算法封装与模型层的领域后训练的协同优化，而非单纯依赖通用大模型的推理能力
