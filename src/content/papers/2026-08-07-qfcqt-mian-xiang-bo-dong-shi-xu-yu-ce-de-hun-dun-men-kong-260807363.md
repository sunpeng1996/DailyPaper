---
title: 'QFCQT: A Chaotically Gated Quantformer Framework for Volatile Time-Series
  Forecasting'
title_zh: QFCQT：面向波动时序预测的混沌门控Quantformer框架
authors:
- Junkai Lin
- Siqi Hou
- Raymond Lee
affiliations:
- Faculty of Science and Technology, Beijing Normal-Hong Kong Baptist University,
  Zhuhai, China
- Guangdong Provincial Key Lab of Interdisciplinary Research and Application for Data
  Science (BNBU), Zhuhai, China
arxiv_id: '2608.07363'
url: https://arxiv.org/abs/2608.07363
pdf_url: https://arxiv.org/pdf/2608.07363
published: '2026-08-07'
collected: '2026-08-10'
category: Other
direction: 波动时序预测 · Transformer 激活优化
tags:
- Time-Series-Forecasting
- Transformer
- Activation-Function
- Gating-Mechanism
- Non-stationary-Data
one_liner: 引入可学习振荡器激活与混沌门控，提升Transformer对非平稳波动时序的预测性能
practical_value: '- 电商大促、流量波动等非平稳业务时序预测场景，可复用平滑-混沌门控融合机制，平衡常规模式与突变场景的拟合效果

  - 推荐系统用户行为序列、广告点击时序建模中，可尝试引入可学习振荡器激活+时序最大池化组合，提升对局部波动突变的敏感度

  - 多模态时序特征融合时，可参考多参数化振荡器软叠加思路，自适应适配不同分布的输入特征响应模式'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
非平稳时序预测存在长程依赖、局部波动突变、结构偏移、非线性振荡等难题，现有Transformer预测模型前馈块依赖平滑静态激活，对工况突变敏感度不足。

### 方法关键点
1. 采用Quantformer风格数值编码器，通过线性嵌入直接处理多变量输入；
2. 设计可学习Lee振荡器激活模块，将预激活映射为动态振荡响应后经时序最大池化聚合，采用8组参数化Lee振荡器软叠加，自适应捕获不同工况下的非线性响应模式；
3. 加入平滑-混沌门控融合机制，自适应平衡常规平滑激活与混沌敏感响应。

### 关键结果
在ETTh1、ETTh2、A股股指基准上全面优于Informer、LogTrans、LSTMa等基线，高波动场景下MSE最高提升43.9%。
