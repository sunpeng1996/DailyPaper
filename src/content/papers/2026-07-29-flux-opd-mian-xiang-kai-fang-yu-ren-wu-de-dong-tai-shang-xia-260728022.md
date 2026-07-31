---
title: 'Flux-OPD: On-Policy Distillation with Evolving Contexts'
title_zh: Flux-OPD：面向开放域任务的动态上下文在策略蒸馏方法
authors:
- Yuran Wang
- Zekun Wang
- Bohan Zeng
- Ruixu Zhang
- Wenxuan Liu
- Liu Yang
- Yifan Dai
- Yang Shi
- Bozhou Li
- Chengzhuo Tong
affiliations:
- Peking University
- Tsinghua University
- Shanghai Jiao Tong University
- Kling Team
- Zhongguancun Academy
arxiv_id: '2607.28022'
url: https://arxiv.org/abs/2607.28022
pdf_url: https://arxiv.org/pdf/2607.28022
published: '2026-07-29'
collected: '2026-07-31'
category: Training
direction: 大模型训练 · 在策略蒸馏优化
tags:
- On-Policy Distillation
- Context Distillation
- Knowledge Distillation
- LLM Training
- Reverse KL
one_liner: 通过反向KL分解优化动态上下文蒸馏策略，解决开放域任务蒸馏不稳定痛点
practical_value: '- 生成式推荐/Agent对齐场景下，可不用直接拟合带上下文的大模型输出，改用上下文与无上下文输出的差值作为校正信号，锚定基础模型分布避免训练震荡

  - 多规则/多反馈场景的蒸馏可借鉴冲突度动态加权机制：多上下文输出冲突高时降低校正强度，避免矛盾信号干扰训练

  - 推荐小模型迭代可复用动态上下文范式：每次迭代从当前模型的曝光点击轨迹提取经验作为上下文蒸馏进小模型，无需频繁全量重训'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
开放域LLM训练缺乏可验证奖励，任务偏好难以转化为有效监督信号；传统固定上下文蒸馏的信息被学生吸收后无额外增益，直接用动态演化上下文做监督又会导致蒸馏目标漂移、分布冲突，训练不稳定效果差。

### 方法关键点
- 反向KL目标分解：反向KL下学生是向上下文条件教师的几何均值蒸馏，目标中天然存在衡量多教师分布冲突的冲突项，冲突项不直接产生学生梯度
- 迭代训练流程：每个训练迭代分为上下文提取和上下文蒸馏两步，从当前学生的生成轨迹中由教师提取新的经验上下文，更新上下文池
- 上下文校正策略：以稳定的无上下文教师为锚点，将上下文条件教师和无上下文教师的对数概率差作为校正信号，插值得到最终蒸馏目标，避免目标大幅漂移
- 上下文加权策略：用冲突项作为冲突度指标，动态调整校正强度，上下文一致性高时增强校正，冲突大时削弱校正，降低矛盾信号影响

### 关键结果
在视频生成Prompt优化、医疗问答两个开放域任务上测试，对比OPD、OPCD、OEL三个基线：医疗问答任务总得分20.61，比次优OEL高4.8%；视频生成VBench平均得分80.18，比次优OPD高1.1%；训练过程无OEL的损失突增问题，OOD泛化性比OPD高4.5%。

最值得记住的一句话：动态上下文蒸馏不要直接拟合带上下文的教师输出，而是用上下文差异信号校正稳定基模型，同时用冲突度控制校正强度，兼顾效果和训练稳定性。
