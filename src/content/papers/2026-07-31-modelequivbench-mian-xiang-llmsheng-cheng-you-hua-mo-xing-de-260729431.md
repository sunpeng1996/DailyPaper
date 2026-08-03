---
title: 'ModelEquivBench: Certifying Multi-Relational Evaluation of LLM-Generated Optimization
  Models'
title_zh: ModelEquivBench：面向LLM生成优化模型的多关系可验证评估框架
authors:
- Penglin Zhu
- Jungang Xu
affiliations:
- School of Computer Science and Technology, University of the Chinese Academy of
  Sciences
arxiv_id: '2607.29431'
url: https://arxiv.org/abs/2607.29431
pdf_url: https://arxiv.org/pdf/2607.29431
published: '2026-07-31'
collected: '2026-08-03'
category: Eval
direction: LLM生成内容的细粒度可验证评估
tags:
- LLM Evaluation
- Certifiable Benchmark
- Optimization Model Generation
- Multi-relational Metrics
one_liner: 提出7层级可追溯多关系评估基准，解决LLM生成优化模型评估粒度粗不可验的问题
practical_value: '- 评估LLM生成的排序/优化类业务代码（如出价策略、召回规则）时，可复用E0-E6分层评估逻辑，替代单一运行成功率判断，避免逻辑正确但结构不同的生成结果被误判

  - 生成结果正确性验证可借鉴「可复现证据链」设计，每个判断维度配套可追溯的trace/反例，避免黑盒评估导致的业务风险

  - 对比不同LLM在代码生成类任务的表现时，可采用分阶段失败归因的思路，不用单一准确率做选型依据，匹配不同业务对生成结果的精度要求'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM生成优化模型的评估仅采用单一等价判定或执行成功率，既无法独立核验，也无法覆盖两种模型表述的多层等价场景，评估粒度极粗，结果可信度低。

### 方法关键点
提出ModelEquivBench多关系可验证评估体系，定义E0-E6共7层语义等价维度，从模型可加载、表征对齐、可行域匹配、目标序等价、最优值一致到最优解集等价逐层校验；每个判定结果配套可独立复现的证据（回放trace、显式映射、有理证书、反例等），不确定结果明确标注类型而非盲猜。

### 关键结果数字
在173个优化问题上测试GPT-5.4、Claude Sonnet 4.6、Qwen3.5-397B三款模型，分别有49/35/25个可运行的生成结果至少在一个等价维度不满足，三款模型在不同分层阶段失败，无法用单一准确率得分衡量。
