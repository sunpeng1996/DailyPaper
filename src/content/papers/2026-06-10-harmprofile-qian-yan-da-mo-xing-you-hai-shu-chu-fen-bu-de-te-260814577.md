---
title: 'HarmProfile: Characterizing Harmful Distributions in Frontier LLMs'
title_zh: 《HarmProfile：前沿大模型有害输出分布的特征刻画》
authors:
- Zhouyuan Ma
- Yutao Wu
- Hanxun Huang
- Xiang Zheng
- Xiao Liu
- Yixin Cao
- Zuxuan Wu
- Xingjun Ma
- Yu-Gang Jiang
affiliations:
- Fudan University
- Deakin University
- The University of Melbourne
- City University of Hong Kong
arxiv_id: '2608.14577'
url: https://arxiv.org/abs/2608.14577
pdf_url: https://arxiv.org/pdf/2608.14577
published: '2026-06-10'
collected: '2026-08-18'
category: Eval
direction: 大模型安全评估 · 风险画像构建
tags:
- LLM Safety
- Benchmark Dataset
- Risk Profiling
- Alignment Evaluation
- Harmful Generation
one_liner: 构建含8万+验证样本的多模型有害输出基准，量化前沿LLM的安全风险分布特征
practical_value: '- 搭建LLM驱动的电商导购/客服/内容生成Agent时，可直接复用HarmProfile的15类有害标签体系，快速搭建输出内容安全检测规则，降低业务违规风险

  - 微调业务场景专用LLM时，可引入该数据集的有害样本作为对齐训练负例，针对性提升模型的安全防御能力

  - 评估业务侧LLM的安全水平时，可参考该数据集的风险分布量化方法，无需从零设计评测维度，快速构建自有模型的安全画像'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有前沿LLM安全评估仅将有害生成作为攻击结果而非分析对象，缺乏大规模高质量的前沿模型不良行为样本集，无法系统刻画模型安全风险的分布特征。
### 方法关键点
构建内容导向的基准数据集HarmProfile，覆盖13个模型家族的23款前沿LLM，将有害输出划分为15个大类、57个子类，基于有害输出的内容、严重程度、分布差异定义模型级风险画像。
### 关键结果数字
- 包含80000+经过验证的有害样本
- 不同前沿LLM的有害输出风险画像差异显著
- 模型能力越强，有害输出的危害性与多样性越高，表面完成对齐的模型仍隐含大量未被拦截的危险知识
