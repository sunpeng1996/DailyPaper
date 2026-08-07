---
title: Consistency-Driven Co-Evolution for Self-Supervised Cross-Representation Learning
title_zh: 面向自监督跨表征学习的一致性驱动协同演化方法
authors:
- Xuehang Guo
- Pengyuan Li
- Tom Hope
- Tirthankar Ghosal
- Manling Li
- Qingyun Wang
affiliations:
- William & Mary
- IBM
- Allen Institute for AI
- Oak Ridge National Laboratory
- Northwestern University
arxiv_id: '2608.04926'
url: https://arxiv.org/abs/2608.04926
pdf_url: https://arxiv.org/pdf/2608.04926
published: '2026-08-04'
collected: '2026-08-07'
category: Multimodal
direction: 多模态跨表征自监督学习
tags:
- Cross-Representation Learning
- Self-Supervised Learning
- Multimodal Learning
- Consistency Optimization
- Test-Time Adaptation
one_liner: 提出无标注的跨图表、表格、代码表征一致性协同演化框架，覆盖训练、推理与评估全流程
practical_value: '- 电商多模态商品表征对齐可复用环式一致性约束：商品图、属性表、详情文案的跨模态对齐无需额外标注，通过三类表征环上的一致性损失即可完成自监督训练，降低标注成本

  - 测试时一致性优化trick可直接落地：针对推荐/搜索场景新样本的跨模态表征漂移问题，可引入轻量一致性目标做推理时微调，无需重训全模型即可提升跨模态召回准确率

  - 多模态任务评估体系可参考：做多模态推荐、商品理解的跨任务效果验证时，可设计覆盖全双向映射任务的评估集，更全面衡量模型的泛化能力'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
跨图表图像、结构化表格、可视化代码三类表征的理解任务存在固有一对多映射问题，标注成本高且模糊，现有模型优化缺乏方向自适应、跨表征泛化的通用优化信号，难以适配多任务需求。
### 方法关键点
1. 打破跨表征映射一对多假设，定义显式一对一对应关系，基于多模态表征一致性做无监督优化，无需额外标注；
2. 训练阶段CoCoEvolve@Train在图表-表格-代码环上执行协同演化，对齐三类表征分布；
3. 推理阶段CoCoEvolve@Test复用相同一致性目标做测试时协同优化，适配分布外新样本；
4. 配套CoCoEvolve@Eval评估套件覆盖全部6类跨表征双向映射任务。
### 关键结果
在4个公开基准数据集上，训练、推理两阶段优化均实现稳定性能提升，覆盖全部6类跨表征任务。
