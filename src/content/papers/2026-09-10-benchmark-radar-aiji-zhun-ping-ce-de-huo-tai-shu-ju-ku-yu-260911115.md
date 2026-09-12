---
title: 'Benchmark Radar: A Living Database and Search Engine for AI Benchmarks and
  Evaluation'
title_zh: Benchmark Radar：AI基准评测的活态数据库与搜索引擎
authors:
- Koutian Wu
- Junjie Zhou
- Ergan Shang
- Jiayu Wang
- Pengqian Han
- Junkai Wang
- Wanghan Xu
affiliations:
- Earth-Space-AI
- Tacite AI
- Carnegie Mellon University
- Tsinghua University
- Shanghai Jiao Tong University
arxiv_id: '2609.11115'
url: https://arxiv.org/abs/2609.11115
pdf_url: https://arxiv.org/pdf/2609.11115
published: '2026-09-10'
collected: '2026-09-12'
category: Eval
direction: AI基准评测 · 活态检索库搭建
tags:
- Benchmark
- LLM Evaluation
- Search Engine
- Agent Evaluation
- Dataset Retrieval
one_liner: 构建覆盖多领域AI基准的活态数据库与搜索引擎，提供多维度检索、趋势分析及开放工具链
practical_value: '- 可复用「多源每日同步+源标识留存」架构搭建业务侧推荐/Agent效果评测数据集库，解决评测指标追溯难、版本混乱问题

  - 参考benchmark饱和分析方法，定期评估现有A/B实验指标、推荐排序评测集的有效性，及时替换饱和失效的评测维度

  - 借鉴分数-使用率帕累托前沿视图设计思路，搭建业务算法效果的多维度权衡看板，辅助算法选型决策'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
AI benchmark资源分散，LLM、Agent研发人员难以快速定位匹配的评测数据集、代码，也无法追溯公开分数对应的实验设置，导致评测复现难、选型效率低。
### 方法关键点
1. 对接37个数据源（13个直连连接器+24个官方科研工程信源），每日同步benchmark论文、代码仓、数据集、版本发布信息；
2. 构建带源标识、引用关系的可检索基准目录，留存模型卡、技术报告提及记录与分数变化历史；
3. 配套开放web dashboard、CLI查询工具、可下载数据集与复现分析脚本。
### 关键结果数字
当前目录包含来自4个基准目录的1283条源记录，覆盖790条基准的12916条数值观测，支持benchmark饱和度、采纳趋势分析、分数比较边界校验等功能。
