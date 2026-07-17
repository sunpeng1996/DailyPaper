---
title: 'Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models'
title_zh: 《分块、提示、聚合：大语言模型的统计自一致性研究》
authors:
- Patrik Wolf
- Thomas Kleine Buening
- Andreas Krause
- Celestine Mendler-Dünner
affiliations:
- Max Planck Institute for Intelligent Systems
- ETH Zürich
- ELLIS Institute Tübingen
- Tübingen AI Center
arxiv_id: '2607.15277'
url: https://arxiv.org/abs/2607.15277
pdf_url: https://arxiv.org/pdf/2607.15277
published: '2026-07-16'
collected: '2026-07-17'
category: Eval
direction: 大语言模型 · 统计自一致性评估
tags:
- LLM
- Self-Consistency
- In-Context Learning
- Persona Prompting
- Probabilistic Inference
one_liner: 发现LLM宏观谬误现象，提出无参考标注的LLM统计自一致性评估框架
practical_value: '- 做电商消费者偏好调研、消费趋势预测、人群画像统计类任务时，避免直接向LLM询问整体人群的估计值，可按年龄、地域、消费层级等属性拆分为互斥子群分别查询，再结合子群占比加权聚合，能显著提升估计准确率

  - 不想做复杂拆分时可直接用micro-to-macro prompt技巧：在查询整体统计量前，要求LLM先思考相关子群的特征再输出结论，几乎无额外开销就能降低10%~30%的估计误差，适合大促销售额预测、广告受众偏好预估等场景

  - 做基于LLM的消费者行为仿真、Agent市场模拟时，可复用论文提出的split consistency、order consistency无标注检查逻辑，无需真实标注数据就能提前校验LLM输出的统计结果可靠性，降低仿真偏差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前大量应用将LLM的In-context Learning视作条件推断工具，比如用Persona Prompting模拟人群行为、预测群体统计指标，但长期缺乏对LLM输出是否符合基础概率公理的验证，直接进行整体群体估计的偏差问题未被系统性研究，且缺乏无参考标注的LLM推理可靠性校验方法。

### 方法关键点
- 提出二进制条件树（BCT）框架：递归将目标群体拆分为互斥的细粒度子群，将子群属性转为自然语言prompt分别查询LLM，获取子群目标指标估计和子群占比先验，再通过全概率公式聚合得到整体估计
- 定义两个无参考自一致性评估指标：split consistency（校验父节点直接估计与子节点聚合估计的偏差）、order consistency（校验子群属性描述顺序对估计结果的影响）
- 提出两种优化方案：显式BCT拆分聚合，以及轻量的micro-to-macro提示（引导LLM先思考相关子群特征再输出整体结论）

### 关键结果
实验基于2024美国ACS人口普查数据、全球价值观调查WVS数据，覆盖GPT-5、Claude、Qwen等10+前沿LLM：
1. 细粒度子群聚合的估计结果比直接整体prompt的准确率平均高20%~50%，即宏观谬误现象，跨任务、跨模型普遍存在
2. micro-to-macro提示平均降低10%~30%的估计误差，无需额外拆分步骤
3. 前沿LLM的split consistency通过率普遍低于40%，且自一致性得分与模型通用能力得分无正相关，属于未饱和的优化维度

### 核心结论
LLM掌握的细粒度子群知识比整体知识更可靠，做群体统计估计时，拆分子群再聚合的效果永远优于直接提问
