---
title: Are These Modules Worth Their Cost? A Paradigm-Level Accuracy-Cost Analysis
  of In-context Learning Text-to-SQL
title_zh: ICL Text-to-SQL 范式级准确率-成本分析与配置指南
authors:
- Jiayan Lin
- Yujia Liu
- Zijin Hong
- Zheng Yuan
- Yilin Xiao
- Hao Chen
- Qinggang Zhang
- Xiao Huang
- Feiran Huang
affiliations:
- Jinan University
- The Hong Kong Polytechnic University
- City University of Macau
- Jilin University
- Beihang University
arxiv_id: '2608.28432'
url: https://arxiv.org/abs/2608.28432
pdf_url: https://arxiv.org/pdf/2608.28432
published: '2026-08-28'
collected: '2026-08-31'
category: Eval
direction: LLM 流水线成本准确率权衡评估
tags:
- Text-to-SQL
- In-context Learning
- Cost-Efficiency
- LLM Pipeline
- Accuracy-Cost Tradeoff
one_liner: 量化ICL Text-to-SQL各模块边际准确率-成本收益，给出可迁移的成本感知分层配置指南
practical_value: '- 搭建LLM驱动的业务Agent（如电商导购Agent、query改写、文案生成工具）时，优先加入执行反馈精修逻辑：仅当生成结果执行失败（如无召回、点击率异常、规则校验不通过）时触发改写，成本极低且收益普适

  - 预算有限时，优先对中端LLM做流水线优化（加少量检索、prompt增强模块），而非直接升级到顶级LLM用极简流水线，可在更低成本下拿到更高效果

  - 外部推理脚手架（CoT、问题拆解等）仅在非推理型LLM上添加，自带思考模式的推理LLM加这类脚手架大概率会增加成本且无收益甚至降效

  - 无特殊高准确率要求时，砍掉多候选生成+选择模块，这类模块受候选池上限限制，投入产出比极低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前ICL Text-to-SQL流水线不断叠加复杂模块，公开研究仅报端到端准确率，未量化单个设计的边际准确率增益与对应成本，从业者无法判断哪些模块值得投入，也没有统一的成本感知配置参考。

### 方法关键点
- 将通用ICL Text-to-SQL流水线拆解为5类核心模块（Example Retrieval、Schema Linking、Generation Strategy、Candidate Selection、Refinement），对应17种范式配置，统一控制变量实现隔离评估
- 覆盖4类不同能力、不同推理风格的主LLM Backbone，额外引入5个LLM做无调优迁移验证
- 定义CPP（每提升1个百分点Execution Accuracy的额外成本）为核心性价比指标，同时拆分输入、输出token开销来源

### 关键结果
在BIRD、Spider两个公开数据集上测试得到：
1. Execution-Feedback Refinement是唯一全Backbone通用的高性价比模块，提升1.83~4.89pp EX，CPP低于0.3 USD/pp
2. 固定预算下，中端LLM（Gemini-2.5-Flash）加优化后的流水线，准确率比顶级LLM（GPT-5.4）极简流水线更高，成本更低
3. 提炼的三级分层配置指南，在5个额外验证LLM上无调优直接迁移，Tier3相对基线Tier1提升3.98~7.63pp EX

### 核心结论
固定预算优先优化中端LLM的流水线架构，而非盲目升级更大的模型
