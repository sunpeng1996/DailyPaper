---
title: 'Diminishing Returns of Data in Sparse Autoencoders: Functional Behavior does
  not Guarantee Feature Reproducibility'
title_zh: 稀疏自编码器训练数据收益递减：功能表现不保证特征可复现
authors:
- Sambit Ghosh
- Madelyn Mathai
- R. Venkatesh Babu
- Chirag Agarwal
affiliations:
- IBM
- Indian Institute of Science
- University of Virginia
arxiv_id: '2610.20680'
url: https://arxiv.org/abs/2610.20680
pdf_url: https://arxiv.org/pdf/2610.20680
published: '2026-10-13'
collected: '2026-10-17'
category: LLM
direction: LLM可解释性 · SAE训练数据效率
tags:
- Sparse Autoencoder
- Data Efficiency
- Mechanistic Interpretability
- Feature Reproducibility
- LLM
one_liner: 系统验证SAE训练数据需求随目标变化，功能收敛远早于特征可复现
practical_value: '- 若仅用SAE做LLM激活压缩/语义特征提取服务于推荐召回、Query理解，25M~50M激活token即可达到500M训练规模98%以上的重建/功能性能，可直接削减90%训练成本

  - 数据采样策略按需选择：追求重建精度、干预效果（如用户意图对齐、安全过滤）选随机采样；追求特征可解释性（如人工审核语义标签、特征归因）选FPS采样

  - 若需跨模型/跨批次对齐的稳定SAE特征（如统一Semantic ID体系、可复现的归因分析），不能仅以功能指标为达标依据，需补充特征对齐度校验，且训练数据规模至少提升1个数量级'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前稀疏自编码器（SAE）普遍依赖数亿到数十亿激活token训练，但其数据规模的必要性未被系统验证；同时业界常以功能指标达标作为训练完成标准，忽略功能收敛与特征可复现的差异，既造成训练成本冗余，也无法保障特征级应用的可靠性。
### 方法关键点
- 控制变量实验设计：固定3款LLM（Gemma-2-2B、Pythia-160M、Qwen3-8B）、4类SAE架构、超参数，仅调整激活数据规模（5M/25M/50M/500M）与采样策略（随机采样、最远点采样FPS）
- 双维度评估标准：功能收敛覆盖SAEBench全量指标（重建、稀疏探测、AutoInterp、干预类指标等），特征收敛采用匈牙利匹配计算编码器/解码器的特征对齐度
- 理论框架明确特征可复现的3个必要条件：统计一致性、优化一致性、特征可识别性，仅功能收敛无法满足全部要求
### 关键结果
- 功能层面：5M token即可达到500M参考模型98%以上的重建精度，25M~50M时多数功能指标与500M差距小于2%，部分场景小数据甚至优于大数据
- 特征层面：Gemma-2-2B BatchTopK的严格对齐特征占比，5M时仅2.2%，50M时仅提升至28.9%，随数据规模持续增长无饱和
- 采样策略差异：随机采样的重建精度比FPS高1~3个百分点，FPS的AutoInterp得分比随机采样高2~4个百分点，分别适配不同目标
### 核心结论
SAE训练数据需求完全取决于业务目标，不要默认选用最大规模数据集，功能达标不代表特征可复现
