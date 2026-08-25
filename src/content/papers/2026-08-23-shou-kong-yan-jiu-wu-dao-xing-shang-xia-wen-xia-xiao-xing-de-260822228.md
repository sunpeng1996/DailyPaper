---
title: 'Prompt-Based Abstention Fails Under Misleading Context: A Controlled Study
  of Small Frozen RAG Models'
title_zh: 受控研究：误导性上下文下小型冻结RAG模型的提示式拒答失效
authors:
- Yohanes Andre Setiawan
affiliations:
- Georgia Institute of Technology
arxiv_id: '2608.22228'
url: https://arxiv.org/abs/2608.22228
pdf_url: https://arxiv.org/pdf/2608.22228
published: '2026-08-23'
collected: '2026-08-25'
category: RAG
direction: RAG鲁棒性 · 拒答策略评估
tags:
- RAG
- Abstention
- Frozen LLM
- Benchmark
- Factuality
one_liner: 提出GRAB-RAG基准，证实小型冻结RAG的提示式拒答无法应对通顺的误导性上下文
practical_value: '- 电商RAG商品问答/客服场景，不要仅依靠IDK提示做拒答：爬取的错误参数、恶意植入的误导性内容会触发大量错误回答，需新增事实校验环节

  - 用小型冻结RAG的业务不要堆CoT做拒答：CoT对误导性内容的拦截提升不足3pct，反而会提升2.8pct的正常内容误拒率，浪费算力

  - 可复用两阶段拒答架构：先通过显式IDK提示过滤无信息上下文，再根据业务对准确率/覆盖率的容忍度，选择双阶段冲突校验或NLI校验拦截误导内容

  - 上线前必须单独构造误导性上下文测试集：仅测无上下文场景的拒答准确率会严重高估系统鲁棒性，漏过恶意内容攻击风险'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG的提示式拒答策略仅针对上下文缺失场景设计，但工业界检索到的网页上下文约25%存在冲突信息，通顺但事实错误的误导性上下文和上下文缺失是完全不同的两类问题，此前无系统基准验证小型冻结RAG在两类场景下的拒答表现差异。
### 方法关键点
- 构造GRAB-RAG配对基准：同一问题对应4种上下文（支持、部分退化、缺失、误导），误导性上下文通过实体替换生成，内容通顺无矛盾，仅核心事实错误
- 对比5种拒答策略：无拒答提示、显式IDK提示、CoT推理拒答、双阶段生成端冲突校验（上下文回答与闭卷回答F1匹配）、双阶段NLI蕴含校验
- 全链路用语法约束JSON解码，排除格式错误对结果的干扰
### 关键实验
在NQ、HotpotQA数据集上测试3款3.8B-8B冻结指令模型：显式拒答提示下，上下文缺失时回答率≤3%，但误导性上下文下回答率高达41.6%，其中63%的回答直接照搬植入的错误实体；CoT仅将误导场景回答率降至37.8%，但正常内容误拒率提升2.8pct；双阶段冲突校验将误导场景回答率降至13.3%，但正常内容误拒率升至49.8%；NLI校验将误拒率降至31%，但当模型参数记忆与误导内容一致时完全失效。

**最值得记住的结论**：提示式拒答本质是上下文充足性检查，而非事实一致性检查，无法仅靠prompt优化解决误导性上下文的拒答问题。
