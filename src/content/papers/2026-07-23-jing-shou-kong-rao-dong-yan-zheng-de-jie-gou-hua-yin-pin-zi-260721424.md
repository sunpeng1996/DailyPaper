---
title: An Evaluation Framework for Structured Audio Captions Validated by Controlled
  Perturbations
title_zh: 经受控扰动验证的结构化音频字幕评估框架
authors:
- Liang-Yuan Wu
- Sripathi Sridhar
- Mark Cartwright
- Magdalena Fuentes
affiliations:
- New York University
- New Jersey Institute of Technology
arxiv_id: '2607.21424'
url: https://arxiv.org/abs/2607.21424
pdf_url: https://arxiv.org/pdf/2607.21424
published: '2026-07-23'
collected: '2026-07-24'
category: Eval
direction: 多模态生成评估 · 结构化音频字幕
tags:
- Audio Captioning
- Evaluation Framework
- LLM Judge
- Controlled Perturbation
- Multimodal Evaluation
one_liner: 提出多轴结构化音频字幕评估框架，结合LLM评委与确定性度量，经受控扰动验证可靠性
practical_value: '- 多模态结构化输出（如电商商品结构化文案、短视频结构化描述）评估可复用「LLM语义评估+确定性计算度量」混合范式，兼顾语义柔性与指标刚性

  - 评估框架可靠性验证可引入受控扰动测试方法，向真值注入分级/分类错误，验证指标对好坏样本的区分能力

  - 多属性结构化输出评估可参考正交轴拆分思路，针对不同属性维度设计适配的评估逻辑，避免单一指标的偏差'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
结构化音频字幕（AAC）替代传统单句生成的趋势下，现有评估指标仅针对平文本输出做n-gram匹配，无法可靠评估多模态属性，存在显著评估缺口。
### 方法关键点
1. 基于AudioCards数据集设计5个正交评估轴：标签集、描述文本、逻辑推理、数值度量、频谱轮廓，覆盖语义与声学全维度
2. 采用混合评估范式：用LLM评委捕获语义细粒度差异，搭配确定性计算指标精准度量声学偏差
3. 提出受控扰动验证协议：向真值标注注入不同类型、不同等级的错误，验证框架的评估可靠性
### 关键结果
框架可有效区分语义/声学损坏的样本与保留原意的释义样本，评估区分度远优于传统平文本匹配类指标
