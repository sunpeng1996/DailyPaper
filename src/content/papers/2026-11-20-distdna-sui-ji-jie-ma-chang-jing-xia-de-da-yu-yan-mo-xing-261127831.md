---
title: 'DistDNA: Language Model Fingerprinting under Stochastic Decoding'
title_zh: DistDNA：随机解码场景下的大语言模型指纹识别
authors:
- Lifan Hu
- Qian Yu
- Zhaomin Wu
- Bingsheng He
affiliations:
- Department of Computer Science, National University of Singapore
arxiv_id: '2611.27831'
url: https://arxiv.org/abs/2611.27831
pdf_url: https://arxiv.org/pdf/2611.27831
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM行为指纹 · 模型身份校验
tags:
- LLM-Fingerprint
- Stochastic-Decoding
- MMD
- Model-Verification
- Distribution-Matching
one_liner: 提出无需分类器的DistDNA LLM指纹方案，提升随机解码场景下的模型身份识别准确率
practical_value: '- 业务LLM部署合规校验可复用DistDNA方案，无需训练分类器即可快速验证线上服务的LLM checkpoint是否符合预期，规避模型被篡改的安全风险

  - 做LLM输出分布对齐时，可借鉴prompt-wise MMD计算方法，量化不同解码参数下的输出分布差异，优化生成内容的一致性

  - 小样本估计模型输出分布时，可参考其O(1/R)的采样方差衰减规律，合理设置单prompt采样次数R，平衡识别准确率和计算成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM行为指纹方案未适配随机解码（温度、top-p参数差异）带来的同prompt输出波动，小样本下输出分布估计难度高，且解码参数变化对输出的影响量级与checkpoint变化相当，依赖多checkpoint训练分类器的方案落地成本高。

### 方法关键点
- 以prompt条件下的响应分布作为模型指纹，用逐prompt的最大均值差异（MMD）计算指纹距离
- 预存各已知checkpoint在多种解码参数下的参考指纹，比对时直接取最近邻匹配，无需额外训练分类器
- 理论证明有限采样带来的距离方差项随单prompt采样数R的增加以O(1/R)速度衰减

### 关键结果
在115个LLM checkpoint的测试集上，DistDNA相对最优基线LLM DNA的识别准确率提升10.36%
