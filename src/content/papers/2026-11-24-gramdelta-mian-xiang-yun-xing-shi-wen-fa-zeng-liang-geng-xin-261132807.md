---
title: 'From Grammar Deltas to Token Masks: Incremental Constrained Decoding under
  Runtime Grammar Evolution'
title_zh: GramDelta：面向运行时文法增量更新的增量约束解码框架
authors:
- Hantao Hua
- Jiming Su
- Yonggang Che
- Feng Zhu
affiliations:
- National University of Defense Technology
arxiv_id: '2611.32807'
url: https://arxiv.org/abs/2611.32807
pdf_url: https://arxiv.org/pdf/2611.32807
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: LLM结构化生成 · 约束解码优化
tags:
- Constrained Decoding
- Structured Generation
- Earley Parser
- Incremental Computation
- LLM Inference
one_liner: 提出增量约束解码框架GramDelta，避免文法更新时重放前缀，大幅降低更新延迟与TPOT开销
practical_value: '- Agent工具调用、动态参数校验场景：电商导购Agent需要根据用户当前浏览的品类动态加载不同的工具/参数Schema时，可复用GramDelta的增量文法更新逻辑，避免每次Schema变更都全量重放历史前缀，降低动态约束的更新延迟

  - 动态结构化文案生成场景：比如商品详情页AI文案、个性化营销短信生成，需要根据实时用户特征/商品特征动态调整输出约束（如必须包含特定优惠、参数），可借鉴其增量状态维护机制，减少约束重建的冗余计算，提升生成TPOT

  - 工程实现trick：其历史依赖索引+无编译因子化Token投影的设计可直接复用，不需要每次约束更新都重编译Token掩码缓存，在约束频繁变更的场景下能大幅降低额外开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有文法约束解码只能处理固定前置文法，而代码生成、Agent工具调用、动态结构化输出等场景中，文法会随生成过程动态更新（比如新声明的变量、实时加载的工具Schema、随上下文新增的输出规则），现有方案遇到新文法更新时需要重放整个已生成前缀重建约束状态，存在大量冗余计算，延迟高、TPOT开销大，无法适配约束频繁动态变化的生产场景。

### 方法关键点
1. 历史Delta定位：维护非终端的历史等待位置索引，新增文法规则时直接定位到可以激活该规则的所有历史位置，不需要扫描全量历史状态，仅从受影响的位置开始更新
2. 增量Earley闭包：仅传播新增规则触发的Predict/Scan/Complete推导，不重放已生成前缀，理论证明更新后的状态和全量重建完全等价，无精度损失
3. 无编译因子化Token投影：结合文法无关的词汇位集快速过滤和共享历史的前缀树推导，直接生成更新后的下一词掩码，不需要每次更新都重编译掩码缓存

### 关键结果
在Qwen3-8B/32B、Granite-4.1-3B/8B共4个模型上测试，对比Fresh全量重建、XGrammar、llguidance等基线：中位数首次文法更新延迟降低10.7~11.5倍，相比最强基线llguidance，持续文法演化下的额外TPOT开销降低53.1~81.9%，无文法更新时引入的额外开销可忽略。

**最值得记住的一句话**：对于文法随生成过程动态增量更新的场景，增量维护约束状态比全量重建的效率提升可以达到一个数量级以上。
