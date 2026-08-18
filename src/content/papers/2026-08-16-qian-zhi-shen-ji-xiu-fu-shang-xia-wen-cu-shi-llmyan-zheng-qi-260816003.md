---
title: Prior Audit-Repair Context Shifts LLM Verifier Thresholds Toward Leniency
title_zh: 前置审计-修复上下文促使LLM验证器判定阈值趋向宽松
authors:
- Parsa Mazaheri
- Kasra Mazaheri
affiliations:
- University of California, Santa Cruz
- Massachusetts Institute of Technology
arxiv_id: '2608.16003'
url: https://arxiv.org/abs/2608.16003
pdf_url: https://arxiv.org/pdf/2608.16003
published: '2026-08-16'
collected: '2026-08-18'
category: LLM
direction: LLM验证器行为特性研究
tags:
- LLM Verifier
- Audit-Repair Pipeline
- False Alarm Reduction
- Threshold Shift
- Signal Detection
one_liner: 验证前置审计修复上下文可使LLM验证器误报率降9-25%，变化来自判定阈值而非判别能力
practical_value: '- 搭建LLM+Agent的自检修复pipeline时，可利用前置审计修复上下文降低验证模块误报率，减少不必要的内容/商品召回过滤损失

  - 做生成式推荐/广告文案的合规校验时，若前置放修复环节，需定期校准验证器阈值，避免漏过不符合合规要求的输出

  - 涉及多LLM协作的搜索推荐推理链路，不要将同一LLM同时用作修复器和验证器，避免阈值偏移导致的判别稳定性下降'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前LLM自检修复流水线普遍将同/异源LLM分别作为验证器、修复器，业界未关注这种架构排布是否会改变验证器的判定逻辑，导致误判率波动。
### 方法关键点
基于人类标注正确的ProcessBench数据集，控制当前任务完全一致，对比存在前置审计-修复上下文、长度匹配的非审计上下文两种场景下的LLM验证器误报率，结合信号检测分析定位效果来源。
### 关键结果
15组模型×prompt措辞组合均实现误报率下降，相对长度匹配对照组绝对降幅2.8~11.5pp，相对降幅9~25%；效果来自验证器判定阈值偏移而非判别能力变化，人工抽检显示82%的原始误报为错误判定，该阈值偏移无显著业务危害；开启CoT推理能力时效果仍稳定存在
