---
title: 'DeepStress: Stress-Testing Deep Search Agents'
title_zh: DeepStress：面向深度搜索Agent的鲁棒性压力测试框架
authors:
- Ismael Rousseau
- Geraldine Damnati
- Frederic Bechet
affiliations:
- Orange Research
- Aix-Marseille Univ.
- CNRS
- LIS UMR 7020
arxiv_id: '2607.13920'
url: https://arxiv.org/abs/2607.13920
pdf_url: https://arxiv.org/pdf/2607.13920
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: 搜索Agent鲁棒性压力测试框架
tags:
- Search Agent
- Stress Test
- Robustness
- RAG
- Evaluation Metric
one_liner: 通过可控生成三类劣化检索结果，量化评估不同搜索Agent的鲁棒性差异与故障模式
practical_value: '- 做电商导购、商品搜索类Agent上线前的鲁棒性测试时，可复用DeepStress的思路：拦截检索调用，动态生成不同可信度/事实性/相关性的商品信息，不用依赖真实脏数据就能快速定位Agent的故障点，比如会不会把虚假参数的商品推荐给用户

  - 评估面向C端的搜索/推荐Agent性能时，不要只看准确率，可复用RAS和CoPRAS指标：区分"答错""主动弃权""超调用次数"等不同失败模式，对答错的惩罚远高于弃权，更符合业务对安全性的要求，同时CoPRAS可以平衡鲁棒性和推理成本

  - 选型开源搜索Agent时要注意：实验显示多数开源Agent（如Search-R1）对低可信度、非事实的召回内容完全无感知，不会主动弃权，上线前必须额外增加召回内容质量校验、冲突检测的前置模块，避免输出错误信息

  - 构建Agent评测数据集时，必须添加无检索的纯parametric knowledge基线，避免使用HotpotQA这类LLM预训练时已经记忆的数据集，否则评测结果无法反映Agent的真实检索推理能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有搜索Agent的标准评测多基于高质量召回基准，无法复现真实场景中频繁出现的低可信度、不相关、虚假内容等极端检索条件，且仅用最终准确率无法区分"答错""主动弃权""超出工具调用上限"等不同故障模式，导致上线后容易出现误导用户的灾难性错误。

### 方法关键点
- 搭建DeepStress模拟测试环境：拦截Agent的检索工具调用，动态生成可控属性的返回文档，独立调整三个维度的劣化比例：**可信度**（来源URL、样式是否可信）、**相关性**（是否匹配查询意图）、**事实性**（内容是否符合事实）
- 提出RAS（Reliability-Aware Score）指标：正确回答得1分，答错/格式错误得0分，主动弃权/超出工具调用次数在低可靠性场景下按环境可靠度得部分分数，更贴合业务中"宁可不答也不答错"的需求
- 配套CoPRAS（Cost per RAS）指标，将token消耗、工具调用成本纳入计算，衡量单位可靠得分的计算开销，用于平衡性能和成本

### 关键实验结果
测试覆盖HotpotQA、BrowseComp-Plus两个数据集，12款不同架构的搜索Agent（含GPT系列、Search-R1、DR-Tulu等开源/闭源模型），共3.36万条测试轨迹：
- 召回质量从100%降到0%时，平均准确率从0.66降至0.30，而平均RAS仍保持在0.61，说明高鲁棒性Agent会优先选择弃权而非输出错误答案
- 多数开源Agent对可信度劣化几乎无感知，召回可信度降为0%时正确率无明显下降，但错误率大幅上升
- 低推理开销的gpt-5-nano（low）在劣化场景下CoPRAS最优，平衡了鲁棒性和计算成本

### 核心结论
搜索Agent的鲁棒性核心不是干净数据下的准确率，而是在低质量召回下不输出错误答案的能力。
