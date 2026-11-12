---
title: Causal Concept Explanations for Deep Neural Models
title_zh: 面向深度神经网络的因果概念可解释性方法
authors:
- Josh Rountree
- Pulkit Verma
- Oswin So
- Chuchu Fan
- Julie A. Shah
affiliations:
- MIT Computer Science and Artificial Intelligence Laboratory
- Indian Institute of Technology Madras
- MIT Laboratory for Information and Decision Systems
arxiv_id: '2611.14407'
url: https://arxiv.org/abs/2611.14407
pdf_url: https://arxiv.org/pdf/2611.14407
published: '2026-11-10'
collected: '2026-11-12'
category: Other
direction: 神经网络因果可解释性框架
tags:
- Causal_Interpretability
- Mediation_Analysis
- Concept_Explanation
- Causal_Alignment
- Model_Transparency
one_liner: 提出CCW-Net框架，首次将干预中介分析作为训练目标实现可量化的因果级模型概念解释
practical_value: '- 推荐系统特征归因场景可复用中介分析框架，量化不同用户、物品、上下文特征对点击预测、排序结果的因果贡献，避免相关性解释误导特征迭代

  - 电商高风险决策场景（如营销预算分配、智能客服应答）可引入必要性、充分性、独立性三个因果对齐准则，优化Agent决策模块的概念表示，提升决策可信度

  - 针对现有黑盒推荐/LLM推理接口，可复用文中评估方法，快速量化各输入概念对输出结果的因果影响，无需修改原有模型架构'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有神经网络概念解释多为相关性结论，无法验证解释对输出的必要性与充分性，易产生误导，无法支撑高风险场景的模型认证与落地。
### 方法关键点
1. 提出CCW-Net框架，首次将经济学、医学领域的干预中介分析作为训练目标，对齐概念解释与模型输出的因果关系
2. 基于反事实概念表示，设置三类因果对齐准则：必要性驱动无关概念影响归0，充分性确保相关概念可完整重构模型输出，独立性保证各概念贡献线性可分解
3. 同时将中介分析作为通用评估工具，可量化任意模型输出中各概念的因果贡献占比，无需修改原模型结构
### 关键结果
在飞行器控制、自动驾驶、图像分类三类高风险任务上验证有效性，实现兼具可解释性与量化因果属性的模型解释能力，可直接支撑高可靠AI系统的评估、认证与部署
