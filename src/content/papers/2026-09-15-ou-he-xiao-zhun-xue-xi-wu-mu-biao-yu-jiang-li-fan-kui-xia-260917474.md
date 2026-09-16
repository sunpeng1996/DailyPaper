---
title: 'Coupled Calibration and Learning: Mitigating Teacher Bias in LLM Distillation
  without Target-Domain Reward Feedback'
title_zh: 耦合校准学习：无目标域奖励反馈下缓解LLM蒸馏教师偏差
authors:
- Haichen Hu
- Yuheng Zhang
- David Simchi-Levi
affiliations:
- MIT
- UIUC
arxiv_id: '2609.17474'
url: https://arxiv.org/abs/2609.17474
pdf_url: https://arxiv.org/pdf/2609.17474
published: '2026-09-15'
collected: '2026-09-16'
category: Training
direction: LLM蒸馏 · 无目标域反馈训练优化
tags:
- Knowledge Distillation
- LLM Training
- Covariate Shift
- Teacher Bias
- Offline Distillation
one_liner: 仅依赖源域奖励的CCL蒸馏算法，可收敛到最优学生，规避教师偏差传播
practical_value: '- 电商/推荐场景下做垂类小模型蒸馏（比如商品文案生成、推荐理由生成小模型）时，若目标垂类无足够人工标注/奖励反馈，可套用CCL框架，仅用已有的通用域标注校准大教师后再蒸馏，避免大模型在垂类的偏差被小模型继承

  - 蒸馏时可复用token级分支校准trick：在token生成节点采样当前学生的替代输出与教师输出对比，仅用源域奖励即可获取校准信号，无需全量标注目标域数据，大幅降低标注成本

  - 小模型迭代优化阶段可借鉴「梯度候选+随机候选」的无监督选择机制，仅用目标域无标注数据即可筛选更优的学生模型，无需额外标注成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM 蒸馏通过大教师模型监督训练小模型可大幅降低部署成本，但直接模仿教师会同步传播其系统偏差，尤其当目标域与源域存在协变量偏移、且目标域无可靠奖励反馈时，常规蒸馏方法会残留持久的教师偏差，无法得到性能最优的小模型。
### 方法关键点
- 耦合校准与学习（CCL）迭代框架采用双向耦合设计：每轮先基于源域奖励反馈校准教师，再用校准后的教师在无标注目标域数据上训练学生，更新后的学生反向指导下一轮教师校准
- 核心采用token级分支校准机制：在源域样本生成过程中选取某一token位置，对比教师输出与当前学生的替代输出，结合参考策略完成分支生成后，用源域奖励更新教师校准参数
- 学生更新阶段每次生成梯度更新、随机采样两个候选，用目标域rollout的学生与校准教师的KL散度做无监督选择，全程无需目标域奖励反馈
### 关键结果
- 理论证明CCL输出的学生与最优Oracle学生的期望平均KL散度随迭代次数呈多项式速率收敛到0
- 分离性分析表明：正则化直接蒸馏方法即使教师性能优于所有学生策略，当迭代次数足够大时，最终学生与Oracle的KL散度仍有不低于$κ_{SM}(1-α)^2/(128λ^2)$的正下界，偏差无法消除
### 核心结论
无目标域奖励反馈的LLM蒸馏不必承受持久的教师偏差损失，通过耦合校准与学习即可在有限迭代内恢复最优学生模型
