---
title: Can an Agent Debug a Web Corpus? Agentic Auditing of Slovak FineWeb2
title_zh: Agent驱动的网页语料缺陷审计框架及斯洛伐克语FineWeb2验证
authors:
- Marek Šuppa
- Ivan Vykopal
- Jaroslav Kopčan
affiliations:
- Comenius University in Bratislava
- Cisco Systems
- Kempelen Institute of Intelligent Technologies (KInIT)
- Brno University of Technology
arxiv_id: '2610.31636'
url: https://arxiv.org/abs/2610.31636
pdf_url: https://arxiv.org/pdf/2610.31636
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent工具调用 · 语料质量自动化审计
tags:
- Agentic Workflow
- Corpus Curation
- LLM Tools
- Data Quality
- Test Automation
one_liner: 提出将LLM作为语料调试器的Agent审计工作流，输出低成本可复用的缺陷检测规则
practical_value: '- 可复用「Agent探索+人工校验+可执行测试」三级工作流，做推荐语料/用户评论/广告素材库的自动化脏数据审计，比全量LLM标注成本低1000倍以上

  - 工具设计上给Agent开放只读的统计/采样/检索接口，严格限制数据读取预算，既降低调用成本又避免数据泄露

  - 电商/广告场景脏数据检测优先把发现的模式沉淀成元数据规则而非持续调用LLM，单规则全库扫描耗时可压缩到秒级'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多语言语料生产普遍采用统一流水线，无法针对每个语种做定制化质量校验，传统人工审计仅能单次生效不可复用，全量LLM分类打标成本极高（26M文档标注成本达1.2万-9万美元），亟需低成本、可沉淀的语料质量审计方案。

### 方法关键点
- 三级工作流设计：Agent通过只读预算API探索语料输出候选缺陷规则→母语者盲标注校验规则准确率→无LLM/GPU依赖的测试运行器执行规则
- 给Agent开放11个限定工具：聚合SQL查询、条件采样、文本检索、句子级语言识别、候选检测器校验等，仅文档读取消耗预算，统计类操作免费
- 零先验提示词设计：不预设缺陷类型、不指定邻接语言，仅要求输出的规则可复现、有全量覆盖率统计、经过样本验证

### 关键结果
- 在2650万篇斯洛伐克语FineWeb2语料上实测，单轮Agent运行成本仅2.21-2.84美元，发现7类缺陷，其中6类经人工验证准确率53%-100%，最大的机器生成内容农场占比5.32%（140.8万篇），86.6%通过了原流水线的所有过滤规则
- 沉淀的7条元数据规则全库扫描仅需0.7秒，成本是全量LLM分类的1/17000
- 与静态采样基线对比，最佳基线（低置信度样本采样）每轮成本仅1.03美元，可发现更多缺陷，但Agent输出的规则自带全量覆盖率统计、反例说明，大幅降低后续人工整理成本

### 核心结论
不要用LLM全量做分类打标，要用它一次生成可复用的检测规则，把单次推理的价值放大百万倍
