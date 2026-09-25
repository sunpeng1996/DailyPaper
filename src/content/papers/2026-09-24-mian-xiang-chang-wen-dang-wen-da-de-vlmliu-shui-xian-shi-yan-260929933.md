---
title: An Empirical Study of VLM Pipelines for Long-Document QA
title_zh: 面向长文档问答的VLM流水线实证研究
authors:
- Kenan E. Ak
- Jay Mohta
- Gwang Gook Lee
- Yan Xu
- Dimitrios Dimitriadis
affiliations:
- Amazon.com
arxiv_id: '2609.29933'
url: https://arxiv.org/abs/2609.29933
pdf_url: https://arxiv.org/pdf/2609.29933
published: '2026-09-24'
collected: '2026-09-25'
category: Eval
direction: 多模态长文档QA · 流水线选型
tags:
- VLM
- Long-Document QA
- RAG
- Agent
- Pipeline Evaluation
one_liner: 对比不同规模VLM下长文档QA流水线的输入、检索、Agent选型的性能与成本规律
practical_value: '- 处理带图表/表格的电商详情页、商品手册、平台规则类QA时，优先选图像检索（如ColQwen2.5、Nem-CE），比文本检索Hit@5高9pp以上，token消耗仅为全量输入的1/7~1/4

  - Agent架构选型严格匹配VLM规模：7B/9B级开源VLM不要用复杂Agent，静态top-k图像检索效果更好、成本仅为Agent的1/4~1/9；27B以上或API级VLM（如Claude
  Sonnet）选6工具FC Agent可获最优效果

  - 文本检索无需堆砌多阶段LLM pipeline，单阶段cross-encoder重排就能达到和多阶段方案几乎一致的效果，算力成本大幅降低

  - 文档图像渲染固定DPI=144即可，更高DPI不会提升VLM效果，还可能引入压缩损耗浪费算力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前VLM已广泛用于混合文本、图表、表格的长文档处理，但生产落地时输入模态选择、检索器选型、是否采用Agent架构三者的联合性能/成本 trade-off 缺乏系统的对照实验数据，过往研究多仅测试单维度优化，且常用宽松的LLM打分导致结果不可复现。
### 方法关键点
- 拆解长文档QA流水线为3个核心可变量：输入模态（原始PDF、全页图像、抽取文本、top-k检索图像）、检索器（词汇、稠密文本、视觉晚交互、重排4大类）、执行策略（静态流水线/6工具FC Agent）
- 统一测试4类VLM：Claude Sonnet 4.5 API、开源Qwen3.5-4B/9B/27B，全部采用基准自带的确定性打分器，避免LLM评判的偏置
- 自研6工具FC Agent：预提取文档结构目录，支持读指定页、取单图表、全文BM25搜索等工具调用，单query最多8轮交互
### 关键结果
- 采用Sonnet 4.5时，6工具Agent在MMLongBench-Doc准确率达0.625，比最强静态top-5检索高+9.2pp，输入token仅20k，为原始PDF输入的1/4；在LongDocURL准确率达0.659，与最强静态流水线持平
- 检索层面：图像检索比最强文本检索Hit@5高9pp，单cross-encoder重排的文本检索效果与复杂多阶段LLM检索流水线几乎一致（平均Hit@5 82.0 vs 82.4）
- 明确规模阈值：Qwen3.5-9B及以下开源VLM用Agent效果比静态top-k图像检索低最多9.3pp，token消耗为后者的4~9倍；27B以上VLM用Agent才会出现收益
> 最值得记住：长文档VLM流水线选型完全取决于所用VLM规模，小模型选静态图像检索，大模型选工具调用Agent，不要盲目堆复杂架构
