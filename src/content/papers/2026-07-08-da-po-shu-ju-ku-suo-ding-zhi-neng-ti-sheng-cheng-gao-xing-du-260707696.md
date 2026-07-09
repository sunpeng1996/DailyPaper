---
title: 'Breaking Database Lock-in: Agentic Regeneration of High Performance Storage
  Readers for Database Bypass'
title_zh: 打破数据库锁定：智能体生成高性能存储读取器实现数据库旁路
authors:
- Victor Giannakouris
- Immanuel Trummer
affiliations:
- Cornell University
arxiv_id: '2607.07696'
url: https://arxiv.org/abs/2607.07696
pdf_url: https://arxiv.org/pdf/2607.07696
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: Agent 代码生成 · 数据库存储访问优化
tags:
- Agent
- LLM Code Synthesis
- Database Bypass
- Storage Reader
- Analytical Workload
one_liner: 通过LLM辅助代码合成自动生成数据库存储解析器，绕开驱动实现最高27倍分析吞吐量提升
practical_value: '- 离线特征计算场景可复用该思路，直接读取业务库底层存储文件绕开JDBC/ODBC，大幅提升特征抽取吞吐量，尤其适合T+1类批量特征加工

  - 可迁移Agent+LLM代码生成的范式，针对业务中自定义日志、存储格式等场景，自动生成解析代码降低人工开发成本

  - 生成的解析器直接输出Apache Arrow格式，可无缝对接Spark、DuckDB等常用离线分析引擎，减少格式转换开销'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有外部分析负载访问数据库需经过JDBC/ODBC等驱动层，这类层未针对批量列存分析优化，导致离线分析、读副本场景吞吐量低、延迟高，存在数据访问锁定问题。
### 方法关键点
Jailbreak框架利用LLM消化数据库存储格式的源码、文档，自动生成对应存储文件的解析读取组件，完全绕开数据库引擎与驱动层，直接读取底层存储文件并序列化为Apache Arrow列存缓冲区，可直接被DuckDB、Spark、GPU加速框架等通用查询引擎消费。
### 关键结果
在PostgreSQL、MySQL存储文件上基于TPC-H基准测试验证正确性，端到端分析吞吐量最高较JDBC/ODBC基线提升27倍，范式可泛化到所有有公开格式文档/源码的存储系统。
