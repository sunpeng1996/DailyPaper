---
title: Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory
  Portability
title_zh: Agent 内存跨模型升级可移植性对照研究
authors:
- Ankit Goyal
- Jaideep Ray
affiliations:
- LinkedIn
arxiv_id: '2609.05339'
url: https://arxiv.org/abs/2609.05339
pdf_url: https://arxiv.org/pdf/2609.05339
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: Agent 长时记忆跨模型迁移优化
tags:
- Agent Memory
- Memory Portability
- RAG
- Knowledge Graph
- Model Migration
one_liner: 对比4种主流Agent内存格式的跨模型迁移鲁棒性，给出可落地的内存架构选型与迁移指南
practical_value: '- 电商导购Agent、用户偏好记忆系统优先选用固定Schema KG存储用户核心偏好、订单、履约等结构化事实，跨模型升级准确率波动仅±0.002，几乎无迁移损失；若采用NOTES格式存储自然语言记忆，必须单独测试每个writer→reader的迁移方向，避免最高13.28pp的准确率下降

  - 推荐/搜索的RAG召回系统升级embedding模型时禁止混用新旧向量索引，实测50/50混合索引仅能获得全量重索引41.6%的收益，损失近60%的准确率提升，必须全量重索引后再切流，或完全隔离新旧向量空间分别路由

  - 所有Agent长时记忆系统必须留存原始交互历史，仅基于已压缩的NOTES做修复无法达到90%性能恢复目标，保留原始历史的情况下，在适配的修复模型支撑下可实现70%+的场景性能恢复'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Agent系统迭代中模型升级是常态，但长时记忆的跨版本迁移缺乏标准化方案，容易出现新模型对旧记忆解读偏差、embedding空间不兼容导致检索失效、记忆修复无原始证据等静默故障，现有研究缺乏不同内存格式在相同迁移条件下的对照量化结果。
### 方法关键点
- 隔离记忆写入、读取、embedding三个可变模块，定义RPAS（迁移后性能保留率）、CTR（恢复成本）两个可量化指标；
- 横向对比4种工业界主流内存格式：LC-RAW（全量原始历史）、RAG（分块向量检索）、NOTES（模型压缩自然语言笔记）、KG-fixed（固定Schema知识图谱）；
- 采用48条带随机答案码的合成历史做测试，排除预训练知识干扰，使用exact match打分，无LLM裁判偏差，测试基座为Llama-3.1-8B-Instruct、Qwen2.5-7B-Instruct。
### 关键结果
- KG-fixed跨模型迁移准确率波动仅+0.0004±0.0020，几乎无损失；NOTES格式迁移准确率存在强不对称性，最高下降13.28pp、最高上升9.91pp；
- RAG系统embedding从bge v1.0升级到v1.5时，全量重索引准确率提升11.90pp，50/50混合索引仅提升4.96pp，损失近60%的潜在收益；
- NOTES仅靠存量存储修复无法达到90%性能恢复目标，留存原始历史时在适配修复模型支撑下可实现34/48场景达标；
- 故障溯源：NOTES 80%准确率损失来自写入阶段的信息丢失，RAG 81%损失来自检索阶段的召回错误。
### 核心结论
内存是Agent的长生命周期资产，而非当前模型的临时输出，模型升级应作为内存迁移事件来全链路验证，而非简单替换模型组件。
