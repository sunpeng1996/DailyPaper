---
title: A Human-Centered Validation of the Explainability-Performance Coefficient
title_zh: 可解释性-性能系数的人中心验证研究
authors:
- Christian Oliva
- Luis F. Lago-Fernández
affiliations:
- Universidad Autónoma de Madrid, Spain
arxiv_id: '2607.29614'
url: https://arxiv.org/abs/2607.29614
pdf_url: https://arxiv.org/pdf/2607.29614
published: '2026-07-31'
collected: '2026-08-03'
category: Eval
direction: XAI可解释性 · 人因对齐评估指标
tags:
- XAI
- Explainability Evaluation
- Human-Centered AI
- Model Agnostic
- EPC Score
one_liner: 提出模型无关的EPC评分，平衡特征稀疏性与模型性能，实现对齐人类认知的XAI质量评估
practical_value: '- 推荐/广告排序模型的可解释性评估可直接复用EPC score，平衡特征重要性的稀疏性与排序效果，避免解释冗余或失真

  - 面向C端的推荐理由生成场景，可使用EPC score作为离线评估指标，对齐用户对推荐理由的认知接受度，降低AB测试成本

  - 监管要求高的电商信贷/营销推荐场景，可基于EPC score筛选合规XAI方法，满足监管对决策可解释性的要求'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
深度学习在高风险领域快速落地，现有XAI评估存在两大核心痛点：难以客观量化解释保真度，现有指标与人类认知对齐度不足，可解释性与性能的权衡缺乏统一量化标准
### 方法关键点
模型无关的EPC score通过显式平衡特征选择稀疏性与保留的模型性能，量化解释质量，支持表格、文本、图像多模态场景的XAI评估
### 关键结果
跨多模态实验验证EPC score可有效揭示网络激活、数据维度与解释器性能的关联；人因验证显示高EPC得分与人类词汇情感判断、空间视觉标注高度对齐，可替代部分人工评估环节
