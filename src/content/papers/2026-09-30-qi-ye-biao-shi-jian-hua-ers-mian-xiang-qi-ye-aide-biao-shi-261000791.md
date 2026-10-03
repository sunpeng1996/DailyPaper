---
title: 'Enterprise Representation Simplification (ERS): Reducing Representational
  Complexity for Enterprise AI'
title_zh: 企业表示简化(ERS)：面向企业AI的表示复杂度降低方法
authors:
- Terry Dorsey
- Kevin Huggins
affiliations:
- Denodo Corporation
- Harrisburg University
arxiv_id: '2610.00791'
url: https://arxiv.org/abs/2610.00791
pdf_url: https://arxiv.org/pdf/2610.00791
published: '2026-09-30'
collected: '2026-10-03'
category: Other
direction: 企业AI表示复杂度度量与优化
tags:
- Enterprise AI
- Representation Complexity
- Cost Optimization
- Reasoning Performance
- Schema Optimization
one_liner: 提出与实现无关的企业表示复杂度度量ERC和简化框架ERS，支撑降本和AI推理性能提升
practical_value: '- 搭建企业级电商导购Agent、RAG问答系统时，可按ERC的4个维度裁剪冗余的知识库/schema表示，直接降低大模型推理负担，提升输出准确率

  - 跨业务域的推荐/广告系统迭代时，用ERS的经济模型评估表示简化方案的ROI，对比一次性改造成本和长期运维、推理成本收益，避免无效优化

  - 涉及Text-to-SQL的电商数据查询、用户行为分析场景，可直接复用「前置降低schema复杂度」的优化思路，无需额外算法改造即可提升推理效果'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
企业信息受应用、项目、组织边界、技术栈等多重因素影响，长期积累的表示复杂度极高，既提升企业运维治理成本，也增大AI系统的信息识别、关联、解释负担。

### 方法关键点
1. 定义ERS框架，在保留指定范围必要信息的前提下，裁剪不必要的表示冗余
2. 定义与实现无关的复杂度度量ERC，从表示对象、交互、行为、支撑源4个维度，分别在全局表示层、单任务层度量复杂度，可区分架构级简化和检索优化
3. 配套经济评估模型，拆分全局recurring运维成本、任务级recurring推理成本、一次性表示转换成本，可评估指定时间窗口内的简化ROI

### 关键结果
已有公开Text-to-SQL研究验证，降低schema与推理复杂度可有效提升推理准确率，任务级ERC下降可直接减少AI系统的处理负载
