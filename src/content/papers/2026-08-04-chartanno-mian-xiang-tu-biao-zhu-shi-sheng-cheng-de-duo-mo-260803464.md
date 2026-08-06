---
title: 'ChartAnno: Evaluating MLLMs for Chart Annotation Generation'
title_zh: ChartAnno：面向图表注释生成的多模态大语言模型评测基准
authors:
- Zhenghan Chen
- Zekai Shao
- Lidan Tan
- Xin Lin
- Xingchen Zeng
- Yi Shan
- Ziyue Lin
- Xiaoliang Fu
- Xinyuan Liu
- Yuetong Guo
affiliations:
- Fudan University
- Yonsei University
- Sun Yat-sen University
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2608.03464'
url: https://arxiv.org/abs/2608.03464
pdf_url: https://arxiv.org/pdf/2608.03464
published: '2026-08-04'
collected: '2026-08-06'
category: Eval
direction: 多模态大模型评测 · 图表注释生成
tags:
- MLLM
- Benchmark
- Chart Annotation
- Evaluation
- Multimodal
one_liner: 构建含1200个真实图表的ChartAnno基准，评测不同输入下10款MLLM的图表注释生成能力
practical_value: '- 做电商运营类图表自动标注（如销量、流量趋势图注释文案生成）时，优先给MLLM输入图表代码而非仅图像，可降低推理成本同时保证核心标注质量

  - 广告素材自动标注、数据报表自动解读等多模态生成场景，给模型更明确的指令可显著提升输出质量，抽象意图推理类任务需额外做prompt调优或小样本微调

  - 多模态任务选型时，大参数开源MLLM可覆盖大部分需求，仅对设计类细节要求高的场景再考虑补充图像输入或使用闭源模型'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有MLLM在图表理解、生成、编辑领域进展显著，但图表注释生成能力缺乏系统评测；该任务需推理用户意图、解析图表语义、匹配适配的标注元素，实用价值高但研究空白大。
### 方法关键点
构建ChartAnno评测基准，包含1200个真实世界图表，配套对应代码、三级明确度的标注指令；测试10款代表性MLLM，覆盖仅图表代码、代码+图像、仅图像三类输入设置，从语义匹配、设计合理性等多维度评估效果。
### 关键结果
闭源MLLM整体表现最优，大参数开源模型已缩小差距；指令明确度越高注释质量越好，抽象意图推理仍是当前模型最大短板；额外输入图表图像对整体效果提升有限，仅对设计相关指标有明显增益。
