---
title: Improving Semantic Coverage in AI Test & Evaluation through Generative Augmentation
title_zh: 通过生成式增强提升AI测试评估的语义覆盖度
authors:
- Connor Hashemi
- Bharadwaj Ravichandran
- Connor Anderson
- Shitij Govil
- Brandon RichardWebster
- Brian Hu
- Keith Fieldhouse
affiliations:
- Kitware Inc
arxiv_id: '2610.13697'
url: https://arxiv.org/abs/2610.13697
pdf_url: https://arxiv.org/pdf/2610.13697
published: '2026-10-09'
collected: '2026-10-13'
category: Eval
direction: AI模型评测 · 生成式数据增强
tags:
- diffusion models
- test and evaluation
- data augmentation
- VLM
- semantic coverage
one_liner: 提出无需语义标注的三阶段生成式增强pipeline，填补AI测试集语义缺口，提升评测可靠性
practical_value: '- 可复用三阶段语义缺口识别+增强流程，补全搜索/推荐评测集的冷门语义场景（如大促、小众用户需求场景），无需修改训练数据即可更准确评估模型鲁棒性

  - VLM零样本标注语义因子+embedding聚类定位核心影响语义的方法，可直接迁移至多模态推荐bad case归因，无需人工打标即可快速定位模型失效的语义场景

  - 扩散模型保内容换语义属性的增强思路，可用于生成电商多模态素材的多样性测试用例，评估多模态召回/排序模型的跨场景泛化性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
AI模型测试评估（T&E）通常仅能访问预留测试集，无法获知训练数据语义构成，若测试集存在语义覆盖缺口（如缺失昼夜、天气等关键场景），会导致评估结果严重失真。
### 方法关键点
提出无标注三阶段生成式增强pipeline：
1. 用VLM做零样本语义因子标注，结合embedding空间聚类定位对下游模型行为影响最大的语义缺口；
2. 基于扩散的图生图模型保留场景核心内容，将已覆盖样本转换到缺失语义域生成增强样本；
3. 对增强样本embedding做统计校验，确认覆盖度提升后再纳入测试集，全程无需重训待评测模型。
### 关键结果
在昼夜语义缺口场景的图像分类、目标检测任务验证，增强后测试集可更准确区分是否接触过缺失语义的模型，评估结论与理想全量覆盖测试集的匹配度显著提升。
