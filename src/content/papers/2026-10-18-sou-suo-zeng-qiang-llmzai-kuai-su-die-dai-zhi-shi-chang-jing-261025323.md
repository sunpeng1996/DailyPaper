---
title: Where and Why Search-Augmented LLMs Fail When Reasoning over Rapidly Evolving
  Knowledge
title_zh: 搜索增强LLM在快速迭代知识场景下的推理失败归因分析
authors:
- Tianyi Hu
- Bhavyajeet Singh
- Niket Tandon
- Akhil Arora
affiliations:
- Aarhus University
- Microsoft Research
- Technische Universität Darmstadt
arxiv_id: '2610.25323'
url: https://arxiv.org/abs/2610.25323
pdf_url: https://arxiv.org/pdf/2610.25323
published: '2026-10-18'
collected: '2026-10-20'
category: RAG
direction: RAG 动态知识推理故障归因
tags:
- RAG
- Failure Attribution
- Temporal Reasoning
- Benchmark
- Knowledge Conflict
one_liner: 提出TREK归因与基准套件，明确搜索增强LLM处理动态知识的核心瓶颈为后检索推理
practical_value: '- 排查电商实时RAG（如活动规则、价格、库存问答）的线上错误时，可复用TREKTRACE的归因逻辑：先校验是否召回了正确证据，再给模型仅喂正确证据重跑，就能快速定位错误来自查询生成、检索还是后推理阶段，无需额外标注。

  - 优化实时性RAG系统时无需过度投入召回侧，重点优化后检索阶段的冲突解决逻辑：针对电商场景常见的新旧活动规则、同款不同参数/价格的冲突，增加时效性、查询约束匹配度、来源可信度的显式校验，比单纯提升召回准确率收益更高。

  - 做RAG的离线压测时，不要仅使用过时干扰项，需补充相关性干扰（如同品类不同规格的参数）、低可信度干扰（如第三方错误评价），才能避免离线指标虚高、线上效果不达预期。

  - 现有基于语义+时效分数的重排方法抗干扰性差，可替换为过滤式RAG：先让模型显式判断每个召回片段是否符合查询约束、是否可信，再生成答案，对复杂干扰的抵抗能力提升明显。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有搜索增强LLM（RAG）处理实时变化知识（如赛事结果、商品价格、活动规则）时，错误评估完全是黑盒，仅能得到最终准确率无法定位错误根因；且现有测试基准大多仅包含过时干扰项，模型靠「选最新内容」的捷径就能拿到虚高分数，无法反映真实场景下多源冲突信息的复杂度。

### 方法关键点
- 推出TREK全链路诊断套件：① TREKTRACE归因框架：无需额外标注或重训练，先通过检索测试判断错误属于预检索（查询构造错误）、检索（未召回正确证据）阶段，再通过反事实重跑判断后检索错误属于证据解读错误还是干扰项误导；② TREKBENCH-WILD真实场景基准：聚合3个公开数据集的144道动态知识多跳推理题；③ TREKBENCH-CTRL受控干扰基准：覆盖时效性、相关性、可信度三类干扰项，设置4档难度梯度。

### 关键结果数字
- 测试10+款从8B到235B的开源/闭源模型，GPT-5.4搭配原生搜索的最高准确率仅为70.1%；
- 顶尖模型的错误中88%以上来自后检索阶段，干扰项误导是首要原因；
- 仅过时干扰项场景下，GPT-5.4-mini准确率比纯黄金证据低6.3pp，换成无源性提示的对抗干扰后，准确率下降达36.8pp，现有基准至少低估4倍真实难度。

### 最值得记住的一句话
当前搜索增强LLM处理动态知识的核心瓶颈已经不是检索，而是后检索阶段对多源冲突证据的抗干扰推理能力。
