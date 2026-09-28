---
title: Statistical attribute alignment for black-box generative AI via output post-processing
title_zh: 面向黑盒生成式AI的统计属性对齐输出后处理方法
authors:
- Kevin Jiang
- Morgane Austern
- Edgar Dobriban
- Jason M. Klusowski
arxiv_id: '2609.31607'
url: https://arxiv.org/abs/2609.31607
pdf_url: https://arxiv.org/pdf/2609.31607
published: '2026-09-25'
collected: '2026-09-28'
category: LLM
direction: 生成式AI · 属性对齐后处理
tags:
- Attribute Alignment
- Black-box Generative Model
- Post-processing
- Distribution Alignment
- Generative AI
one_liner: 提出最小化查询量的黑盒生成模型后处理算法，实现输出属性分布与用户指定目标对齐
practical_value: '- 电商生成商品文案/素材场景，可复用该后处理算法对黑盒生成模型的输出做属性校准，无需微调模型即可让生成内容的性别/年龄/地域等属性分布符合业务定向目标，降低合规风险。

  - 生成式推荐场景生成候选item时，可通过该算法控制生成结果的价格/品类等属性分布匹配目标客群消费偏好，同时最小化生成模型调用次数，降低推理成本。

  - Agent生成synthetic persona做推荐冷启动训练数据时，可复用该算法校准生成的用户属性分布与真实目标用户群一致，提升合成数据的可用性。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前生成式AI输出的属性分布难以对齐业务目标，比如公平性要求的敏感属性分布、合成数据的真实分布匹配等；多数场景下仅能黑盒访问生成模型，无法通过微调解决对齐问题，prompt干预的效果也存在局限。
### 方法关键点
针对黑盒生成模型可重复查询的场景，分别设计精确对齐、近似对齐两类后处理算法：在保证输出的属性联合分布尽可能匹配用户指定目标的前提下，最小化对生成模型的预期查询次数，且理论证明了当请求输出量m趋近于无穷时算法的最优性。
### 关键结果
在文生图、地理编码用户persona生成两类任务上验证，该后处理算法的统计属性对齐效果显著优于仅用prompt干预的方案，可作为prompt方法的有效补充。
