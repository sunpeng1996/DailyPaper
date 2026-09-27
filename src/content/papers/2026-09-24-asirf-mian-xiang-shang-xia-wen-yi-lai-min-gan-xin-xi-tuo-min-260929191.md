---
title: 'ASIRF: An Agentic Framework for Context-Dependent Sensitive Information Redaction'
title_zh: ASIRF：面向上下文依赖敏感信息脱敏的智能体框架
authors:
- Sudha Priyadarshini
- Mohamed Chahine Ghanem
affiliations:
- University of Liverpool, UK
- Keele University, UK
arxiv_id: '2609.29191'
url: https://arxiv.org/abs/2609.29191
pdf_url: https://arxiv.org/pdf/2609.29191
published: '2026-09-24'
collected: '2026-09-27'
category: Agent
direction: Agent 敏感信息脱敏系统优化
tags:
- Agent
- Sensitive Information Redaction
- RAG
- Multi-Agent
- Open-source LLM
one_liner: 无需训练仅靠知识库更新的智能体脱敏框架，85%场景召回优于OpenAI隐私过滤器
practical_value: '- 电商/广告多业务域的用户隐私脱敏场景可直接复用该框架，无需为支付、客服、物流等不同域单独训练分类器，仅需更新知识库的敏感实体定义，适配成本降低90%以上

  - 小参数开源LLM搭配RAG做规则类垂直任务效果可超越预训练闭源基线，业务中可优先尝试4B-14B级开源模型+RAG的方案，平衡成本与合规效果

  - 可根据业务对 latency 和效果的要求选择架构：对精度要求高的合规场景选三阶段多智能体架构，对响应速度要求高的实时场景选单智能体架构，两者泛化性均优于固定分类器

  - 合规类任务评估可采用token级模糊匹配替代精确span匹配，避免边界判定误差导致的漏判，优先优化召回指标降低合规风险'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统敏感信息脱敏系统依赖训练时固定的实体分类体系，适配新业务域需要标注大量数据重新训练，成本高周期长，且完全无法识别未在训练中出现过的自定义敏感实体，无法满足电商、金融等多业务域动态变化的隐私合规要求。
### 方法关键点
- 提供两套可落地架构：ASIRF-Multi为三链式多智能体流水线，依次完成输入域分类、对应域敏感实体定义RAG检索、敏感值提取三步任务；ASIRF-Single为单智能体一站式完成所有任务，仅移除阶段拆分保留RAG能力，可用于对 latency 要求更高的场景。
- 知识库基于ChromaDB存储跨域敏感实体定义，采用HNSW索引做1024维语义检索，新增业务域仅需添加对应专家编写的敏感定义，无需标注数据和模型训练。
- 验证覆盖10款1B-14B参数的开源模型（Gemma-3、Qwen3、Ministral系列），跨两个推理平台，排除单模型特性对架构效果的干扰。
### 关键结果
- 8个测试数据集覆盖3个真实域、2个虚构OOD域、3个公开隐私数据集，基线为OpenAI Privacy Filter（OPF）固定训练的分类器。
- 85%（68/80）的模型-域组合下，至少一种架构的召回超过OPF；所有模型在虚构OOD域的召回均远超OPF，最小的Gemma-3-1B也优于基线；移除RAG后召回平均下降10~20pct，验证RAG的核心增益。

**最值得记住的结论**：规则类垂直域任务中，基于推理时知识库检索的智能体框架，泛化性和适配成本远优于训练时固定分类体系的方案。
