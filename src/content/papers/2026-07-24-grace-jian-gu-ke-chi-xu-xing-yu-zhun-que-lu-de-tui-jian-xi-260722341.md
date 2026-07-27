---
title: 'Bringing GRACE to Recommendation: Fine-Tuning for Sustainable and Accurate
  Personalization'
title_zh: GRACE：兼顾可持续性与准确率的推荐系统微调框架
authors:
- Yibowen Zhao
- Yinan Zhang
- Ning Liu
- Lizhen Cui
- Chunyan Miao
affiliations:
- 山东大学
- 南洋理工大学
- 山东大学-南洋理工大学联合人工智能研究中心
- 阿里巴巴-南洋理工大学全球电子可持续性联合实验室
arxiv_id: '2607.22341'
url: https://arxiv.org/abs/2607.22341
pdf_url: https://arxiv.org/pdf/2607.22341
published: '2026-07-24'
collected: '2026-07-27'
category: RecSys
direction: 绿色推荐 · 多目标微调
tags:
- Green Recommendation
- Multi-objective Optimization
- Fine-tuning
- Differentiable Relaxation
- Gradient Projection
one_liner: 基于可微绿色损失与梯度投影的微调框架，无需重训练或推理重排实现绿色推荐
practical_value: '- 可复用梯度投影的多目标平衡方案：新增业务侧（如绿色、合规、健康）优化目标时，将新增目标的梯度投影到原主目标梯度的正交空间，控制新增目标更新幅度不超过主目标的α比例，避免主指标大幅下降

  - 离散非可分指标优化trick：对于top-K维度的离散业务指标（如绿色得分、合规率），可采用Gumbel-softmax的可微松弛方案构造损失，替代pairwise弱监督，实现端到端优化

  - 无推理 overhead 的多目标优化架构：所有新增目标融合在微调阶段完成，推理阶段和原模型完全一致，无额外重排延迟，适合低延迟要求的大规模电商推荐场景

  - 超参数可调的业务平衡方案：通过projection ratio参数可直接调节新增目标与主目标的trade-off，支持业务动态调整优先级'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
全球对环境可持续性与公共健康的关注推动绿色推荐发展，但现有方案存在明显缺陷：全量重训类方法计算成本高、碳排放大，重排类方法会增加推理延迟，且离散非可微的绿色标签难以直接融入梯度优化，多目标冲突易导致推荐准确率大幅下降，亟需低成本、无推理额外开销的优化方案。
### 方法关键点
- 构造可微绿色损失：基于Gumbel-softmax松弛实现离散top-K绿色指标的连续近似，替代传统pairwise弱监督，支持绿色目标的端到端梯度优化
- 梯度投影冲突缓解：将绿色目标梯度投影到原推荐准确率梯度的正交空间，同时限制绿色梯度的更新幅度不超过主梯度的α比例，最小化对用户偏好学习的干扰
- 全流程仅微调原有预训练推荐模型，推理链路与原模型完全一致，无额外计算开销
### 关键结果
在GreenRec、RecipeEmission两个真实食品推荐数据集上，对比FHFRS、CFARS等重排基线与GradNorm、MGDA等多目标微调方案：GRACE适配SASRec、FDSA等4类主流推荐backbone，平均提升健康/环保指标5%~27%，推荐准确率最高提升18%，90%以上场景准确率损失小于2%，推理延迟与原模型完全一致。
> 最值得记住：新增业务目标优化无需改动推理链路或全量重训，可微松弛+梯度投影的微调方案即可实现多目标平衡且无推理 overhead
