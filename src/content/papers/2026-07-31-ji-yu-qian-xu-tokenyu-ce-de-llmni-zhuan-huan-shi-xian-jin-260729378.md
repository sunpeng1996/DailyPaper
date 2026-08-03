---
title: 'PTP: Previous-Token Prediction based LLM Inversion for Near-Exact Prompt Reconstruction'
title_zh: 基于前序Token预测的LLM逆转换实现近精确Prompt重构
authors:
- Pirzada Suhail
- Nagasai Saketh Naidu
- Atanu R Sinha
- Amit Sethi
affiliations:
- IIT Bombay
- Adobe Research
arxiv_id: '2607.29378'
url: https://arxiv.org/abs/2607.29378
pdf_url: https://arxiv.org/pdf/2607.29378
published: '2026-07-31'
collected: '2026-08-03'
category: LLM
direction: LLM黑盒逆转换 · Prompt重构
tags:
- LLM Inversion
- Prompt Reconstruction
- Black-box LLM
- Previous-Token Prediction
- Generative Model
one_liner: 黑盒场景下用前序Token预测目标训练逆LLM，无需额外数据与权重访问实现更优Prompt重构
practical_value: '- 黑盒LLM场景下可复用PTP训练思路，无需访问模型权重/Logits即可从输出反推输入Prompt，可用于电商搜索用户Query意图复盘、广告大模型生成效果归因

  - 逆模型训练可完全复用目标LLM生成的合成数据，无需额外标注数据集，可降低业务侧垂直场景Prompt重构任务的数据集构建成本

  - 多样化Prompt采样生成能力可用于生成语义等价的Prompt集合，可用于电商Agent多轮对话意图对齐、推荐系统用户Query改写的语料增强'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM自回归生成的Prompt与响应存在多对多映射，现有Prompt重构方案依赖外部大规模数据集微调，且要求访问模型权重或Logits，无法适配黑盒LLM场景。
### 方法关键点
- 基于Previous-Token Prediction（PTP）训练目标，类比前向Next-Token Prediction逻辑，完全基于目标黑盒LLM生成的合成数据从零训练逆语言模型，建立前向生成与逆向重构的关联
- 支持采样生成多样化重构Prompt，所有生成Prompt输入目标LLM均可得到近似原始响应，无需额外辅助数据、无需访问模型内部信息
### 关键结果
在所有基于Token的Prompt与响应重构评估指标上均优于现有方案，且对不同LLM生成的响应具备跨模型泛化迁移能力
