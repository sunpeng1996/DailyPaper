---
title: Generalization behavior of OPTQ and the role of regularization
title_zh: OPTQ量化算法的泛化特性及正则化参数的作用
authors:
- Erin George
- Rayan Saab
affiliations:
- University of California, San Diego
arxiv_id: '2609.31560'
url: https://arxiv.org/abs/2609.31560
pdf_url: https://arxiv.org/pdf/2609.31560
published: '2026-09-25'
collected: '2026-09-28'
category: LLM
direction: 大语言模型 · 后训练量化优化
tags:
- OPTQ
- Post-training Quantization
- Regularization
- Generalization
- LLM Compression
one_liner: 推导OPTQ量化泛化误差边界，给出正则化参数λ最优取值，低采样场景下泛化性能优于现有方案
practical_value: '- 业务侧部署LLM做推荐/Agent服务时，若校准数据集规模小，可采用论文给出的λ=β·∥X∥_F²/(m^(1/3) min{m,N}^(2/3))（β取1）的参数设置，避免低采样场景下量化后模型泛化性能暴跌

  - 做垂直领域LLM后训练量化时，优先选择带正则化的OPTQ变体，相比传统经验λ设置方案，可在保证高采样场景精度的同时降低小校准集下的精度损失

  - 对于电商/推荐场景下微调的垂直领域LLM，量化时可复用论文的泛化误差边界公式预评估量化后的推理精度损失，减少上线前的全量测试成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有OPTQ量化的理论分析仅覆盖校准数据集内误差，缺乏泛化性研究，小校准集下OPTQ易过拟合校准数据的伪相关，导致推理阶段精度暴跌，且行业内现有λ参数设置方案在低采样场景下表现不稳定，缺乏理论支撑的最优取值规则。
### 方法关键点
- 推导两类OPTQ泛化误差上界：一类针对同分布测试样本，将校准集误差与泛化误差关联；另一类针对随机OPTQ，适配任意分布测试样本，两类边界均验证正则化λ的核心作用
- 基于误差边界最小化目标，给出λ的最优取值公式，无需依赖未知分布参数，仅通过校准集矩阵的统计量即可计算
- 提出随机OPTQ的二次型误差边界，可用于量化后参数的截断阈值预估，避免溢出误差
### 关键实验
在均匀Hadamard、非均匀Hadamard、ReLU神经网络输出三类分布下测试，对比现有λ设置方案（λ1=0.01∥X∥_F²/N、λ2=1e-3∥X∥_op），当校准样本量m<500时，β=1的λ设置方案可降低40%以上的测试误差，高m场景下与现有最优方案精度持平。
### 核心结论
OPTQ量化的正则化参数λ不能直接套用固定经验值，小校准集场景下按校准集F范数的幂率缩放设置λ可兼顾高低采样场景的泛化性能。
