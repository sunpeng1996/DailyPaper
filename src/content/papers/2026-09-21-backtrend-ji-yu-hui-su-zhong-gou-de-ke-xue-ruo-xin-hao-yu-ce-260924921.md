---
title: 'BackTrend: Evaluating Scientific Weak-Signal Prediction via Backward Reconstruction'
title_zh: BackTrend：基于回溯重构的科学弱信号预测评估基准
authors:
- Xiao Zhou
- Yilun Zhao
- Owen Jiang
- Tiansheng Hu
- Cai Xu
- Manasi Patwardhan
- Arman Cohan
affiliations:
- Yale NLP Lab
- New York University
- TCS Research
arxiv_id: '2609.24921'
url: https://arxiv.org/abs/2609.24921
pdf_url: https://arxiv.org/pdf/2609.24921
published: '2026-09-21'
collected: '2026-09-22'
category: Eval
direction: 弱信号预测 · 基准评测
tags:
- Weak Signal Prediction
- Benchmark
- LLM Evaluation
- RAG Evaluation
- Agent Evaluation
one_liner: 构建了AI/ML领域人类验证的弱信号预测回溯基准，评测了现有LLM、RAG、Agent系统的预测性能
practical_value: '- 电商新品/新赛道弱信号挖掘场景可复用回溯标注范式：用成熟爆品反推早期信号构建标注集，解决冷启动标注难问题

  - 评测趋势预测类Agent/RAG系统时，可复用语义匹配+覆盖率双维度指标，避免只看表面合理性忽略真实对齐度

  - 趋势预测类系统仅增加检索/网页搜索资源到中等阈值后收益见顶，需优化信号关联建模而非单纯堆检索量'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有趋势追踪、引文预测等领域缺乏将早期前驱信号与后续成熟范式绑定的验证参考集，弱信号预测效果无法可靠度量。
### 方法关键点
1. 构建BackTrend回溯基准，给定成熟目标主题和时间证据约束，要求系统恢复两类前驱信号：问题域（未被重视的研究问题）、解决方案域（已知问题的新兴方法）
2. 覆盖25个AI/ML成熟主题、66条人类验证弱信号，基于2019-2024文献发表频率轨迹重构得到
3. 采用语义匹配、覆盖率两类指标评测前沿LLM、RAG、研究类Agent系统
### 关键结果
最强系统仅实现10.1% F1，Coverage10最高仅18.5%；增加检索/网页搜索证据在中等预算内可提升性能，但无法填补核心性能缺口
