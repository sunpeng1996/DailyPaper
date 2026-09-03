---
title: 'From Tokens to Semantics: Leveraging Complementary Signals for Hallucination
  Detection in Black-Box LLMs'
title_zh: 基于Token与语义互补信号的黑盒大模型幻觉检测方法
authors:
- Urja Pawar
- Rajitha Ramanayake
- Owen O'Neill
- Nabeel Kemal
- Abhishek Mandal
- Houssem Chatbri
- Christopher Martin
affiliations:
- BNY
arxiv_id: '2609.02679'
url: https://arxiv.org/abs/2609.02679
pdf_url: https://arxiv.org/pdf/2609.02679
published: '2026-09-02'
collected: '2026-09-03'
category: LLM
direction: 黑盒LLM · 幻觉检测
tags:
- Hallucination Detection
- Black-box LLM
- Semantic Entropy
- Token Uncertainty
- Supervised Learning
- Unsupervised Learning
one_liner: 结合语义熵与token概率互补信号，提出多套无需参考上下文的黑盒LLM幻觉检测方案
practical_value: '- 做Agent生成内容（商品文案、智能客服回复）的幻觉校验时，无标注场景可先用TopK或CoCoA方案，仅调用黑盒LLM的采样输出和token
  log-prob即可实现，无需额外模型权重

  - 若有业务场景的幻觉标注数据，优先用Stacked融合语义聚类特征与多响应聚合token特征，能稳定接近最优检测效果，比单信号方案AUROC平均高0.05以上

  - 采样参数优先设置N=10个响应，temperature按场景调整：多跳推理类任务调高temperature增加语义分歧，歧义类任务调低temperature减少无效波动

  - 电商商品信息抽取、交易问答等高准确率要求场景，可设定1%-3%的低FPR预算，此时TopK/Stacked方案的召回率比纯语义熵方案高20%以上'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM落地高风险场景（如电商交易问答、金融合规审核、智能客服回复）时，幻觉漏检会造成用户权益损失与合规风险，误检又会挤占有限的人工审核资源；现有幻觉检测方案大多需要可信参考上下文或白盒访问模型内部状态，无法适配黑盒API调用的生产场景，且语义熵、token概率两类常用信号存在互补失效模式：语义熵在所有响应属于同一语义簇时失效，token置信度会漏判模型持续高置信生成的错误，亟需融合方案。
### 方法关键点
- 无监督方案：TopK聚合多采样响应的平均top-k熵与跨响应置信度方差；CoCoA融合目标响应置信度与采样响应的语义差异，仅需阈值校准无需标注
- 有监督方案：Gated级联路由，多语义簇时输出语义熵得分，单语义簇时调用聚合token特征的分类器；Stacked直接拼接语义特征、聚类数与多响应聚合token特征，经PCA降维后用L2正则逻辑回归输出幻觉概率
- 所有方案仅依赖黑盒API返回的生成文本、token log-prob，无需参考上下文或模型内部权重
### 关键实验
覆盖7个基准数据集（含2个自定义金融数据集，跨文本QA、多模态信息抽取等场景）、4个主流LLM，对比13种基线方法；Stacked在近一半场景下取得最优AUROC，26组对比中20组AUROC与最优值差距≤0.05；无标注场景下TopK、CoCoA性能接近有监督方案；1%-3%低FPR预算下，token类/融合方案比纯语义熵方案召回率高15%-25%。
### 核心结论
没有通用最优的幻觉检测方案，需结合业务标注资源、FPR预算、任务类型联合选择检测方法、采样参数与判定阈值。
