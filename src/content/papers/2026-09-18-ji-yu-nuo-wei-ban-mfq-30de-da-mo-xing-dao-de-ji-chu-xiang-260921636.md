---
title: Steering LLMs Responses Towards Moral Foundations on the Norwegian MFQ-30
title_zh: 基于挪威版MFQ-30的大模型道德基础响应引导研究
authors:
- Hans Andersen
- David Dichas
affiliations:
- University of Oslo
arxiv_id: '2609.21636'
url: https://arxiv.org/abs/2609.21636
pdf_url: https://arxiv.org/pdf/2609.21636
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: 大模型价值对齐 · 道德特征引导
tags:
- LLM Alignment
- Moral Foundations
- Prompt Steering
- Activation Engineering
- Psychometrics
one_liner: 对比prompt与激活层引导方法，验证人口统计学persona可将大模型道德特征与人群相似度提升44%-77%
practical_value: '- 做Agent个性化对齐时，仅用中性人口统计学persona即可大幅提升模型行为与目标人群的匹配度，无需注入人群分布标注数据，降本效果明显

  - LLM做问卷类打分任务（如用户偏好调研、商品满意度预测）时，可直接读取候选答案token的logit加权计算得分，避免生成采样的不稳定性，也不需要约束解码

  - 低资源/小语种场景的LLM应用，可先通过注意力校验筛出能正确理解任务的模型，避免平均得分看似接近人工但实际无任务理解能力的「认知幻影」问题

  - 单对prompt构造的ActAdd泛化性差，若要做可控特征引导优先选择prompt persona方案，简单稳定易落地'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前大模型在企业与消费场景渗透率已超过88%，但其道德价值取向是否与目标地域人群匹配、如何低成本引导模型对齐人群价值，尚缺乏小语种/区域场景的量化验证方案，且现有面向人类设计的心理测量工具在LLM上的有效性也未充分校验。
### 方法关键点
- 数据集：采用经过本地验证的挪威版MFQ-30道德基础问卷，匹配1282名挪威受访者的基准数据作为对齐目标
- 评估设计：加入注意力校验筛除无任务理解能力的模型，采用Mahalanobis d²作为相似度指标（加权人群协方差，比欧氏距离更贴合人类真实分布）
- 对比两种引导方案：①prompt层中性人口统计学persona引导，无任何人群分布标注信息；②激活层ActAdd引导，采用单对对比prompt构造steering vector在模型中层注入
- 打分策略：直接读取1-6分对应token的logit加权计算得分，避免生成解析错误，无需多次采样平均
### 关键结果
6个测试开源大模型中仅3个通过注意力校验，其余3个平均得分接近人类但实际未理解问题，属于典型的「认知幻影」；仅含挪威人口统计学特征的中性persona，可将Gemma 4、Qwen3-14B、Qwen3-8B与挪威人群的相似度分别提升44%、62%、77%，甚至让原本未通过反向量表校验的Qwen3-8B成为稳健通过者；单对prompt构造的ActAdd无法实现单道德维度的精准引导，反而会抹平模型的特征区分度，效果远差于prompt引导。
### 最值得记住的结论
不需要注入任何人群标注数据，仅用描述人口统计学属性的中性persona，即可大幅提升大模型行为与目标人群的匹配度，同时还能缓解模型的任务理解失效问题。
