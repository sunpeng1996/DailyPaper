---
title: 'Agentic Visual Generation: From Generative Models to Agentic Control'
title_zh: 智能体视觉生成：从生成模型到智能体控制层级框架
authors:
- Yinming Huang
- Shuyuan Tu
- Xi Yan
- Jiahao Zhan
- Zihan Yang
- Zhen Xing
- Hui Zhang
- Tiehua Zhang
- Yu-Gang Jiang
- Zuxuan Wu
affiliations:
- 复旦大学
- 上海创新研究院
- 香港中文大学MMLab
- 阿里巴巴通义实验室
- 同济大学
arxiv_id: '2609.06758'
url: https://arxiv.org/abs/2609.06758
pdf_url: https://arxiv.org/pdf/2609.06758
published: '2026-09-05'
collected: '2026-09-09'
category: Agent
direction: 智能体生成系统 · 能力层级划分
tags:
- Agent
- Visual Generation
- Control Hierarchy
- Evaluation Framework
- LLM
one_liner: 提出基于控制器决策因果可达范围的L0-L4智能体视觉生成层级框架与对齐评估方法
practical_value: '- 可复用L0-L4层级划分规则，对自家LLM+工具链的生成类Agent（如商品图/营销素材生成Agent）做能力定级，明确迭代路径

  - 层级对齐评估方法可直接复用：做不同Agent版本对比时固定生成器、工具、预算变量，仅迭代控制器决策能力，避免效果提升归因错误

  - L3结果自适应、L4经验复用的设计范式可迁移到推荐系统多轮交互场景：用户对推荐结果不满时自动触发召回/重排策略，沉淀跨会话用户偏好到长期记忆

  - 边界判定规则可用来清理伪Agent系统：避免把固定prompt工程、多步固定流程错当成Agent能力，减少研发资源浪费'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有智能体视觉生成领域缺乏统一的智能性判定标准，常将规划深度、工具调用、多角色协作等表面特征直接等同于智能性，无法准确衡量控制器的实际决策边界，也导致不同系统间的能力对比缺乏对齐基准，研发迭代易出现归因错误。

### 方法关键点
- 以控制器决策的最大因果可达范围为核心判定依据，划分L0（固定支持）-L4（经验自适应控制）共5个层级，每个层级配套可复现的判定规则，完全隔离系统架构、模型大小、输出质量等无关变量的干扰
- 提出层级对齐评估框架：对比不同能力系统时固定生成器、工具、算力预算、评估器等变量，仅扩展控制器决策范围，精准量化控制器能力的增量价值
- 构建覆盖200+代表性智能体视觉生成系统的结构化语料库，标注层级、任务、机制、反馈、记忆等10+维度字段，开源所有标注数据和统计工具

### 关键结果
对语料库的统计分析显示：2025年后智能体视觉生成领域的增长60%以上由L3（结果自适应控制）系统驱动；L4（跨任务经验复用）目前仍处于早期，占所有标注系统的比例不足10%；超过80%的系统采用单控制器架构，多角色协作架构占比不足20%。

### 核心结论
智能体的核心判定标准是决策的因果可达范围，而非采用的架构、工具数量、模型大小等表面特征
