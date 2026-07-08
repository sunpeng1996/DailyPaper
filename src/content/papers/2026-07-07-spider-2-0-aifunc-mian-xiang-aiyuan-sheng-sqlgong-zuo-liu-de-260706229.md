---
title: 'Spider 2.0-AIFunc: Extending Real-World Text-to-SQL to AI-Native SQL Workflows'
title_zh: Spider 2.0-AIFunc：面向AI原生SQL工作流的Text-to-SQL扩展
authors:
- Tianyang Liu
- Canwen Xu
- Fangyu Lei
- Nikki Lijing Kuang
- Jixuan Chen
- Tao Yu
- Julian McAuley
- Zhewei Yao
- Yuxiong He
affiliations:
- UC San Diego
- Snowflake AI Research
- University of Hong Kong
arxiv_id: '2607.06229'
url: https://arxiv.org/abs/2607.06229
pdf_url: https://arxiv.org/pdf/2607.06229
published: '2026-07-07'
collected: '2026-07-08'
category: Eval
direction: AI原生SQL · Text-to-SQL评测基准
tags:
- Text-to-SQL
- Benchmark
- AI-Native-SQL
- LLM-Evaluation
- Agent
one_liner: 构建覆盖6类云平台AI函数的AI原生Text-to-SQL评测基准及测试集
practical_value: '- 电商用户评论/工单分析场景可直接复用云平台SQL原生AI函数，省去离线NLP任务链路，大幅降低分析开发成本

  - 自研Text-to-SQL Agent时，AI原生SQL场景无需过度设计schema检索、表选择等复杂模块，极简架构即可达到最优效果

  - 评估大模型企业级SQL分析能力时，可复用多轮跨时间窗口执行校验方法，保障生成SQL的结果稳定性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前主流云数据平台已内置LLM原生SQL函数，可直接在SQL中完成分类、情感分析、实体抽取、相似检索等任务，但现有Text-to-SQL基准仅覆盖传统SQL语法，无法评估模型生成AI原生SQL的能力。
### 方法关键点
基于现有企业级Text-to-SQL基准，通过Agent流水线将原始任务改写为AI原生形式，同步转换目标查询、优化自然语言指令降低歧义；所有实例经过多轮跨时间窗口重复执行校验，保证结果稳定；最终数据集覆盖Snowflake平台6类AI函数，包含125个真实数据库、465个验证通过的测试实例。
### 关键结果
最强闭源大模型执行准确率达67-70%，最优开源模型仅58.1%，误差主要来自谓词定义、schema对齐、AI函数参数配置错误；传统Text-to-SQL Agent的复杂schema检索、表选择策略对AI原生SQL场景无效，极简Agent效果相当甚至更优。
