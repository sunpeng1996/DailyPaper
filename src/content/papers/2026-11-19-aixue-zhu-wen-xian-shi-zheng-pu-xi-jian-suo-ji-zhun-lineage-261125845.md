---
title: 'LINEAGE: A Benchmark for Empirical Lineage Retrieval in AI Scientific Literature'
title_zh: AI学术文献实证谱系检索基准LINEAGE
authors:
- Pangjing Wu
- Xu Yuan
- Wenqi Fan
- Qing Li
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2611.25845'
url: https://arxiv.org/abs/2611.25845
pdf_url: https://arxiv.org/pdf/2611.25845
published: '2026-11-19'
collected: '2026-11-20'
category: Eval
direction: 学术文献检索 · 基准数据集构建
tags:
- Retrieval
- Benchmark
- Scientific Literature
- Graph Construction
- LLM Agent
one_liner: 构建覆盖17个AI顶会的大规模实证论文谱系检索基准与自动化构造工具
practical_value: '- 垂域检索基准构建可复用Lineage-Constructor的异构数据转化+证据校准思路，解决弱监督关联标注成本高的问题

  - 多跳关联检索评估可借鉴其结构指标设计，不局限单点召回，验证召回结果连通性是否满足业务需求，适配电商商品溯源、竞品关联等场景

  - 科研Agent的检索模块选型可参考该基准的19套系统测试结论，优先选择长路径关联召回鲁棒的方案'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有学术文献检索基准仅以主题相关性、引用链接为监督信号，无法捕捉论文间「作为实证对比基线」的谱系关联，无法支撑研究Agent的文献综述、实验规划等复杂任务需求。
### 方法关键点
定义实证谱系关联为「目标论文明确将前置工作作为实验对比基线」的关联关系，开发Lineage-Constructor工具，从异构论文元数据、全文基线证据中自动化构建校准后的谱系图，支持多跳检索的结构层面评估。
### 关键结果数字
基准覆盖2018-2025年17个AI顶会的12.1万篇论文，包含3950个图组件、6.75万个论文节点、16.49万条谱系边、8万条多面检索查询；测试19个主流检索系统，发现性能随谱系距离提升骤降，单点召回指标无法反映实际检索的结构连通性效果。
