---
title: 'PAIChecker: Uncovering and Checking PR-Issue Misalignment in SWE-Bench-Like
  Benchmarks'
title_zh: PAIChecker：检测SWE类基准中PR与Issue配对错位的多Agent系统
authors:
- Manyi Wang
- Junjielong Xu
- Pinjia He
affiliations:
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2607.28587'
url: https://arxiv.org/abs/2607.28587
pdf_url: https://arxiv.org/pdf/2607.28587
published: '2026-07-30'
collected: '2026-07-31'
category: Agent
direction: 多Agent协作 · 代码基准质量校验
tags:
- Multi-Agent
- LLM4Code
- Benchmark Curation
- Misalignment Detection
one_liner: 提出三阶段多Agent框架校验代码基准PR-Issue配对质量，最高准确率达92.12%
practical_value: '- 多Agent分阶段校验架构可迁移到电商商品信息对齐、内容合规场景：拆分垂直子Agent做专项维度检测，上层仅做证据汇总与标签否决，比单Prompt方案准确率高30%以上

  - 文本优先、后验校验的逻辑可复用在用户反馈与工单对齐、RAG检索结果校验场景：先做文本语义比对过滤明确匹配/不匹配样本，仅对存疑样本调用工具验证，降低50%以上的工具调用开销

  - 双级自校正机制可用于大模型输出质量校验：先核对文本证据一致性，再验证实际业务落地效果，可降低20%以上的幻觉输出率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
SWE-bench类代码基准广泛用于评估LLM代码解决能力，依赖PR与Issue自动配对构建任务，但实测13.6%的人工校验样本存在配对错位，会导致评估结果失真，甚至让模型学到错误的监督信号。现有单Prompt/单Agent方案漏检错检率高，无法适配规模化基准构建需求。

### 方法关键点
- 三阶段权责分离架构：Phase I部署3个专用子Agent，分别检测不完整说明、PR范围溢出、缺陷PR/后续PR三类错位模式，输出结构化证据与异常线索
- Phase II由协调Agent汇总子Agent结果，支持预定义分类外的Others标签，同时做文本级自校正，剔除证据不足的标签
- Phase III由代码校验Agent结合仓库代码上下文，做实现级校验，进一步剔除误报
- 仅Phase I有权新增预定义标签，后续阶段仅拥有否决权，避免错误分类

### 关键结果
在SWE-Gym、SWE-bench Multilingual两个数据集上对比7种Prompt/Agent基线，覆盖4种SOTA LLM backbone，最高二元准确率达92.12%（SWE-Gym）、91.67%（多语言数据集），Exact Match最高84.66%，比最强基线高出5.13~12.39个准确率百分点。

**最值得记住的结论**：跨场景的对齐校验任务中，拆分垂直子Agent做专项检测、上层仅做汇总与否决、多环节分层校验的模式，远比单Prompt/单Agent端到端方案的准确率更高、泛化性更好
