---
title: 'PosteriorBench: From Point Estimates to Posterior Matching in Evaluating Generative
  Inverse Solvers'
title_zh: PosteriorBench：面向生成式逆求解器的后验匹配评估基准
authors:
- Jiachen Yao
- Zi-Siang Hsu
- Xi Deng
- Aditi Gupta
- Xin Ju
- Sally M Benson
- Gege Wen
- Anima Anandkumar
affiliations:
- California Institute of Technology
- National Taiwan University
- Lawrence Berkeley National Laboratory
- Stanford University
- Imperial College London
arxiv_id: '2609.20794'
url: https://arxiv.org/abs/2609.20794
pdf_url: https://arxiv.org/pdf/2609.20794
published: '2026-09-17'
collected: '2026-09-19'
category: Eval
direction: 生成式模型评估 · 后验分布校准
tags:
- Benchmark
- Posterior_Matching
- Evaluation_Metric
- Uncertainty_Quantification
- Generative_Model
one_liner: 推出覆盖4类物理逆问题的后验分布评估基准及5维度量化评价体系
practical_value: '- 生成式推荐/Agent生成内容的评估可借鉴其多维度后验评估思路，在传统准确率指标外新增分布对齐、不确定性校准类指标，规避生成结果mode
  collapse、多样性不足问题

  - 针对用户行为稀疏的冷启动推荐这类ill-posed场景，可参考其后验方差调优方法，通过调整生成模型的guidance weight、输入噪声水平优化生成结果的分布匹配度

  - 多场景统一评估pipeline的设计思路可复用在生成式推荐的离线评测环节，对齐不同模型的评价标准，降低A/B测试筛选成本'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有生成式逆求解器评估仅关注单点重建准确率，不适配多解的ill-posed场景，无法识别mode collapse、过置信等后验分布偏差问题。
### 方法关键点
1. 推出PosteriorBench基准，覆盖达西流反演、泊松源恢复、碳捕获存储、光传输材质推理4类物理逆问题，采用拒绝采样、MCMC构建高保真参考后验
2. 配套5维评估指标：后验均值误差、后验标准差误差、最大均值差异、切片Wasserstein距离、径向平均功率谱误差，覆盖点精度、不确定性、分布对齐、频率保真维度
3. 基准适配稀疏感知、低分辨率输入、多噪声水平等场景，提供统一分布匹配与不确定性量化pipeline
### 关键结果
现有求解器普遍存在较大分布匹配gap，神经算子可提升分辨率鲁棒性，guidance weight与生成噪声是后验方差校准的核心参数
