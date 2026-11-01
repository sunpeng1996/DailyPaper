---
title: 'Rural Readiness: Domain Generalization with Adversarially Chosen Domains'
title_zh: 对抗选择域下的领域泛化：低资源乡村场景模型适配研究
authors:
- Cynthia Dwork
- Andisheh Ghasemi
- Lunjia Hu
affiliations:
- Harvard University
- Northeastern University
arxiv_id: '2610.40468'
url: https://arxiv.org/abs/2610.40468
pdf_url: https://arxiv.org/pdf/2610.40468
published: '2026-10-29'
collected: '2026-11-01'
category: Training
direction: 领域泛化 · 训练样本复杂度优化
tags:
- Domain_Generalization
- Sample_Complexity
- Adversarial_Training
- VC_Dimension
- Transfer_Learning
one_liner: 推导对抗选择域泛化的样本复杂度边界，放松学习目标后样本需求从Ω(dk)降至O(d)
practical_value: '- 做跨域推荐（如一二线用户模型迁下沉/乡村用户场景）时，可适度放松对100%源域效果的约束，只需保证模型在绝大多数源域表现达标，即可大幅降低训练所需样本量，同时保障未知目标域泛化效果

  - 跨域模型训练时，若目标域只能拿到少量标注样本，无需浪费资源做额外的目标域小样本微调，其对最坏场景下的源域样本复杂度无优化作用

  - 计算跨域模型的样本需求时，可参考本文给出的基于VC维的复杂度边界，快速估算所需训练数据量，减少数据采集成本'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
数据充足源域训练的预测模型，迁移到数据匮乏的未知目标域（如城市医院模型迁乡村医疗场景）时性能骤降，现有领域泛化方法对对抗选择的未知域的泛化能力、样本复杂度边界缺乏明确理论支撑。
### 方法关键点
1. 提出对抗选择域下的领域泛化问题设定，要求学习器在任意未知目标域的表现，与符合源域证据的最差假设表现接近
2. 仅假设假设类存在对k个源域都低误差的通用预测器，基于VC维推导该目标的样本复杂度边界
### 关键结果
- 原严格目标的样本复杂度下界为Ω(dk)，d为假设类VC维，k为源域数量
- 放松目标为允许模型与99%源域表现优秀的假设竞争时，样本复杂度大幅降至O(d)（仅含对数因子误差）
- 少量目标域标注样本无法优化源域的最坏情况样本复杂度
