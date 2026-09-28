---
title: 'Compact Documentation for Coding Agents: A Benchmark, an Optimizer, and Why
  It Does Not Transfer'
title_zh: 面向编码Agent的精简文档：基准、优化器及迁移失效原因
authors:
- Md Shohel Arman
- Igor Molybog
affiliations:
- Daffodil International University
- University of Hawaiʻi at Mānoa
arxiv_id: '2609.31587'
url: https://arxiv.org/abs/2609.31587
pdf_url: https://arxiv.org/pdf/2609.31587
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: Agent 编码任务性能优化
tags:
- Coding Agent
- Benchmark
- Prompt Optimization
- RAG
- Negative Result
one_liner: 构建编码Agent文档评估基准与优化prompt，发现高保真文档无法提升仓库问题解决效率
practical_value: '- 做Agent任务的prompt优化时，可复用往返评估基准：用输出反向还原输入的通过率作为优化信号，无需人工标注

  - RAG/上下文检索落地时要验证收益：不要默认加文档/检索上下文就有用，需做控制变量测试，避免无效工程投入

  - 做文档类prompt生成时，优先保证内容完备性而非长度，可大幅提升信息保真度'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
大代码库无法全量塞进Agent上下文，业界普遍假设高保真精简文档可替代未加载的源码，提升Agent问题解决效率，但该假设缺乏验证。
### 方法关键点
1. 提出roundtrip基准：通过「从描述重新生成的代码是否通过原测试」给文档打分，证明保真度核心驱动因素是内容完备性而非长度；
2. 用该基准作为优化信号，迭代出高保真文档生成prompt，可泛化到未见过的文件；
3. 设计含阳性对照的实验，验证文档对Agent解决真实仓库问题的增益。
### 关键结果数字
跨2个模型族、10个仓库的测试显示，当源码可访问时，静态精简文档、检索上下文都无法带来超过仅输入问题的性能提升，仅在Agent完全无法访问源码的边界场景下文档才有价值。
