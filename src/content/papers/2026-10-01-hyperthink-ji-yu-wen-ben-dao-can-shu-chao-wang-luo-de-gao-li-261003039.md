---
title: 'HyperThink: Text-to-Parameter Hypernetworks for Efficient Reasoning'
title_zh: HyperThink：基于文本到参数超网络的高效推理框架
authors:
- Donggyun Kim
- Jack Lu
- Chanwoo Kim
- Mengye Ren
- Seunghoon Hong
affiliations:
- KAIST School of Computing
- NYU Courant Institute School of Mathematics, Computing, and Data Science
arxiv_id: '2610.03039'
url: https://arxiv.org/abs/2610.03039
pdf_url: https://arxiv.org/pdf/2610.03039
published: '2026-10-01'
collected: '2026-10-14'
category: Reasoning
direction: 大语言模型 · 高效推理 · 超网络参数自适应
tags:
- Hypernetwork
- Efficient Reasoning
- CoT
- VQ-VAE
- Parameter Efficient Tuning
one_liner: 通过轻量超网络生成查询条件化偏置更新，无需长思考链即可保留LLM推理能力并大幅降低延迟
practical_value: '- 电商实时导购/客服Agent优化：可将CoT推理的长思考链成本摊销为单次超网络前向的参数更新，无需生成<think>中间内容，延迟接近无思考模式，准确率损失极小，适配低延迟要求的实时对话场景

  - 推荐系统实时用户适配：VQ码本设计可复用在个性化参数自适应场景，将用户/query级的参数更新约束到有限语义原型，既防止过拟合，又提升跨域泛化能力

  - 高并发推理场景部署优化：仅调整基模型偏置参数的方案参数量仅为基模型的0.015%，预测和部署成本远低于LoRA/提示调优，适合端侧、高并发的推理服务'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
CoT及长思考链可大幅提升LLM多步推理能力，但推理时需要顺序生成大量思考token，延迟高、算力成本高，无法适配低延迟的业务场景；现有无思考推理方案又会显著损失复杂任务准确率，亟需平衡推理效果与效率的新范式。

### 方法关键点
- 框架上将推理过程转化为查询条件化的参数调制：用轻量超网络预测参数更新替代长思考链生成，基模型全程冻结，推理时仅需一次超网络前向即可完成自适应
- 极轻量参数更新设计：仅预测Transformer高层的偏置参数，更新参数量仅占基模型的0.015%，计算成本极低
- VQ瓶颈正则化：加入向量量化解码器将参数更新约束到有限可复用原型码本，搭配使用率正则化防止码本崩溃，大幅提升跨域泛化能力
- 训练时用基模型思考模式的输出做监督，对齐思考模式的响应分布，端到端优化

### 关键实验
在GSM8K、MATH-500、常识问答、代码生成等多类任务上测试，对比原生无思考、预算控制思考、System2蒸馏等基线：Qwen3-0.6B上MATH-500准确率比原生无思考高1.92%，FLOPs仅高20%；Olmo-3-7B上达到思考模式90%左右的准确率，延迟仅为后者的7-9%。

最值得记住的结论：无需显式生成思考token，通过查询条件化的极少量参数更新即可摊销推理成本，是平衡准确率和延迟的可行新范式。
