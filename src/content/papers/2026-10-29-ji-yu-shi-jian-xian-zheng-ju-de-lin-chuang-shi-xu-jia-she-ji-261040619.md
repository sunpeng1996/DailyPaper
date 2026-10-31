---
title: 'Testimony from Timelines: Evidence-Grounded Significance Testing of Temporal
  Clinical Hypotheses'
title_zh: 基于时间线证据的临床时序假设显著性检验基准与范式
authors:
- Chengyang He
- Wenlong Zhang
- Koduvayur Subbalakshmi
- Ping Wang
affiliations:
- Stevens Institute of Technology
arxiv_id: '2610.40619'
url: https://arxiv.org/abs/2610.40619
pdf_url: https://arxiv.org/pdf/2610.40619
published: '2026-10-29'
collected: '2026-10-31'
category: Reasoning
direction: 大模型时序推理验证 · 基准构建
tags:
- Temporal Reasoning
- Statistical Testing
- Benchmark
- Clinical NLP
- Text-to-SQL
one_liner: 构建时序假设检验全链路标注基准STRATA，提出可审计的三阶段检验范式ART
practical_value: '- 电商业务中验证时序类假设（如大促后用户留存变化、商品召回后销量波动）可复用ART分阶段范式：先明确定义假设，再匹配对应样本，最后做统计检验，避免无依据下结论

  - 做业务效果归因、A/B测试结论校验时，不能仅看最终结论是否符合预期，需额外校验核心证据样本的选择准确率，规避「结论对但逻辑错」的伪正确问题

  - 用大模型做业务数据分析时，可提前给模型投喂标准化的业务规则codebook，能大幅降低大模型的中间决策错误，提升最终结论准确率'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有LLM回答时序因果类问题（如产品召回后销量是否下跌、疫苗副作用先后关系）时仅输出流畅结论，无统计显著性检验支撑；现有大模型数据分析基准仅校验最终结论，不校验中间过程的正确性，无法识别结论正确但证据选择错误的问题。
### 方法关键点
1. 构建STRATA基准，包含8735条基于疫苗不良事件临床时间线的假设，覆盖检验方案、证据集、p-value、结论全链路gold标注
2. 提出ART三阶段范式：清晰表述假设→检索匹配相关证据记录→执行统计检验，所有中间决策可审计
### 关键结果
ART解决了大部分结论-证据gap，同范式下31B开源模型效果与前沿闭源模型差距缩小到0.01以内，给前沿模型提供规则手册后准确率接近满分
