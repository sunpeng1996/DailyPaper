---
title: Why Does Post-Training Quantization Work?
title_zh: 揭秘大语言模型训练后量化（PTQ）生效的内在机制
authors:
- Yuxiang Chen
- Michael Beyer
- Jun Zhu
- Jianfei Chen
affiliations:
- 清华大学
- Bosch AI Research
arxiv_id: '2609.11716'
url: https://arxiv.org/abs/2609.11716
pdf_url: https://arxiv.org/pdf/2609.11716
published: '2026-09-10'
collected: '2026-09-11'
category: LLM
direction: 大语言模型 · 训练后量化鲁棒性
tags:
- Post-Training Quantization
- LLM Inference
- Quantization Robustness
- NVFP4
- Model Compression
one_liner: 发现层间误差抵消与LM头高置信预测保护机制，揭示预训练LLM训练后量化生效原理
practical_value: '- 部署LLM服务/Agent推理时可放心选用4-bit PTQ方案，主流预训练LLM天然具备量化鲁棒性，Qwen3-32B无校准NVFP4量化后平均精度仅掉0.43%，可大幅降低推理成本

  - 优化量化策略时可利用层间误差抵消特性，对抵消效应强的中间层采用更低比特量化，最终层保留更高精度以保护top-k token预测，适配搜索推荐场景的top结果稳定性需求

  - 电商/广告场景的生成式推荐、文案生成任务中，PTQ量化后top-ranked token预测保留率达85%以上，可满足业务对生成结果一致性的要求，无需额外微调'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
PTQ是当前LLM推理压缩的主流方案，业界普遍认为其效果损失小的原因是量化权重与全精度权重相似度高，但实验发现随机初始化模型与预训练模型的NVFP4权重重建余弦相似度几乎一致，前者的最终隐层误差却是后者的5.5倍，现有解释无法成立，亟需明确PTQ生效的内在机制。
### 方法关键点
- 对齐全精度与量化模型的输入，逐层计算隐状态误差、层更新误差的交互关系，推导隐层误差增长的精确递推公式，拆分误差增长的三类贡献项
- 分解最终隐层误差的长度/角度分量，结合高维LM头的几何特性，推导不同排名token的得分、概率变化的理论边界
- 开展反事实干预实验：移除/反转层间误差抵消效应，验证该机制对误差增长的因果作用
### 关键结果
- 覆盖Qwen3、OLMo3、Gemma3、OLMoE等密集/MoE架构，在C4、WikiText、GSM8K数据集上验证机制通用
- Qwen3-32B采用NVFP4 4-bit RTN无校准量化后，6项零样本基准平均精度仅下降0.43%，top1预测翻转率仅8.3%~12.7%，top10召回率保持85%左右
- 预训练模型的层间误差抵消可累计抵消63.4%的新增层误差，最终隐层误差中90%以上是角度旋转，高维LM头将旋转对top token得分的影响衰减近80倍

最值得记住的结论：预训练LLM的量化鲁棒性来自预训练过程习得的层间自校正误差抵消机制，而非单纯的权重重建精度。
