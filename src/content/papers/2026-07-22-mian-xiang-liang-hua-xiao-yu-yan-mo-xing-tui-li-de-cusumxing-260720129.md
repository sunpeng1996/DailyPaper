---
title: CUSUM-Shaped Inference-Time Monitoring and Targeted Re-Decoding for Quantized
  Small Language Model Reasoning
title_zh: 面向量化小语言模型推理的CUSUM型推理时监控与定向重解码
authors:
- El Hassane Ettifouri
- Ayoub Belfatmi
- Mahaman Sanoussi Yahaya Alassan
- Walid Dahhane
affiliations:
- Novelis Research, Paris, France
arxiv_id: '2607.20129'
url: https://arxiv.org/abs/2607.20129
pdf_url: https://arxiv.org/pdf/2607.20129
published: '2026-07-22'
collected: '2026-07-23'
category: LLM
direction: 量化小语言模型 · 推理时监控优化
tags:
- Quantized LLM
- Inference Optimization
- KV Cache
- CUSUM
- Test-time Tuning
one_liner: 提出MGT-B推理时监控回退框架，修复量化小语言模型推理无效轨迹以提升准确率
practical_value: '- 电商Agent采用轻量化量化LLM推理时，可复用MGT-B的CUSUM监控逻辑，检测重复/无效生成轨迹，减少无意义token消耗，降低推理成本

  - 生成式推荐/广告文案生成场景，可借鉴回滚+KV cache状态恢复的重解码方案，在不影响正常生成性能的前提下修正退化输出

  - 对推理时延敏感的搜索推荐场景，可参考该框架的选择性监控策略，仅对触发告警的轨迹做重解码，平衡准确率和推理开销'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：量化小自回归推理模型易进入长重复、无效生成轨迹，但现有推理流程不会根据生成轨迹动态分配计算资源，导致准确率损失和算力浪费。
**方法关键点**：基于token级e-CUSUM控制器改进得到MGT-B外部控制器，将预采样不确定性、退化特征的重叠窗口映射为位置相关的经验尾概率；采用带CUSUM型重置的混合投注因子累积机制触发告警；告警后自动估算回滚点，恢复token与KV cache状态，执行约束重解码修正轨迹。
**关键结果数字**：在467对历史覆盖测试集上准确率提升4.5个百分点（McNemar p=0.000753）；316条未触发告警的输出与原生模型完全一致，151条告警轨迹共带来29次纠错、仅8次效果倒退。在240对时间序列审计集上准确率提升2.5个百分点。
