---
title: 'StARS: Socially Appropriate Robot Actions via a Recommender System-Driven
  Approach'
title_zh: StARS：基于推荐系统驱动的社交适配机器人动作生成方法
authors:
- Erencem Ozbey
- Fethiye Irmak Dogan
- Jin Huang
- Hatice Gunes
affiliations:
- Bogazici University
- University of Cambridge
arxiv_id: '2607.21802'
url: https://arxiv.org/abs/2607.21802
pdf_url: https://arxiv.org/pdf/2607.21802
published: '2026-07-23'
collected: '2026-07-27'
category: Agent
direction: Agent 个性化动作生成优化
tags:
- Collaborative Filtering
- Personalized Preference
- Scene Representation
- HRI
- Model Agnostic
one_liner: 融合协同过滤与可学习场景表征，生成适配用户个性化偏好的社交合规机器人动作
practical_value: '- 个性化多模态场景下的偏好建模可复用「用户-场景-待评分候选」三元组范式，将个性化匹配问题转化为推荐排序问题，降低建模复杂度

  - 模型无关的协同过滤+场景表征融合架构可迁移到个性化文案/素材推荐场景，无需改动原有图像/文本编码器即可快速实现个性化适配

  - 稀疏反馈下的鲁棒性优化思路可复用在冷启动用户推荐场景，缓解少样本下的偏好估计偏差'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
人机交互（HRI）场景中社交适宜性存在显著个体差异，相同场景下的同一机器人动作会被不同用户给出完全相反的评价，传统方法无法适配个性化偏好，建模成本高。
### 方法关键点
将社交适宜动作生成问题转化为推荐系统偏好建模任务：把标注用户对应推荐范式中的user、场景/上下文对应item、候选动作的适宜性评分对应预测目标；提出StARS模型无关框架，融合协同过滤与可学习场景表征，可对接任意场景编码器与底座模型，无需重构底层即可实现个性化适配。
### 关键结果
在MannersDB+、SocNav1两个公开数据集验证，适配不同底座模型时均稳定提升性能，与人工标注的一致性显著优于基线，在稀疏偏好反馈下仍保持优秀鲁棒性。
