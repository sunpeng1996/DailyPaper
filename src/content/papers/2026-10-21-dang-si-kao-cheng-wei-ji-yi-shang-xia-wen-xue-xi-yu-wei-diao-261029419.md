---
title: 'When Thoughts Become Memory: Unifying In-Context Learning and Fine-Tuning'
title_zh: 当思考成为记忆：上下文学习与微调的统一框架
authors:
- Leon Chlon
- Julie Huang
affiliations:
- Hassana Labs
arxiv_id: '2610.29419'
url: https://arxiv.org/abs/2610.29419
pdf_url: https://arxiv.org/pdf/2610.29419
published: '2026-10-21'
collected: '2026-10-22'
category: LLM
direction: LLM 上下文学习与微调决策框架
tags:
- In-Context Learning
- Fine-Tuning
- Information Theory
- KV Cache
- Model Adaptation
one_liner: 提出信息论统一准则，可认证决策新数据应存入模型上下文或权重
practical_value: '- 做RAG/Agent的prompt优化时，可复用上下文价值评估方法：通过删除某段prompt上下文重跑的方式，无标注量化该段信息对任务的增益，快速过滤无效上下文、降低KV
  cache开销

  - 电商场景定制大模型时，可复用决策准则：小样本场景优先用ICL（上下文窗口可容纳时效果优于微调），样本量超过窗口阈值后再评估微调/LoRA的收益，避免盲目微调浪费算力

  - 可复用anytime-valid测试方法，线上AB测试时不用等固定样本量，随时可终止实验且错误率可控，适合推荐/广告策略的快速迭代'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有研究仅单独解释上下文学习（ICL）或微调的内在机制，缺乏跨架构、跨任务的统一量化准则，无法判定新数据应存入运行时上下文（如Transformer KV cache）还是写入模型权重，盲目选择易导致效果下降、算力浪费。
### 方法关键点
- 提出信息论统一增益定律：ICL和微调的预期增益均可拆解为「存储的查询相关比特数+先验修复项-解码损失」三部分，两类方法的收益可直接横向对比
- 无标注上下文价值评估：删除某段上下文后重跑模型，通过前后预测分布的KL散度量化该段的实际贡献，还可拆分内容增益和格式增益
- 任意时刻有效选择测试：基于离线查询的编码长度对比两类方案的效果，随时可停止测试且错误率可控，无需已知数据真实分布
### 关键实验结果
在Transformer、TabPFN、立体视觉网络、GPT-2等7类模型上验证，所有认证选择100%正确；GPT-2场景下64000条查询流中61948次选中更优方案，错误率最高3.3%；小样本表格任务上ICL模式的TabPFN编码效率比微调的XGBoost高30%以上。
### 核心结论
当上下文可完整放入模型窗口时，任何微调的收益上限都不会超过ICL的解码损失。
