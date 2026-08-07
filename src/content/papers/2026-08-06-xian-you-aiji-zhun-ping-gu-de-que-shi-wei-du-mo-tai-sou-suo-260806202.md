---
title: 'What Current AI Benchmarks Leave Unmeasured: Modality, Search, Citations,
  and Implications (for Safety Evaluations)'
title_zh: 现有AI基准评估的缺失维度：模态、搜索、引用与安全评估启示
authors:
- Ro Encarnación
- Tina Behzad
- Emma Lurie
- Danaé Metaxa
affiliations:
- University of Pennsylvania
- Stony Brook University
arxiv_id: '2608.06202'
url: https://arxiv.org/abs/2608.06202
pdf_url: https://arxiv.org/pdf/2608.06202
published: '2026-08-06'
collected: '2026-08-07'
category: Eval
direction: LLM安全评估体系优化
tags:
- LLM
- LLM Safety
- Benchmark
- Evaluation
- Web Search
- Consistency
one_liner: 对比ChatGPT不同访问模态与搜索开关的评估表现，指出现有LLM基准仅测单模态单轮准确率的缺陷
practical_value: '- 做LLM+推荐/Agent系统评测时，不能仅测API单轮准确率，需覆盖实际部署的访问模态、RAG/搜索开关场景，缩小评测与上线效果的gap

  - 电商导购、客服类Agent需新增重复prompt响应一致性评估项，避免21%的不一致回复导致用户体验下降、政策合规风险

  - 接入搜索/RAG的生成式推荐/问答系统，需额外评估引用溯源、拒答行为的稳定性，不能仅用准确率作为核心上线指标'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM基准评估普遍依赖单模态（仅API）、单轮prompt测试，仅输出准确率指标，未考虑部署场景的搜索功能、访问模态差异等变量，无法真实反映上线后的行为与安全风险。
### 方法关键点
抽取BBQ、SafetyBench两个常用安全基准的401条分层prompt，针对ChatGPT的聊天UI、官方API两种模态，分别测试有无开启web搜索的表现，每条prompt重复3次，共收集4812条回复，除准确率外额外评估一致性、文本相似度、引用溯源、拒答行为4个维度。
### 关键结果数字
关闭搜索时UI响应准确率低于API；开启搜索后准确率最高下降8pct，甚至反转两个模态的性能排名；相同prompt重复测试最高21%出现不一致响应；不同模态的引用来源、拒答行为均存在显著差异。
