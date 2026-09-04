---
title: 'The Geometry of Ignorance: LLMs Know When to Temper Bayesian Priors'
title_zh: 《无知的几何：大语言模型可自主调节贝叶斯先验权重》
authors:
- Toni J. B. Liu
- Jiajun Bao
- Yizhou Liu
- Gurbir Arora
- Nicolas Boullé
- Raphaël Sarfati
- Christopher J. Earls
affiliations:
- Cornell University
- MIT
- Imperial College London
- Goodfire AI
arxiv_id: '2609.02959'
url: https://arxiv.org/abs/2609.02959
pdf_url: https://arxiv.org/pdf/2609.02959
published: '2026-09-02'
collected: '2026-09-04'
category: LLM
direction: LLM可解释性 · 先验调控机制
tags:
- LLM Interpretability
- Unembedding Geometry
- Bayesian Prior
- Tempered Inference
- Model Steering
one_liner: 发现LLM的unembedding中存在编码unigram分布的「无知方向」，可定量衡量和干预模型对先验的依赖
practical_value: '- 电商/广告文案生成场景可通过干预无知方向的λ值调控生成效果：降低λ抑制高频无意义token提升多样性，提高λ生成符合用户习惯的通用话术

  - RAG/Agent系统可将λ作为hallucination预警信号：λ突增说明上下文信息不足，模型正 fallback 到语料先验，此时触发补充召回或拒绝生成

  - 垂直领域小模型预训练时，可跟踪无知方向的归一化KL指标判断训练进度：KL降至低位说明模型已习得领域unigram分布，可转向高阶语义训练'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
LLM在上下文信息不足时会默认依赖训练语料的unigram先验，但此前该行为的底层机制不明确，也缺乏可跨模型比较的定量指标衡量先验依赖程度，难以针对性干预生成效果。

### 方法关键点
- 通过线性最小二乘拟合unembedding矩阵与语料unigram分布的对数概率，可唯一识别编码先验的「无知方向」$d_{prior}$，无需任何模型前向传播
- 将最终预测隐态投影到$d_{prior}$得到先验加载因子$\lambda$，证明预测分布可正交分解为$\lambda$次幂的unigram先验与上下文驱动似然的乘积，完全对应调温贝叶斯更新
- 可直接修改预测隐态在$d_{prior}$方向的分量干预$\lambda$，精准调控模型对先验的依赖程度

### 关键实验结果
在Llama、Qwen、Gemma、Pythia四个系列0.4B~405B模型上验证：训练后$d_{prior}$的归一化KL（均匀分布基线为1）普遍低于0.2，可高精度还原unigram分布；$\lambda$随上下文信息量增长而下降，上下文充分时70B以上模型$\lambda$可降至0以下，自动抑制高频token；干预$\lambda$每提升1，预测分布与unigram的KL散度下降约2nats，随机方向干预无显著效果。

最值得记住的结论：LLM对语料先验的依赖完全由unembedding空间的单个方向控制，无需复杂探针即可定量读取和干预。
