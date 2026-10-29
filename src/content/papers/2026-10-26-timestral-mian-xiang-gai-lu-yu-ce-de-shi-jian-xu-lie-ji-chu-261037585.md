---
title: Timestral
title_zh: Timestral：面向概率预测的时间序列基础模型系列
authors:
- Adrien Petralia
- Alexandre Gavaudan
- Artjom Joosen
- Etienne Goffinet
- Richard Kurle
- Yassine El Ouahidi
- Yassir Bendou
- Abdelaziz Bounhar
- Abhijeet Somani
- Aditi Kabra
affiliations:
- Mistral AI
arxiv_id: '2610.37585'
url: https://arxiv.org/abs/2610.37585
pdf_url: https://arxiv.org/pdf/2610.37585
published: '2026-10-26'
collected: '2026-10-29'
category: Other
direction: 时间序列基础模型 · 概率预测优化
tags:
- Time_Series_Forecasting
- Foundation_Model
- Probabilistic_Forecasting
- Decoupled_Horizon_Forecasting
- Open_Source
one_liner: 推出4种参数量的时序预测基础模型系列，3项核心优化在三大基准达SOTA，权重与代码全开源
practical_value: '- 电商销量、流量、库存、广告投放效果预测场景可直接复用开源Timestral模型，基于业务数据做LoRA微调即可快速落地，降低建模成本

  - 训练时序类预测模型时可复用Decoupled Horizon Forecasting（DHF）机制，无需掩码上下文即可训练长预测窗口，降低训练复杂度同时提升效果

  - 时序类模型预训练可参考两阶段 pipeline：先基于大规模合成数据预训练，再用真实+合成混合数据做post-training，解决真实标注数据不足问题'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有时间序列基础模型存在长预测窗口训练需掩码上下文、对已知未来协变量支持差、真实训练数据覆盖有限导致泛化性不足等问题，单步前向覆盖的上下文/预测窗口组合少，训练效率低。
### 方法关键点
1. 采用Decoupled Horizon Forecasting（DHF）机制，分离预测token与因果编码上下文，长窗口训练无需掩码上下文，每个观测值同时作为预测目标和后续预测的上下文，单步前向即可覆盖多组上下文/窗口组合
2. 原生支持因果架构下的已知未来协变量输入
3. 两阶段训练pipeline：第一阶段仅用大规模多样化合成语料预训练，第二阶段用真实+合成混合数据、扩展上下文长度做post-training
### 关键结果
推出5M、28M、123M、209M四种参数量的Timestral模型系列，在GIFT-Eval、TIME、fev-bench三大基准上，209M与123M版本包揽所有指标前两名，所有模型权重开源至Hugging Face，推理代码开源至GitHub。
