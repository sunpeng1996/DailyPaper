---
title: 'Tytan: Interactive Neurosymbolic Construction of Analytic Semantic Schemas
  from Relational Data'
title_zh: Tytan：基于神经符号方法从关系数据交互式构建分析语义Schema
authors:
- Donna Hooshmand
- Shubham Shahi
- Cameron Barrie
- Abhratanu Dutta
- Marko Sterbentz
- Harper Pack
- Kristian J. Hammond
affiliations:
- Northwestern University
arxiv_id: '2608.06331'
url: https://arxiv.org/abs/2608.06331
pdf_url: https://arxiv.org/pdf/2608.06331
published: '2026-08-06'
collected: '2026-08-07'
category: LLM
direction: 神经符号系统 · 语义Schema自动构建
tags:
- Neurosymbolic
- Semantic Schema
- Relational Data
- LLM
- Interactive System
one_liner: 结合数据库符号分析与LLM语义推理，自动构建关系库语义Schema并对歧义点主动交互问询
practical_value: '- 做电商数仓语义层自动构建时，可复用「元数据符号规则+LLM语义推理」的混合架构，大幅降低人工标注Schema的人力成本

  - 落地LLM与结构化数据交互的系统时，针对LLM推理歧义点设计定向自然语言交互校验逻辑，可显著提升输出准确率

  - 语义类型识别、实体关联类任务可复用这套评估维度：覆盖度、检索正确性、语义角色准确率，直接对齐业务效用'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前数据分析工具依赖的语义层多为人工编写，存在知识获取瓶颈，限制分析系统扩展性，非技术用户高度依赖专家且人工输出易出错，亟需低成本高准确率的自动化语义Schema构建方案。
### 方法关键点
提出TYTAN系统，融合关系数据库符号分析（表结构、键值关联等规则）与LLM语义推理能力，完成实体提议、语义角色分配、命名三类核心任务；当推理结果置信度不足存在歧义时，自动生成定向自然语言问题向用户确认，兼顾自动化效率与输出准确性。
### 关键结果
在7个参考域数据集上实现100%的Schema覆盖度，1678条自建检索指令100%可正确执行，语义角色匹配准确率达92%-100%，少量与人工标注的不一致经核实为标注错误；在无显式外键的10表现实生产库盲测中，100%还原实体结构，满足5名独立盲测标注员的所有可满足预期。
