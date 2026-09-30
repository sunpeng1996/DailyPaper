---
title: 'Alpha Diffusion Language Models: Factorization Alone Is Not the Problem'
title_zh: Alpha扩散语言模型：因子分解本身并非性能瓶颈
authors:
- Nikita Gushchin
- Dmitry Baranchuk
- Alexander Korotin
affiliations:
- Applied AI Institute, Moscow
- Yandex Research
- AXXX, Russia
arxiv_id: '2609.38066'
url: https://arxiv.org/abs/2609.38066
pdf_url: https://arxiv.org/pdf/2609.38066
published: '2026-09-29'
collected: '2026-09-30'
category: Training
direction: 扩散LLM并行生成优化
tags:
- DiffusionLM
- AlphaLoss
- ParallelDecoding
- SequenceLevelTraining
- FactorizedModel
one_liner: 用序列级alpha损失训练因子化扩散LM，大幅提升少步并行生成精度
practical_value: '- 电商/广告短文案、商品卖点批量生成场景，可引入序列级alpha损失微调扩散LM，用极少NFE生成合规内容，大幅降低推理成本，无需改模型架构

  - 推荐系统多属性并行生成场景（如同时生成商品标题、标签、推荐理由），用该损失可避免独立预测的token组合出无效结果，提升生成内容的一致性

  - 工程实现可直接复用mask归一化的alpha loss计算trick，适配不同长度序列的训练，无需依赖teacher模型蒸馏，训练pipeline改动量极小'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
离散扩散语言模型支持多token并行生成，相比自回归LLM推理时延更低，是高吞吐生成场景的重要方案。但传统交叉熵训练仅拟合单token边际分布，少步生成时独立预测的token容易组合出语义错误、语法无效的序列，此前的优化方案多依赖显式建模token依赖或teacher模型蒸馏，训练成本高且架构改动大。

### 方法关键点
- 提出序列级alpha损失，将广义交叉熵（alpha loss）作用于所有masked token的联合概率，α趋近于0时退化为普通交叉熵，α=1时最优解拟合序列联合模态
- 加入基于mask数量的归一化机制，保证不同长度、不同mask比例的样本损失权重一致
- 完全兼容原有因子化扩散模型架构，无需额外引入依赖模块，也不需要teacher模型生成的轨迹做监督，直接在带噪样本上训练即可

### 关键结果
在TinyGSM数据集训练，GSM8K数学推理基准评测，仅4次模型前向推理（NFE）时精度达34.6%，比采用相同采样器的MDLM基线高30.4个百分点，比同期最优其他基线高26.9个百分点；单步全并行生成时精度达7.66%，是最优token-wise alpha loss方案的3.6倍；迁移到1.7B参数的SDAR扩散模型后，GSM8K精度达77.2%，tokens per forward（TPF）比普通CE微调提升27.1%，代码生成场景下TPF提升11.5%且精度几乎无损失。

最值得记住的一句话：扩散语言模型并行生成的性能瓶颈并非因子化架构本身，而是传统训练目标未适配联合分布的拟合需求
