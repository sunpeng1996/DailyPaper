---
title: 'Pinocchio: Fast Uncertainty Estimates for Black-Box Language Models'
title_zh: Pinocchio：面向黑盒大语言模型的快速不确定性估计
authors:
- Kevin David Hayes
- Arka Pal
- Haosong Zhang
- Tom Goldstein
- Micah Goldblum
affiliations:
- University of Maryland
- Ritual AI
- Fudan University
- Columbia University
arxiv_id: '2609.24881'
url: https://arxiv.org/abs/2609.24881
pdf_url: https://arxiv.org/pdf/2609.24881
published: '2026-09-21'
collected: '2026-09-22'
category: LLM
direction: LLM 黑盒不确定性校准
tags:
- Uncertainty Estimation
- Black-box LLM
- LoRA
- Zero-shot Transfer
- Multimodal
one_liner: 基于多模型响应训练的轻量外部校准器，无需黑盒LLM内部信息即可单步预测回答正确率，支持跨模型零样本迁移
practical_value: '- 业务中使用闭源API大模型做客服答疑、商品文案生成、导购问答时，可直接集成开源`pinocchio-uq`包，2行代码实现回答正确率预判，过滤幻觉避免给用户传递错误信息

  - 训练业务专属不确定性校准器时，可复用其数据策略：优先选择模型准确率20%-80%的难例，补充多模态任务数据增强训练信号，混合高低能力模型的响应数据提升跨模型迁移性

  - 校准器可轻量化部署：0.8B小 checkpoint 即可达到8B模型99%的AUROC性能，推理仅需单步前向，无额外采样开销，适配低延迟业务场景

  - 跨模型部署时如果校准偏移，仅需100条标注样本做Platt/Isotonic后校准即可大幅降低ECE，不需要全量重训'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM不确定性估计方法要么需要白盒权限（logits、权重、微调权限），要么依赖多轮采样导致推理成本升高5-10倍，或者 verbalized 置信度校准差、存在模型盲区；而工业界大量使用的闭源API大模型（GPT、Claude等）不开放内部信息，高风险场景（如电商导购、Agent自动执行）缺乏低成本高可靠的不确定性校验能力。

### 方法关键点
- 架构：基于Qwen3-VL-8B-Instruct做LoRA微调（r=32，α=64），文本任务用灰度占位图统一多模态输入格式，输入包含问题、回答、可选模型ID/基准元数据，输出为回答正确/错误的二分类概率，仅在最后token计算交叉熵损失
- 数据策略：混合7款不同能力LLM在20个跨域基准（9个文本+11个多模态）上的3.2万条带标注响应，优先选择模型准确率20%-80%的难例保证正负样本均衡，拒绝/空回答标注为错误
- 推理：仅需单步前向，无需访问目标LLM的任何内部信息、不需要多次采样

### 关键结果
训练集内7款LLM的回答正确性预测AUROC达0.862，远超verbalized置信度等单步黑盒基线（最优基线仅0.649）；零样本迁移到13款未见过的跨厂商LLM，平均AUROC达0.814，0.8B小checkpoint可保留大模型99%的AUROC性能；仅需100条标注样本做后校准，即可将零样本迁移后的ECE从0.259降至0.058。

最值得记住的结论：小参数外部校准器预测黑盒LLM回答正确性的效果，远好于LLM自身输出的置信度。
